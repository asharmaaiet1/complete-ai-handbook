# Security Policy

## Reporting a vulnerability

Please do not disclose exploitable vulnerabilities in a public issue.

Until a private security contact is configured, do not include secrets, personal data or exploit details in public discussions. The repository owner should configure GitHub's private vulnerability reporting and add a monitored security contact before accepting production-sensitive code.

## Scope

Security reports may concern:

- Exposed credentials or secrets.
- Unsafe code execution in examples.
- Insecure dependency or build configuration.
- Data leakage in sample applications.
- Authentication, authorization or tenant-isolation flaws.
- Prompt injection and unsafe tool-use demonstrations.
- Vulnerable dependencies.

## Safe contribution practices

- Never commit real API keys or credentials.
- Use synthetic or explicitly licensed datasets.
- Treat model output and retrieved documents as untrusted input.
- Validate and authorize tool calls on the server.
- Avoid executing generated code without isolation and explicit controls.
- Keep dependencies reviewed and updated.

Educational examples are not automatically production-safe. Each tutorial must explain relevant limitations.
