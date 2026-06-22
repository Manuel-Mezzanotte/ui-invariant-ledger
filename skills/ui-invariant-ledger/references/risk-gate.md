# Risk Gate

Risk is determined by touched concerns, not by diff size.

If behavior can change, the task is never `MICRO`.

Run this gate twice:

1. Before editing, based on the requested change and affected surface.
2. After editing, based on the actual diff.

## Mode Decision

Use the lowest mode that honestly covers the touched concerns.

- `MICRO`: only for edits that cannot change observable behavior.
- `CHECKPOINT`: for local UI edits where behavior is nearby or side effects are plausible.
- `LEDGER`: for stateful, data-driven, accessible, public-contract, multi-surface, or high-impact behavior.

If unsure between two modes, choose the higher-risk mode.

Visual wording does not lower risk. A request to "clean up", "simplify", "polish", or "refactor" a surface still follows the touched concerns below.

## MICRO Is Forbidden When Touching

- conditional rendering
- state hooks, stores, reducers, or local business logic
- event handlers
- form validation
- loading, error, empty, disabled, success, or pending states
- data fetching or API mapping
- routing or navigation
- focus, keyboard, ARIA, labels, roles, or semantic elements
- responsive containers, overflow, sticky layout, or fixed layout
- component props used outside the edited file
- design-system primitives
- auth, permissions, payments, destructive actions, or user data

Do not classify a task as `MICRO` just because the diff is small, the request sounds visual, or the user did not mention behavior.

## CHECKPOINT Triggers

Use `CHECKPOINT` when the edit is local but could affect nearby behavior.

Examples:

- layout changes around loading, error, or empty branches;
- markup extraction that should keep conditions and handlers stable;
- responsive container or overflow changes;
- design-system class or primitive changes with possible behavior or accessibility side effects;
- visual changes on interactive elements when handlers stay unchanged.
- visual cleanup of static markup around a stateful branch when the stateful branch is preserved but not edited.

## LEDGER Triggers

Use `LEDGER` when the change can affect core behavior or reviewer verification paths.

Examples:

- form state, submit behavior, validation, disabled logic, or pending state;
- modal, dialog, drawer, popover, menu, tooltip, focus, Escape, keyboard, ARIA, labels, roles, or semantic behavior;
- tables, filters, sorting, pagination, row selection, row actions, or empty states;
- data fetching, API mapping, error rendering, optimistic UI, cache invalidation, or permissions;
- routing, navigation, auth, payments, destructive actions, or user data;
- public component props, shared primitives, or multiple UI surfaces.
- visual cleanup of a modal, form, table, or navigation surface when the component contains pending state, error rendering, validation, focus behavior, keyboard behavior, responsive guards, or public props.

## Post-Diff Recheck

Inspect the actual diff after editing.

Report:

- initial mode;
- actual touched concerns;
- final mode;
- reason for any escalation.

If a `MICRO` diff touched any forbidden concern, escalate at least to `CHECKPOINT`.

If a `CHECKPOINT` diff touched stateful behavior, data flow, accessibility behavior, public contracts, user data, or multiple surfaces, escalate to `LEDGER`.

## Anti-Gaming Rules

- Do not call a change visual-only when it touches conditions, handlers, state, semantics, focus, keyboard behavior, API data, or public props.
- Do not treat `INSPECTED` code as `CHECKED` behavior.
- Do not omit unknowns to keep the mode lower.
- Do not downgrade risk because tests passed if relevant behavior was not covered by those tests.
- Do not hide skipped browser, keyboard, viewport, or error-path checks.
- Do not produce a long ledger to appear careful; list only invariants plausibly affected by the request or diff.
