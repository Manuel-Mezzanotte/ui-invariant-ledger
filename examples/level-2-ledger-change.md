# Level 2: LEDGER Change

## Request

Clean up the layout of `SettingsModal`.

## Surface

The modal contains:

- dialog primitive behavior;
- submit pending state;
- inline API error rendering;
- input error association via `aria-describedby`;
- cancel button behavior;
- mobile width guard.

## Risk Gate

Mode: `LEDGER`

Touched concerns: form state, pending state, API error rendering, accessibility association, dialog behavior, and responsive layout.

Escalation reason: a visual cleanup of a modal form can change behavior even when the request does not mention behavior.

## Expected Skill Output

```text
# UI Invariant Ledger

## Risk Gate
- Mode: LEDGER
- Touched concerns: modal form, pending state, API error rendering, accessibility association, responsive guard.
- Escalation reason: behavior can change during a visual cleanup of a stateful modal.

## Surface
- Component/surface: SettingsModal
- Files touched: SettingsModal.tsx

## Requested Change
- Clean up modal layout.

## Preserve
| Invariant | Evidence | Status |
|---|---|---|
| Dialog primitive remains used | INSPECTED | Preserved in diff |
| Submit remains disabled while saving | INSPECTED | Preserved in diff |
| API error remains inline with role="alert" | INSPECTED | Preserved in diff |
| Input remains associated with the error via aria-describedby | INSPECTED | Preserved in diff |
| Cancel remains type="button" and disabled while saving | INSPECTED | Preserved in diff |

## Permit
| Allowed change | Scope |
|---|---|
| Rework spacing and grouping | Modal body only |

## Probe
| Unknown | Why it matters | What was inspected | Blocking |
|---|---|---|---|
| Focus return and Escape behavior | Dialog accessibility regression risk | Dialog primitive remains used | No |
| Mobile viewport behavior | Overflow risk | Width guard remains present | No |

## Evidence
- Checked: none.
- Inspected: diff and preserved branches/attributes.
- Assumed: Dialog primitive keeps existing keyboard behavior.
- Not checked: browser rendering, focus return, Escape, mobile viewport, real API error path.

## Invariant Delta
### Preserved
- Dialog primitive, pending disabled state, inline error, aria-describedby, cancel button type.

### Intentionally Changed
- Visual grouping and spacing.

### Not Checked
- Focus return, Escape, mobile viewport, real API error path.

### At Risk
- Keyboard/focus behavior until checked in browser.

## Post-diff Risk Recheck
- Initial mode: LEDGER
- Actual touched concerns: layout around modal form state and accessibility attributes
- Final mode: LEDGER
- Reason: stateful modal concerns remained in scope.

## Reviewer Focus
- Check save disabled state while pending.
- Trigger an API error and confirm inline alert.
- Test Escape/focus behavior in browser.
- Check mobile width under 430px.
```

## Static Comparison

Naive refactor:

```text
FAIL dialog primitive preserved
FAIL submit disabled while saving
FAIL inline API error alert preserved
FAIL input error association preserved
FAIL cancel does not submit and is disabled while saving
FAIL mobile width guard preserved
```

Skill-guided refactor:

```text
PASS dialog primitive preserved
PASS submit disabled while saving
PASS inline API error alert preserved
PASS input error association preserved
PASS cancel does not submit and is disabled while saving
PASS mobile width guard preserved
```

## Why This Is LEDGER

The edited surface is a stateful modal form. Even a layout-only cleanup can accidentally remove error handling, disabled states, accessibility wiring, dialog behavior, or responsive guards. The ledger makes those invariants visible and gives the reviewer concrete checks.
