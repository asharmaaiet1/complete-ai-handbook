# Contributing to Complete AI Handbook

Thank you for considering contributing to Complete AI Handbook.

This project aims to create a comprehensive, technically accurate and practical AI learning resource for software developers. We welcome contributions from developers, researchers, educators and AI enthusiasts.

## 1. Ways to contribute

- Create new tutorials.
- Improve explanations or correct technical inaccuracies.
- Add mathematical examples and runnable code.
- Create architecture diagrams.
- Explain research papers.
- Add practical projects and coding exercises.
- Improve documentation and fix broken references.

## 2. Before you start

1. Check existing issues and pull requests.
2. Search for an existing tutorial on your proposed topic.
3. Open an issue for substantial new content.
4. Discuss the scope before starting large contributions.

Small typo fixes and straightforward corrections do not require an issue.

## 3. Development workflow

1. Fork the repository.
2. Clone your fork.
3. Create a descriptive branch.
4. Make your changes.
5. Validate Markdown and code.
6. Test executable examples.
7. Submit a pull request.

```bash
git clone https://github.com/asharmaaiet1/complete-ai-handbook.git
cd complete-ai-handbook
git checkout -b content/your-topic
git add .
git commit -m "docs: add your topic"
git push origin content/your-topic
```

## 4. Content quality

Major tutorials should explain prerequisites, learning objectives, motivation, internal mechanisms, relevant mathematics, implementation, limitations, exercises and credible references.

Do not copy content from other websites, books, courses or repositories. Paraphrased research must be attributed. Clearly label opinions, experimental results and unverified claims.

Use the [tutorial template](TUTORIAL_TEMPLATE.md).

## 5. Code quality

### Python

- Follow PEP 8.
- Use type hints where appropriate.
- Use Ruff for linting and formatting.
- Use Pytest for tests.
- Document and constrain dependencies.

### TypeScript

- Use strict TypeScript.
- Follow the project's formatting and linting rules.
- Document required environment variables.
- Test important functionality.

All examples should be reproducible using documented setup instructions.

Never commit API keys, passwords, private credentials, personal information, unauthorized datasets or unapproved large model files. Use `.env.example` for environment-variable documentation.

## 6. Diagrams and visual assets

- Prefer Mermaid for simple diagrams.
- Use editable draw.io source for complex diagrams.
- Explain diagrams in the accompanying tutorial.
- Credit third-party visual assets and respect their licenses.

## 7. Research and references

Prioritize original research papers, official technical documentation, reputable academic publications and established engineering resources. Link to original sources where possible. Do not invent benchmarks, performance claims or research results.

## 8. Pull requests

A pull request should have a descriptive title, explain what changed and why, identify affected domains, include references where applicable, and confirm that code and documentation checks have been run.

## 9. Review process

Contributions are evaluated for technical correctness, educational value, clarity, originality, code quality, reproducibility, reference quality and security implications. Maintainers may request revisions.

## 10. Community conduct

Be respectful, constructive and inclusive. Technical disagreement is welcome when supported by evidence. Harassment, personal attacks and discriminatory behavior are not acceptable. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## 11. Licensing

By submitting a contribution, you confirm that you have the right to contribute it. Source code is distributed under Apache License 2.0; original educational documentation is distributed under CC BY-SA 4.0. Third-party material remains subject to its own license and attribution requirements.

## 12. Our philosophy

Understand before implementing. Verify before teaching. Build before recommending. Document before assuming.

Thank you for helping make AI education more accessible.
