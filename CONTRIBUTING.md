# Contributing

Thanks for helping improve UI Invariant Ledger.

This project should stay small, practical, and evidence-driven. Prefer changes backed by real frontend edits, not theoretical completeness.

## Good Contributions

- Verified examples from real UI changes.
- Clearer Risk Gate wording after repeated misclassification.
- Better output trimming rules when ledgers are too verbose.
- Documentation that helps reviewers understand what was checked, inspected, assumed, or not checked.
- Compatibility fixes for Codex, Claude Code, OpenCode, or other Agent Skills consumers.

## Non-Goals

- Persistent ledgers by default.
- Detector scripts or custom CLI before real need is proven.
- Claims of zero regressions or complete verification.
- Long policy documents inside `SKILL.md`.

## Before Opening A Pull Request

Run:

```bash
python3 scripts/validate_skill.py
gh skill publish --dry-run
```

If you change the skill itself, also check:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py skills/ui-invariant-ledger
```

## Writing Examples

Examples should include:

- request;
- before/after or clear surface description;
- expected skill output;
- evidence labels;
- not-checked behavior;
- why the mode is `MICRO`, `CHECKPOINT`, or `LEDGER`.

Avoid examples that imply the skill guarantees safety.

## Release Notes

Update `CHANGELOG.md` for user-visible changes.

Use patch releases for documentation, validation, and compatibility fixes. Use minor releases when behavior guidance changes enough that users should deliberately adopt it.
