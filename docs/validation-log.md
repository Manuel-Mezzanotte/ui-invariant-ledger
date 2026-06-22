# Validation Log

This log records public release and repository checks that are useful before promoting the project more widely.

## 2026-06-23 - v0.1.6 Public Readiness Check

Repository: `Manuel-Mezzanotte/ui-invariant-ledger`

Checked by: Codex

### GitHub Topics

Result: passed.

Changed repository topics:

- removed `devel`;
- added `developer-tools`.

Current topics:

```text
agent-skills
ai
ai-agents
ai-coding
ai-tools
claude-code
codex
coding-agents
cursor
frontend
frontend-development
markdown
opencode
skills
ui
ux
developer-tools
```

### Latest Release

Result: passed.

Command:

```bash
gh release list --repo Manuel-Mezzanotte/ui-invariant-ledger --limit 6
```

Observed result:

```text
v0.1.6    Latest    v0.1.6    2026-06-22T21:39:29Z
v0.1.5              v0.1.5    2026-06-22T21:10:02Z
v0.1.4              v0.1.4    2026-06-22T21:00:59Z
v0.1.3              v0.1.3    2026-06-22T20:56:11Z
v0.1.2              v0.1.2    2026-06-22T20:39:34Z
v0.1.1              v0.1.1    2026-06-22T20:34:30Z
```

GitHub API also reports:

```text
latestRelease.tagName: v0.1.6
latestRelease.url: https://github.com/Manuel-Mezzanotte/ui-invariant-ledger/releases/tag/v0.1.6
```

Note: the unauthenticated public `/releases` page can lag briefly because of GitHub rendering or cache behavior. The release-specific page, GitHub CLI, and GitHub API all reported `v0.1.6` as the latest release during this check.

### CI

Result: passed.

Latest workflow run:

```text
workflow: ci.yml
commit: 50624f9
title: docs: add v1 readiness plan
status: completed
conclusion: success
url: https://github.com/Manuel-Mezzanotte/ui-invariant-ledger/actions/runs/27985838557
```

### Local Repository Validation

Result: passed.

Command:

```bash
python3 scripts/validate_skill.py
```

Output:

```text
Skill repository validation passed.
```

### GitHub Skill Publish Dry Run

Result: passed with non-blocking warning.

Command:

```bash
gh skill publish --dry-run
```

Output:

```text
Dry run complete. Use without --dry-run to publish.
warning    no active tag protection rulesets found. Consider protecting tags to ensure immutable releases (Settings > Rules > Rulesets)
```

The warning is expected until tag protection rulesets are configured manually in GitHub repository settings.
