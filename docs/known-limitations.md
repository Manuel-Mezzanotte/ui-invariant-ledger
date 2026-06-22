# Known Limitations

UI Invariant Ledger is a reviewability skill. It does not guarantee correct frontend behavior.

## What It Cannot Prove

- Browser behavior unless a browser path was actually checked.
- Keyboard behavior unless keyboard paths were actually exercised.
- Focus behavior unless focus entry, trap, and return were actually checked.
- Responsive behavior unless specific viewports were checked.
- API behavior unless success, error, and edge paths were actually run or tested.
- Accessibility behavior beyond what was inspected or checked.

## Evidence Limits

`INSPECTED` means code or diff was read. It does not mean behavior was verified.

`ASSUMED` means the agent inferred from surrounding patterns. It should not be treated as preserved behavior.

`CHECKED` requires a real command, test, browser path, viewport, keyboard path, or concrete runtime check.

## Persistent Ledger Limits

The v0.1 line intentionally does not create persistent `.ui-invariants/surfaces/*.md` files.

Persistent ledgers can become stale. If they are added later, they must include reconciliation rules for `STALE` evidence before influencing current claims.

## Output Limits

Long ledgers can hide the important review points. The skill should list only invariants plausibly affected by the request or diff.

## Security Limits

The skill is not a security scanner. It can flag high-risk UI surfaces such as auth, payments, destructive actions, permissions, and user data, but it does not replace security review.
