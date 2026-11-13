"""Repository integrity checks for the public preview."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from yaml.nodes import MappingNode, ScalarNode, SequenceNode

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FENCED_BLOCK = re.compile(r"^\s*(```+|~~~+).*?^\s*\1\s*$", re.MULTILINE | re.DOTALL)
INLINE_LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)

CANONICAL_LESSONS = (
    "what-is-ai.md",
    "ai-vs-ml-vs-dl.md",
    "history-of-ai.md",
    "types-of-ai.md",
    "ai-applications.md",
)


def _markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts
        and "site" not in path.parts
        and "release-package" not in path.parts
    )


def _heading_slugs(content: str) -> set[str]:
    slugs: set[str] = set()
    counts: dict[str, int] = {}
    for match in HEADING.finditer(content):
        heading = INLINE_LINK.sub(r"\1", match.group(1))
        heading = heading.replace("`", "").replace("**", "").replace("*", "")
        base = re.sub(r"[^\w\- ]", "", heading.lower(), flags=re.UNICODE)
        base = re.sub(r"\s+", "-", base.strip())
        count = counts.get(base, 0)
        counts[base] = count + 1
        slugs.add(base if count == 0 else f"{base}-{count}")
    return slugs


def _local_markdown_targets(source: Path) -> list[tuple[str, str]]:
    content = FENCED_BLOCK.sub("", source.read_text(encoding="utf-8"))
    targets: list[tuple[str, str]] = []
    for match in MARKDOWN_LINK.finditer(content):
        raw_target = match.group(1).strip()
        target = raw_target.split(maxsplit=1)[0].strip("<>") if raw_target else ""
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            continue
        targets.append((unquote(parsed.path), unquote(parsed.fragment)))
    return targets


def _resolve_markdown_target(source: Path, target_path: str) -> Path:
    candidate = (source.parent / target_path).resolve() if target_path else source.resolve()
    if candidate.is_dir():
        for index_name in ("index.md", "README.md"):
            index = candidate / index_name
            if index.is_file():
                return index
    return candidate


def test_local_markdown_links_and_anchors_resolve() -> None:
    broken: list[str] = []
    for source in _markdown_files():
        for target_path, fragment in _local_markdown_targets(source):
            resolved = _resolve_markdown_target(source, target_path)
            if not resolved.exists():
                broken.append(f"{source.relative_to(ROOT)} -> {target_path or '#'}")
            elif fragment and resolved.suffix == ".md":
                headings = _heading_slugs(resolved.read_text(encoding="utf-8"))
                if fragment.lower() not in headings:
                    broken.append(
                        f"{source.relative_to(ROOT)} -> {target_path}#{fragment} (missing heading)"
                    )
    assert not broken, "Broken local Markdown links:\n" + "\n".join(broken)


def _navigation_pages(nav: object) -> list[str]:
    if isinstance(nav, str):
        return [nav]
    if isinstance(nav, list):
        return [page for item in nav for page in _navigation_pages(item)]
    if isinstance(nav, dict):
        return [page for item in nav.values() for page in _navigation_pages(item)]
    return []


def _plain_yaml_node(node: object) -> object:
    if isinstance(node, ScalarNode):
        return node.value
    if isinstance(node, SequenceNode):
        return [_plain_yaml_node(child) for child in node.value]
    if isinstance(node, MappingNode):
        return {_plain_yaml_node(key): _plain_yaml_node(value) for key, value in node.value}
    return None


def test_mkdocs_navigation_pages_exist() -> None:
    config_path = ROOT / "mkdocs.yml"
    config = _plain_yaml_node(yaml.compose(config_path.read_text(encoding="utf-8")))
    assert isinstance(config, dict)
    docs_dir = ROOT / config.get("docs_dir", "docs")
    missing = [
        page
        for page in _navigation_pages(config.get("nav", []))
        if not (docs_dir / page).is_file()
    ]
    assert not missing, "MkDocs navigation points to missing pages: " + ", ".join(missing)


def test_repository_yaml_files_parse() -> None:
    yaml_files = [
        ROOT / "mkdocs.yml",
        *ROOT.joinpath(".github").rglob("*.yml"),
        *ROOT.joinpath(".github").rglob("*.yaml"),
    ]
    for path in yaml_files:
        yaml.compose(path.read_text(encoding="utf-8"))


def test_contribution_request_form_has_expected_required_fields() -> None:
    path = ROOT / ".github" / "ISSUE_TEMPLATE" / "contribution-request.yml"
    form = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert form["name"] == "Contribution Request"
    fields = {item.get("id"): item for item in form["body"] if item.get("id")}
    assert {"github-username", "contribution-area", "proposal", "scope", "acknowledgements"} <= set(fields)
    assert fields["proposal"]["validations"]["min_length"] == 50


def test_five_preview_lessons_are_present_and_marked_as_drafts() -> None:
    lessons_dir = ROOT / "docs" / "start-here"
    for name in CANONICAL_LESSONS:
        path = lessons_dir / name
        content = path.read_text(encoding="utf-8")
        assert content.startswith("---\n"), f"Missing YAML front matter: {path}"
        front_matter = content.split("---\n", 2)[1]
        metadata = yaml.safe_load(front_matter)
        assert metadata["status"] == "draft", f"Preview lesson is not marked draft: {path}"
        assert "last_updated" in metadata, f"Missing update date: {path}"
        assert len(content) >= 1000, f"Lesson content appears incomplete: {path}"


def test_root_lesson_pages_point_to_canonical_documentation() -> None:
    for name in CANONICAL_LESSONS:
        path = ROOT / "00-start-here" / name
        content = path.read_text(encoding="utf-8")
        canonical = f"../docs/start-here/{name}"
        assert canonical in content, f"Root lesson does not point to canonical source: {path}"


def test_generated_and_local_environment_artifacts_are_not_tracked() -> None:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    tracked = [Path(item.decode("utf-8")) for item in result.stdout.split(b"\0") if item]
    forbidden_parts = {
        ".venv",
        "venv",
        "site",
        ".pytest_cache",
        ".ruff_cache",
        ".mypy_cache",
        "__pycache__",
        "dist",
        "build",
        "htmlcov",
    }
    forbidden = [
        path.as_posix()
        for path in tracked
        if any(part in forbidden_parts for part in path.parts)
        or (path.name.startswith(".env") and path.name != ".env.example")
        or path.name == "complete-ai-handbook-initial-preview-replacements.zip"
    ]
    assert not forbidden, "Generated or local environment files are tracked: " + ", ".join(forbidden)
