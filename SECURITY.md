# Security Policy

## Reporting a vulnerability

Please do not post credentials, personal data, exploit steps, or other sensitive vulnerability details in a public issue or discussion.

The owner should enable **Private vulnerability reporting** in the repository's GitHub Security settings before broad public release. When enabled, use the repository's **Report a vulnerability** flow in the Security tab to send a private report. GitHub settings and menu availability can vary by repository eligibility; the owner must verify the feature is enabled and monitored.

If private vulnerability reporting is unavailable or disabled, do not publish exploit details. Use GitHub's private contact route to the repository owner only if one is available. If no private route is available, wait until the owner configures one; this repository does not publish an email address for security reports.

Please include a concise impact description, affected paths or versions, and safe reproduction details only through a private channel. Allow the maintainer time to investigate and coordinate a fix before public disclosure.

## Scope

Reports may concern exposed credentials, unsafe example execution, vulnerable dependencies, data leakage, authorization errors, prompt injection or unsafe tool use, and insecure build or deployment instructions.

## Safe practices

- Never commit real credentials; use documented placeholder values.
- Use synthetic or explicitly licensed datasets.
- Treat model output and retrieved documents as untrusted input.
- Authorize tool calls on the server and avoid executing generated code without isolation.
- Review dependency and build changes.

Educational examples are not automatically production-safe. Each tutorial should explain relevant limitations and safeguards.
