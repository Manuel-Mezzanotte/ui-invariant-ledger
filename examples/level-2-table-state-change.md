# Level 2: LEDGER Table State Change

## Request

Refactor the orders table toolbar and row layout.

## Surface

The table contains:

- loading state;
- empty state;
- sorting;
- pagination;
- row action buttons;
- selected row count.

## Expected Skill Output

```text
# UI Invariant Ledger

## Risk Gate
- Mode: LEDGER
- Touched concerns: table state, sorting, pagination, empty state, row actions, selected count.
- Escalation reason: table refactors can change data and interaction behavior even when the request sounds visual.

## Surface
- Component/surface: OrdersTable
- Files touched: OrdersTable.tsx

## Requested Change
- Refactor toolbar and row layout.

## Preserve
| Invariant | Evidence | Status |
|---|---|---|
| Loading branch remains visible while data loads | INSPECTED | Branch preserved |
| Empty state remains visible when there are no rows | INSPECTED | Branch preserved |
| Sort state still updates from column headers | INSPECTED | Handler preserved |
| Pagination controls still use current page state | INSPECTED | Props preserved |
| Row action buttons still use type="button" | INSPECTED | Preserved in diff |

## Permit
| Allowed change | Scope |
|---|---|
| Rework toolbar grouping | Table toolbar only |
| Rework row spacing | Row markup only |

## Probe
| Unknown | Why it matters | What was inspected | Blocking |
|---|---|---|---|
| Keyboard access to row actions | Accessibility regression risk | Button markup preserved | No |
| Sort/pagination runtime behavior | Data interaction risk | Handlers and props preserved | No |

## Evidence
- Checked: none.
- Inspected: diff, branches, handlers, pagination props, row action buttons.
- Assumed: existing table tests cover sort/pagination if present.
- Not checked: browser table layout, keyboard row actions, live sorting, pagination.

## Invariant Delta
### Preserved
- Loading, empty state, sorting handler, pagination props, row action button type.

### Intentionally Changed
- Toolbar grouping and row spacing.

### Not Checked
- Keyboard row actions, browser layout, live data interactions.

### At Risk
- Sort/pagination behavior until exercised in browser or tests.

## Reviewer Focus
- Sort by a column and confirm row order changes.
- Move between pages and confirm page state.
- Check empty state with zero rows.
- Trigger row actions and verify they do not submit a surrounding form.
```

## Why This Is LEDGER

Tables combine data state and interaction state. Even visual refactors can break sorting, pagination, empty state, or row actions.
