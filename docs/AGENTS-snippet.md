# AGENTS.md Snippet

Use `$ui-invariant-ledger` when modifying existing frontend UI code.

Before editing, classify the task as `MICRO`, `CHECKPOINT`, or `LEDGER`.

If behavior can change, the task is never `MICRO`.

After editing, rerun the Risk Gate against the actual diff and report any escalation, assumptions, and unverified behavior.
