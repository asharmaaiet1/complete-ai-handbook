# GitHub Manual Setup for Initial Public Preview

Repository files cannot change GitHub repository settings. The owner must perform and verify these steps before inviting contributions or relying on the security policy.

## 1. Restrict contribution access

In the repository, open **Settings → General → Pull Requests** and select **Collaborators only**. This preserves the project's approval-first contribution policy; only invited collaborators can open pull requests. Review the GitHub instructions for [restricting pull requests to collaborators](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/disabling-pull-requests).

When a proposal is approved, invite only the contributor who needs access and grant the minimum role required. Remove access when it is no longer needed.

This setting restricts who may open pull requests; it does not disable forks of a public repository. GitHub permits people to view and fork public repositories under its platform terms. Making the repository private can stop new public access, but existing forks and local copies remain. If preventing new public forks matters more than public reading, choose private repository visibility.

## 2. Protect `main`

Create a branch protection rule or repository ruleset targeting `main`:

- Require a pull request before merging.
- Require at least one approving review from the project owner/maintainer.
- Require review from code owners; `.github/CODEOWNERS` currently names only `@asharmaaiet1`.
- Dismiss stale approvals when new commits are pushed.
- Require the latest CI checks before merge: the documentation build and Python/repository checks. Select the exact status contexts after the workflows have run once.
- Block force pushes and branch deletion.
- Do not grant routine bypass to contributors; decide explicitly whether administrators can bypass the rules.

GitHub documents [protected branch review requirements](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) and [CODEOWNERS behavior](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners). CODEOWNERS requests review; only the branch rule makes its approval a merge requirement. Ensure `.github/CODEOWNERS` itself is owned, as configured in this package.

## 3. Enable and monitor private vulnerability reporting

Open **Settings → Security & analysis** (GitHub may label this area **Security and quality**) and enable **Private vulnerability reporting**. Confirm the **Report a vulnerability** form is visible and that owner/admin notifications are monitored. GitHub explains [how to enable private reporting](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository).

Do not direct reporters to public issues for exploit details. If the feature is unavailable, configure an appropriate private route before inviting security reports; do not publish an email address unless the owner chooses and monitors one.

## 4. Verify the release controls

- Confirm the repository's default branch is `main` and the rules apply to it.
- Confirm the `@asharmaaiet1` account is the intended owner and can review the required checks.
- Choose a monitored private contact route for Code of Conduct reports and update that policy if the current route is not actionable; do not invent an email address.
- Confirm contributors cannot bypass required review and status checks.
- Confirm branch protection does not make the owner unable to merge an approved pull request.
- After initial CI runs, verify that both required status checks are selected and block merging when they fail.
- Check notification settings so private vulnerability reports reach a monitored account.

These settings were not changed or inspected as part of creating the replacement package.
