# Applied Remediation Manifest

This manifest records the preview remediation files and their repository-relative destinations. The replacements have been applied to the repository root.

`release-package/` is retained as a local reference copy of the replacement set and is excluded from Git. Do not add that duplicate folder to the public repository. The replacement archive is no longer present after application. The remaining owner actions are the GitHub settings and confirming source credits; see `GITHUB_MANUAL_SETUP.md` and `ATTRIBUTION_REVIEW.md`.

| Package path / destination path | Status in current checkout | Why included and what changed |
|---|---|---|
| `.github/CODEOWNERS` | Replacement of current untracked file | Keeps the configured owner `@asharmaaiet1` as the only reviewer and explicitly routes CODEOWNERS edits to the owner. |
| `.github/ISSUE_TEMPLATE/contribution-request.yml` | Updated | Makes explicit approval and scope a prerequisite; records rights and policy acknowledgements without inventing maintainers. |
| `.github/PULL_REQUEST_TEMPLATE.md` | Updated | Aligns the PR checklist with approval-first governance, references, privacy/security, and the actual CI commands. |
| `.github/workflows/docs-build.yml` | Updated | Uses Python 3.12, pinned documentation requirements and immutable action SHAs, least-privilege read permissions, timeout, concurrency, and a strict MkDocs build. |
| `.github/workflows/python-tests.yml` | Updated | Uses Python 3.12, pinned development requirements and immutable action SHAs, runs Ruff and discovered pytest checks, and uses read-only permissions. |
| `.gitignore` | Updated | Excludes Python/tool caches, local environments, generated site/build output, local env files, and the requested ZIP. |
| `00-start-here/README.md` | Updated | Makes `docs/start-here/` canonical and links directly to the five full lessons. |
| `00-start-here/ai-applications.md` | Updated | Retains a short redirect page to its canonical full lesson. |
| `00-start-here/ai-vs-ml-vs-dl.md` | Updated | Retains a short redirect page to its canonical full lesson. |
| `00-start-here/history-of-ai.md` | Updated | Retains a short redirect page to its canonical full lesson. |
| `00-start-here/types-of-ai.md` | Updated | Retains a short redirect page to its canonical full lesson. |
| `00-start-here/what-is-ai.md` | Updated | Retains a short redirect page to its canonical full lesson. |
| `ATTRIBUTION_REVIEW.md` | New | States the personal project attribution and gives simple source-credit and contribution guidance. |
| `CHANGELOG.md` | Updated | Preserves existing history and records the preview scope, license, CI, and repository-governance remediation in the Unreleased section. |
| `CODE_OF_CONDUCT.md` | Replacement copy; content unchanged | Preserves the existing conduct policy referenced by contributor guidance. |
| `CONTRIBUTING.md` | Updated | States approval-before-work, access and review expectations, actual checks, safe code/data guidance, and the simple ask-before-copying notice. |
| `GITHUB_MANUAL_SETUP.md` | New | Lists settings that repository files cannot apply: collaborator-only PRs, main branch protection, code-owner review, CI status checks, and private vulnerability reporting. |
| `LICENSE` | Updated | Uses a short personal copyright notice for original code and configuration instead of an open-source license. |
| `LICENSE-DOCS` | Updated | Uses a short personal copyright notice for original lessons instead of an open-content license. |
| `README.md` | Updated | Identifies Initial Public Preview scope, lists available lessons, describes planned work, and explains the personal reuse notice and GitHub fork limitation. |
| `ROADMAP.md` | Updated | Separates the current preview from future work and sets an explicit content review gate. |
| `SECURITY.md` | Updated | Provides safe private reporting instructions and states that GitHub private vulnerability reporting must be enabled and monitored manually. |
| `TUTORIAL_TEMPLATE.md` | Updated | Adds claim-level sourcing, tested setup, honest pseudocode labeling, and review metadata that distinguishes last update from completed review. |
| `docs/index.md` | Updated | Labels the site as an initial preview and limits its claims to the five published introductory lessons. |
| `docs/learning-paths.md` | Updated | Shows the one available fundamentals path and explicitly labels all other learning paths as planned. |
| `docs/javascripts/mermaid.js` | Replacement copy; content unchanged | Retains the existing strict Mermaid initialization script required by the MkDocs configuration. |
| `docs/start-here/README.md` | Updated | Serves as the AI Fundamentals overview, lists the five lessons in sequence, and previews AI history. |
| `docs/start-here/ai-applications.md` | Updated | Preserves the full lesson, adds nearby risk-source context, and changes draft metadata from review date to update date. |
| `docs/start-here/ai-vs-ml-vs-dl.md` | Updated | Preserves the full lesson and changes draft metadata from review date to update date. |
| `docs/start-here/history-of-ai.md` | Updated | Preserves the full lesson, adds inline links to the historical primary sources already listed, and changes draft metadata to update date. |
| `docs/start-here/types-of-ai.md` | Updated | Preserves the full lesson, adds a nearby risk-framework reference, and changes draft metadata to update date. |
| `docs/start-here/what-is-ai.md` | Updated | Preserves the full lesson, adds nearby context for its practical definition, and changes draft metadata to update date. |
| `mkdocs.yml` | Updated | Identifies the preview and pins Mermaid to exact version 12.3.0 while keeping the existing navigation. |
| `pyproject.toml` | Updated | Aligns Ruff's target version with Python 3.12. |
| `requirements-dev.txt` | New | Pins pytest, PyYAML, and Ruff and includes the pinned documentation dependencies for reproducible local/CI checks. |
| `requirements-docs.txt` | Replacement copy; content unchanged | Carries the repository's existing exact MkDocs dependency pins into the complete overlay package. |
| `tests/test_repository.py` | Replacement of current untracked test file | Checks internal Markdown paths and heading anchors, MkDocs nav, YAML syntax, the five draft lessons, canonical pointers, and tracked generated/local artifacts. |
| `REPLACEMENT_MANIFEST.md` | New | Inventories the replacement files and records the remaining manual GitHub setup. |

## Owner decisions still required

- Configure and verify the GitHub settings in `GITHUB_MANUAL_SETUP.md`.
- Review the third-party sources and confirm the current credits are adequate.

## Review notes

The five full AI fundamentals lesson files are copied from the current canonical documentation sources and retained. The root numbered lesson files remain short links, so the text has one canonical location rather than two drifting copies. Three lesson update dates changed from `last_reviewed` to `last_updated` because the lessons remain drafts and are not represented as substantively reviewed.
