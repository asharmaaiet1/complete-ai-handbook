# Contributing to Complete AI Handbook

This project is a public educational resource for software developers. Its initial preview is maintained by the project owner.

## Approval before implementation

Contributions follow an approval-first process:

1. Open a **Contribution Request** issue using the provided form. Describe the learning gap, proposed scope, and intended files or examples.
2. Wait for an explicit written approval from the project owner and an agreed scope. An unanswered request is not approval.
3. After approval, the owner will confirm whether collaborator access is needed and how to submit the work.
4. Do not begin work intended for submission or open a pull request before approval. Public bug reports and questions are welcome, but do not grant contribution access.
5. Every pull request requires maintainer review and approval before merge. The owner retains final merge authority.

Repository files describe this process but cannot enforce it. Before inviting contributions, the owner must configure GitHub to restrict pull requests to approved collaborators and protect `main`; see [`GITHUB_MANUAL_SETUP.md`](GITHUB_MANUAL_SETUP.md).

## Approved work workflow

After approval and collaborator access:

1. Agree on the change's scope and relevant files.
2. Create a descriptive branch.
3. Make only the approved change and preserve existing useful content.
4. Run the checks below and include any limitations in the pull request.
5. Open a pull request using the repository template and wait for maintainer review.

```bash
python -m pip install -r requirements-dev.txt
ruff check .
pytest -q
mkdocs build --strict
```

Use Python 3.12 for the project checks. CI runs the same tools on Python 3.12. Do not claim checks passed unless they were run successfully.

## Content quality

Major tutorials should include clear learning objectives, prerequisites, a technically sound explanation, worked examples where useful, limitations, exercises, and references. Link important factual claims to reliable sources near the claim. Clearly distinguish established knowledge, assumptions, and unsettled terminology. Mark draft content honestly.

Use [`TUTORIAL_TEMPLATE.md`](TUTORIAL_TEMPLATE.md). Code should be executable with documented versions or clearly labeled as pseudocode. Keep lesson snippets synchronized with maintained examples.

## Code and data

- Python examples should use type hints where appropriate and pass Ruff checks.
- TypeScript examples should use strict types and document setup and environment variables.
- Document dependencies and test commands; do not add dependencies without a clear need.
- Use synthetic or explicitly licensed data. Never include secrets, credentials, private personal data, or unauthorized datasets.
- Treat model output and retrieved content as untrusted. Explain security limits for examples involving tools, code execution, or sensitive data.

## References and assets

Prefer primary research and official documentation. Do not invent citations, benchmarks, or results. Preserve third-party notices, provide source and license details, and make clear which material is excluded from the project licenses.

## Pull request and automated checks

The pull request should explain what changed, why it is in the approved scope, and which learning domains it affects. Before requesting review, run `ruff check .`, `pytest -q`, and `mkdocs build --strict` as applicable. The PR checklist mirrors these checks; CI results are required but do not replace technical, educational, security, or license review.

## Reuse and contributions

This is a personal project, not an open-source or open-content release. Please ask before copying or reposting its original code or lessons. Third-party material belongs to its respective authors.

The approval-first process still applies. Owner approval to begin work is not automatic permission to copy or publish a finished contribution. Before work is accepted, the contributor and owner should agree simply on how it can be included and credited.

## Community

Be respectful and constructive. See [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md). For security concerns, follow [`SECURITY.md`](SECURITY.md); do not post exploit details publicly.
