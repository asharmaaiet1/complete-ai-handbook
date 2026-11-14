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

All five lessons are published introductory reading. Publication does not mean expert review, and they are not a substitute for domain-specific advice.

## Module status

The table shows what is available now and what remains planned. A module marked **Planned** is a curriculum outline, not a completed tutorial. Published lessons are introductory and have not necessarily received expert review.

| Module | Focus | Status |
| --- | --- | --- |
| [00 · AI Fundamentals](docs/start-here/README.md) | AI fundamentals | **Published** · five lessons |
| [01 · Mathematics for AI](01-mathematics-for-ai/README.md) | Linear algebra, calculus, probability, and statistics | Planned |
| [02 · Python for AI](02-python-for-ai/README.md) | Python programming and scientific tools | Planned |
| [03 · Data Engineering](03-data-engineering/README.md) | Data collection, preparation, and pipelines | Planned |
| [04 · Machine Learning](04-machine-learning/README.md) | Classical ML, training, and evaluation | Planned |
| [05 · Deep Learning](05-deep-learning/README.md) | Neural networks and deep learning frameworks | Planned |
| [06 · Natural Language Processing](06-natural-language-processing/README.md) | NLP methods and language applications | Planned |
| [07 · Computer Vision](07-computer-vision/README.md) | Image and video understanding | Planned |
| [08 · Generative AI](08-generative-ai/README.md) | Generative models and applications | Planned |
| [09 · Large Language Models](09-large-language-models/README.md) | LLM architecture, training, and inference | Planned |
| [10 · Prompt and Context Engineering](10-prompt-and-context-engineering/README.md) | Prompting, context design, and evaluation | Planned |
| [11 · Embeddings and Vector Search](11-embeddings-and-vector-search/README.md) | Embeddings, similarity, and vector indexes | Planned |
| [12 · Retrieval-Augmented Generation](12-retrieval-augmented-generation/README.md) | Retrieval systems and RAG | Planned |
| [13 · AI Agents](13-ai-agents/README.md) | Tool use, workflows, and agent evaluation | Planned |
| [14 · Fine-Tuning and Model Training](14-fine-tuning-and-model-training/README.md) | Adaptation and training workflows | Planned |
| [15 · AI Application Engineering](15-ai-application-engineering/README.md) | Building AI-powered applications | Planned |
| [16 · MLOps and LLMOps](16-mlops-and-llmops/README.md) | Deployment, monitoring, and operations | Planned |
| [17 · AI Security and Governance](17-ai-security-and-governance/README.md) | Safety, security, privacy, and governance | Planned |
| [18 · AI System Design](18-ai-system-design/README.md) | Architecture and system design | Planned |
| [19 · Specialization Paths](19-specialization-paths/README.md) | Focused learning tracks | Planned |
| [20 · Projects](20-projects/README.md) | Hands-on projects | Planned |
| [21 · Research Papers](21-research-papers/README.md) | Guided research-paper reading | Planned |
| [22 · Interview Preparation](22-interview-preparation/README.md) | Interview topics and practice | Planned |
| [23 · Exercises and Assessments](23-exercises-and-assessments/README.md) | Practice exercises and assessments | Planned |

See [ROADMAP.md](ROADMAP.md) for release intent and future work.

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

This is an early preview, not a completed course or a claim that every listed topic is available. Check each lesson's references. See [CHANGELOG.md](CHANGELOG.md) for project history and [CONTRIBUTING.md](CONTRIBUTING.md) for the approval-first contribution process.
