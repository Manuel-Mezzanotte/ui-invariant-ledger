# Additional Tests

These tests extend the original Phase 6 modal form test with two more frontend surfaces.

## Test A: Mobile Navigation Spacing

Scenario: tighten spacing in `MobileNav`.

Expected mode: `CHECKPOINT`.

Preserved invariants:

- closed branch remains present;
- close button remains `type="button"`;
- close button still calls `onClose`;
- `nav` keeps `aria-label="Mobile navigation"`;
- link mapping still uses `link.href` and `link.label`.

Not checked:

- 390px viewport rendering;
- keyboard path;
- browser overflow behavior.

Result: documented in [level-1-navigation-responsive-change.md](../examples/level-1-navigation-responsive-change.md).

## Test B: Orders Table Refactor

Scenario: refactor orders table toolbar and row layout.

Expected mode: `LEDGER`.

Preserved invariants:

- loading state;
- empty state;
- sorting handler;
- pagination props;
- row action button type.

Not checked:

- live sorting;
- live pagination;
- keyboard row actions;
- browser table layout.

Result: documented in [level-2-table-state-change.md](../examples/level-2-table-state-change.md).

## Test Conclusion

The added examples broaden coverage beyond modal forms:

- `CHECKPOINT` for responsive navigation layout;
- `LEDGER` for table state and data interactions.

Both reinforce the core rule: risk follows touched concerns, not diff size or visual wording.
