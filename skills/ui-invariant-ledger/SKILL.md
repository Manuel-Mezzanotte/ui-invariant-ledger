---
name: ui-invariant-ledger
description: Use when modifying existing frontend UI code. Adds risk-scaled checkpoints so AI agents preserve observable UI behavior, distinguish checked evidence from inspected code, and report what remains unverified.
---

# UI Invariant Ledger

## Purpose

Preserve observable frontend behavior while editing existing UI code.

Use risk-scaled checkpoints before and after the diff:

- `MICRO` for tiny changes that cannot change observable behavior.
- `CHECKPOINT` for local UI changes where side effects are possible.
- `LEDGER` for stateful, data-driven, accessible, or multi-surface UI changes.

## Core Rule

If behavior can change, the task is never `MICRO`.

Risk is determined by touched concerns, not by diff size. Read `references/risk-gate.md` when classifying a non-trivial task or when the diff touches behavior-related code.

## Required Model

Use `Preserve / Permit / Probe`:

- `Preserve`: behavior that must not change accidentally.
- `Permit`: change the request allows.
- `Probe`: unknowns, assumptions, or unverified areas to surface.

Use evidence terms precisely:

- `CHECKED`: verified with an actual test, command, browser path, viewport, keyboard path, or concrete check.
- `INSPECTED`: read in code or diff, without independent verification.
- `ASSUMED`: inferred from a pattern or context.
- `STALE`: previous evidence not reconfirmed for the current task.

## Required Outputs

For `MICRO`, write a compact micro-check. Keep it under 80 tokens. Do not use tables.

For `CHECKPOINT`, use `assets/checkpoint-template.md` as the shape. Keep it compact by default.

For `LEDGER`, use `assets/ledger-template.md` as the shape. Include invariant delta and reviewer focus.

## Post-Diff Risk Recheck

After editing, rerun the Risk Gate against the actual diff. Escalate the mode when the diff touched behavior-related concerns that were not included in the initial mode.

## Language Rules

Do not claim guaranteed safety. Avoid phrases such as "no regressions", "fully verified", "everything works", or "safe".

Prefer concrete evidence language: "checked with typecheck", "inspected in code", "not checked in browser", "assumed from existing pattern".
