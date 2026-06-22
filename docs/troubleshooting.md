# Troubleshooting

This document covers common misuse patterns when applying UI Invariant Ledger.

## The Agent Uses MICRO Too Often

Check whether the request or diff touches behavior.

`MICRO` is invalid when the edit touches:

- state;
- handlers;
- conditional rendering;
- validation;
- focus or keyboard behavior;
- accessibility attributes;
- data mapping;
- routing;
- responsive behavior;
- public component contracts.

Escalate to `CHECKPOINT` or `LEDGER` when any of these concerns can change observable behavior.

## The Agent Writes Huge Ledgers

Use `CHECKPOINT` unless the task touches stateful, behavioral, data, accessibility, public-contract, or multi-surface concerns.

Long output is a regression when it hides the actual reviewer focus.

For copy-only or cosmetic-only changes, use `MICRO` when behavior cannot change.

## The Agent Says CHECKED But Only Read Code

Downgrade the evidence label to `INSPECTED`.

`CHECKED` requires a real command, test, browser path, viewport check, keyboard check, or concrete runtime verification.

Reading code or a diff is not enough.

## The Agent Puts Everything In Probe

`Probe` must be specific, actionable, and limited.

Weak examples:

```text
Probe: accessibility.
Probe: responsive behavior.
Probe: make sure nothing broke.
```

Better examples:

```text
Probe: 375px mobile menu open/close path and overflow.
Probe: Escape close and focus return after dialog submit error.
Probe: empty-state copy after clearing all table filters.
```

## Browser Verification Is Unavailable

Mark the item as not checked.

Do not claim browser behavior was verified unless a browser path, viewport, or runtime check actually ran.

## The Agent Treats ASSUMED As Preserved Behavior

`ASSUMED` means the agent inferred from nearby patterns.

It does not prove behavior was preserved. Promote it only after a real check, or keep it visible as an assumption for review.

## The Agent Skips Post-Diff Risk Recheck

Run the Risk Gate again after the diff.

If the edit touched new state, handlers, validation, accessibility, data mapping, routing, responsive behavior, or public contracts, escalate the mode before final output.
