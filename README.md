# Complete AI Handbook

### From Zero to AI Engineer

**Understand AI. Build AI. Engineer AI.**

A public personal learning project for software developers learning artificial intelligence, machine learning, and AI application engineering.

> **Release status: Initial Public Preview.** This preview provides five beginner-level AI fundamentals lessons and a small documentation site. The remaining curriculum, runnable Python and TypeScript examples, and production engineering material are planned; they are not included as completed content.

## Available lessons

The canonical lesson sources are in [`docs/start-here/`](docs/start-here/README.md), which MkDocs publishes as the learning site.

- [What Is Artificial Intelligence?](docs/start-here/what-is-ai.md)
- [AI vs. Machine Learning vs. Deep Learning](docs/start-here/ai-vs-ml-vs-dl.md)
- [A Short History of Artificial Intelligence](docs/start-here/history-of-ai.md)
- [Major Approaches and Types of AI](docs/start-here/types-of-ai.md)
- [AI Applications in the Real World](docs/start-here/ai-applications.md)

All five lessons are drafts for this preview. They are introductory reading, not a substitute for technical review or domain-specific advice.

## Planned curriculum

Mathematics, Python for AI, data engineering, machine learning, deep learning, NLP, computer vision, generative AI, LLMs, retrieval, agents, AI application engineering, MLOps, security, projects, and assessments are planned areas. Their directory pages are scope notes, not completed tutorials. See [ROADMAP.md](ROADMAP.md) for release intent.

## Learning approach

The handbook aims to pair theoretical foundations with practical implementation. Python is intended for mathematics, data science, and machine learning; TypeScript is a first-class language for AI application engineering. The current preview is documentation-only and does not yet contain executable examples.

## Build the documentation site

Use Python 3.12 and install the pinned documentation dependencies:

```bash
python3.12 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements-docs.txt
mkdocs serve
```

On Windows, create the environment with `py -3.12 -m venv .venv`.

For a release check, run `mkdocs build --strict`.

## Contributing

The repository is public to read and fork. Contributions require an approved proposal before implementation intended for submission. Only explicitly approved collaborators should open pull requests. Read [CONTRIBUTING.md](CONTRIBUTING.md). Repository settings must enforce the stated policy; the files alone cannot do so.

## Copyright and reuse

This is a personal project maintained by `@asharmaaiet1`. You are welcome to read it on GitHub. Please ask before copying, reposting, redistributing, or reusing the project's original code or lessons. See [`LICENSE`](LICENSE) and [`LICENSE-DOCS`](LICENSE-DOCS) for the short notices.

Third-party sources and material remain with their respective authors. The project aims to credit the sources it uses.

GitHub allows people to view and fork public repositories under its platform terms. A copyright notice does not turn off GitHub's fork feature. Making the repository private can stop new public access, but existing forks and local copies remain. See [GitHub's explanation of public repository licensing and forks](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository).

## Project status

This is an early preview, not a completed course or a claim that every listed topic is available. Check each lesson's draft status and references. See [CHANGELOG.md](CHANGELOG.md) for project history and [CONTRIBUTING.md](CONTRIBUTING.md) for the approval-first contribution process.
