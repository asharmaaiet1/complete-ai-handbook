## Approval and scope

- [ ] I received explicit project owner approval before starting this work.
- [ ] This pull request matches the approved scope.

## Description

What changed, why, and which user or learning need does it address?

## Learning domain

- [ ] AI fundamentals
- [ ] Mathematics / Python / data
- [ ] Machine learning / deep learning
- [ ] Generative AI / LLMs / retrieval / agents
- [ ] AI application engineering / production systems
- [ ] Other:

## Quality review

- [ ] Important technical claims have nearby credible references.
- [ ] Code is runnable with documented versions, or clearly marked as pseudocode.
- [ ] Internal Markdown links and MkDocs navigation are valid.
- [ ] No unauthorized third-party content, secrets, private data, or unlicensed datasets are included.
- [ ] Relevant security, privacy, limitations, and failure behavior are documented.
- [ ] I ran the automated checks below and report any failures or limits.

```text
ruff check .
pytest -q
mkdocs build --strict
```

CI results are required before merge; automated checks do not replace maintainer review.
