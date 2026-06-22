# Phase 6 Test

## Goal

Test UI Invariant Ledger on a realistic frontend task before publishing examples.

Scenario: refactor a `SettingsModal` to make the layout cleaner.

The component included:

- a dialog primitive;
- submit pending state;
- inline API error rendering;
- input `aria-describedby` linked to the error;
- cancel button that must not submit the form;
- mobile width guard.

## Risk Classification

Mode: `LEDGER`

Reason: the surface is a modal form touching form state, pending state, API error rendering, accessibility associations, dialog behavior, and responsive layout.

## Preserve

| Invariant | Evidence | Result |
|---|---|---|
| Dialog primitive remains used | INSPECTED | Preserved in skill-guided diff |
| Submit remains disabled while saving | INSPECTED | Preserved in skill-guided diff |
| API error remains inline with `role="alert"` | INSPECTED | Preserved in skill-guided diff |
| Input remains associated with error via `aria-describedby` | INSPECTED | Preserved in skill-guided diff |
| Cancel remains `type="button"` and disabled while saving | INSPECTED | Preserved in skill-guided diff |
| Mobile width guard remains present | INSPECTED | Preserved in skill-guided diff |

## Comparison

Static checks against a naive refactor:

```text
[naive-after]
FAIL dialog primitive preserved
FAIL submit disabled while saving
FAIL inline API error alert preserved
FAIL input error association preserved
FAIL cancel does not submit and is disabled while saving
FAIL mobile width guard preserved
```

Static checks against a skill-guided refactor:

```text
[skill-after]
PASS dialog primitive preserved
PASS submit disabled while saving
PASS inline API error alert preserved
PASS input error association preserved
PASS cancel does not submit and is disabled while saving
PASS mobile width guard preserved
```

## What The Skill Improved

Without the skill, the cleanup task can look visually plausible while silently removing behavior: dialog primitive behavior, API error handling, accessibility linkage, pending disabled state, cancel button type, and responsive guard.

With the skill, the same task is correctly escalated to `LEDGER`, forcing the edit to preserve behavior and giving the reviewer a short list of verification paths.

## Not Checked

- Browser rendering.
- Keyboard behavior.
- Focus return behavior.
- Real API error path.
- Mobile viewport runtime behavior.

## Outcome

Phase 6 passes as a first controlled test. The skill correctly identifies this as `LEDGER`, exposes the important invariants, and produces a useful reviewer focus without requiring a persistent ledger.
