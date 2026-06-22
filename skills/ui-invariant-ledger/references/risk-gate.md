# Risk Gate

Risk is determined by touched concerns, not by diff size.

If behavior can change, the task is never `MICRO`.

`MICRO` is forbidden if the change touches:

- conditional rendering
- state hooks or stores
- event handlers
- form validation
- loading, error, empty, disabled, success, or pending states
- data fetching or API mapping
- routing or navigation
- focus, keyboard, ARIA, labels, roles, or semantic elements
- responsive containers, overflow, sticky or fixed layout
- component props used outside the edited file
- design-system primitives
- auth, permissions, payments, destructive actions, or user data

After editing, rerun the gate against the actual diff.

Escalate from `MICRO` to `CHECKPOINT` when the actual diff touches a behavior-related concern.

Escalate to `LEDGER` when the actual diff touches stateful behavior, data flow, accessibility behavior, public component contracts, or multiple UI surfaces.
