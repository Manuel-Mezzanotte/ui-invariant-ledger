---
name: ui-invariant-ledger
description: Use when modifying existing frontend UI code, especially refactors or visual changes to components, forms, modals, tables, navigation, responsive layouts, loading/error/empty states, data mapping, accessibility behavior, or design-system primitives. Adds risk-scaled checkpoints so agents preserve observable UI behavior, distinguish checked evidence from inspected code, and report what remains unverified.
---

# UI Invariant Ledger

## Purpose

Preserve observable frontend behavior while editing existing UI code. Make risk, assumptions, performed checks, and unverified behavior visible without turning every task into a long report.

This skill is not a design-taste guide and does not promise zero regressions.

## Workflow

1. Inspect the request and the affected UI surface.
2. Classify the task as `MICRO`, `CHECKPOINT`, or `LEDGER`.
3. Identify what to `Preserve`, `Permit`, and `Probe`.
4. Edit the code.
5. Re-run the Risk Gate against the actual diff.
6. Report the mode, evidence, unverified areas, and reviewer focus at the detail level required by the mode.

## Risk Gate

Core rule: if behavior can change, the task is never `MICRO`.

Risk is determined by touched concerns, not by diff size. A one-line change can be risky when it touches state, handlers, validation, accessibility, or public component contracts.

Read `references/risk-gate.md` when the task is not obviously `MICRO`, when the diff touches behavior-related code, or when the initial and actual risk may differ.

If unsure between two modes, choose the higher-risk mode.

## Modes

### MICRO

Use only for tiny edits that cannot change observable behavior.

Allowed examples:

- spacing-only class change on a static element;
- copy change with no conditional logic;
- tokenized color change with no state, interaction, or accessibility effect.

Forbidden when the change touches any concern listed in `references/risk-gate.md`.

Output: a micro-check under 80 tokens. Do not use tables or `Preserve / Permit / Probe`.

### CHECKPOINT

Use for local visual or structural changes where side effects are possible but behavior is not the main target.

Typical examples:

- reorganizing a card with existing loading/error branches nearby;
- changing layout in a responsive container;
- extracting markup while keeping props and conditions stable;
- replacing a visual loading indicator while preserving the pending state.

Output: compact `Preserve / Permit / Probe`, normally under 250 tokens. Use `assets/checkpoint-template.md` when a structured receipt helps. Keep to at most 3 `Preserve` items and 3 `Probe` items by default.

### LEDGER

Use when the change is stateful, data-driven, accessible, multi-surface, or behavior-facing.

Typical triggers:

- forms, validation, submit disabled logic, or pending states;
- modals, drawers, focus management, Escape behavior, keyboard paths, ARIA, labels, roles, or semantic elements;
- tables, filters, sorting, pagination, empty states, or row actions;
- data fetching, API mapping, error rendering, permissions, routing, destructive actions, payments, or user data;
- public props used outside the edited file.

Output: a ledger normally under 800 tokens. Use `assets/ledger-template.md` for the shape. Include invariant delta and reviewer focus.

## Preserve / Permit / Probe

Use this model for `CHECKPOINT` and `LEDGER`.

- `Preserve`: observable behavior that must not change accidentally.
- `Permit`: changes allowed by the request.
- `Probe`: unknowns, assumptions, or unverified behavior that should be surfaced.

Do not list a behavior under `Preserve` unless it is supported by evidence. Put uncertain behavior in `Probe`.

## Evidence Terms

Use only these evidence labels:

- `CHECKED`: verified with an actual test, typecheck, lint, browser path, viewport, keyboard path, command, or concrete runtime check.
- `INSPECTED`: read in code or diff, without independent verification.
- `ASSUMED`: inferred from surrounding patterns or naming.
- `STALE`: known from previous evidence but not reconfirmed in the current task.

Do not upgrade `INSPECTED` to `CHECKED` because the code "looks right". If a browser path, keyboard path, mobile viewport, or API error path was not run, say it was not checked.

## Post-Diff Risk Recheck

After editing, inspect the actual diff and rerun the Risk Gate.

Escalate when the diff touched a higher-risk concern than the initial mode allowed.

Example:

```text
Post-diff Risk Recheck:
- Initial mode: MICRO
- Actual diff touched: focus-visible class on an interactive element
- Escalated mode: CHECKPOINT
- Reason: visible focus behavior may have changed
```

If the mode did not change, say so briefly.

## Stop Rules

- Do not remove conditional branches, handlers, ARIA, labels, roles, disabled logic, loading/error/empty states, or API error handling just because their purpose is unclear.
- Do not claim a behavior is preserved when it was only assumed.
- Do not hide unverified responsive, keyboard, focus, or error behavior.
- For auth, permissions, payments, destructive actions, or user data, use `LEDGER` unless the diff is conclusively unrelated to behavior.

## Required Output Shapes

For `MICRO`:

```text
Micro-check:
- Scope:
- Behavior touched:
- Verification:
```

For `CHECKPOINT`, use this compact shape or `assets/checkpoint-template.md`:

```text
UI Invariant Checkpoint
Risk Gate: CHECKPOINT because ...
Preserve:
- ...
Permit:
- ...
Probe:
- ...
Evidence:
- Checked:
- Inspected:
- Not checked:
Post-diff Risk Recheck:
- ...
```

For `LEDGER`, use `assets/ledger-template.md`.

## Language Rules

Use precise, reviewable language:

- "checked with typecheck"
- "inspected in code"
- "not checked in browser"
- "assumed from existing pattern"

Avoid overconfident claims:

- "guaranteed"
- "safe"
- "no regressions"
- "fully verified"
- "everything works"

## Token Discipline

Keep output proportional to risk:

- `MICRO`: max 80 tokens.
- `CHECKPOINT`: max 250 tokens by default.
- `LEDGER`: max 800 tokens by default.

Only exceed these limits when the touched surface is broad enough that omitting detail would hide real risk.
