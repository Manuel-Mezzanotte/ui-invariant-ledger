# Design Notes

## Phase 0 Freeze

UI Invariant Ledger is a markdown-first Agent Skill for preserving observable frontend behavior during AI-assisted UI edits.

The v0.1 promise is reviewability, not zero bugs. The skill should make risk, assumptions, performed checks, and unverified areas visible before and after an edit.

## v0.1 Scope

- Provide one installable skill at `skills/ui-invariant-ledger/SKILL.md`.
- Use three modes: `MICRO`, `CHECKPOINT`, and `LEDGER`.
- Use the Risk Gate rule: if behavior can change, the task is never `MICRO`.
- Use `Preserve / Permit / Probe` for non-micro work.
- Distinguish `CHECKED`, `INSPECTED`, `ASSUMED`, and `STALE`.
- Re-run the Risk Gate after the actual diff.
- Keep output proportional to risk.

## Explicit Non-Scope

- No persistent `.ui-invariants/surfaces/*.md` ledger in v0.1.
- No mandatory scripts or custom CLI.
- No detector rules.
- No promise of zero regressions.
- No full ledger output for every micro task.

## Success Criteria

- Micro tasks stay small.
- Behavior-related changes cannot be classified as `MICRO`.
- Checked evidence is not conflated with inspected code.
- Unverified behavior is declared instead of hidden.
- Reviewer focus is short and useful.
