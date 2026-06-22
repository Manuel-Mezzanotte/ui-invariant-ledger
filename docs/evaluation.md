# Evaluation Scorecard

Use this scorecard on real frontend tasks. The purpose is to evaluate whether UI Invariant Ledger helps an agent preserve observable behavior without producing unnecessary ceremony.

Score each section from `0` to `3`.

```text
0 = missing or misleading
1 = weak, generic, or incomplete
2 = mostly useful with minor gaps
3 = specific, correct, and proportional
```

## Task Record

```text
Task:
Repository or surface:
Agent host:
Prompt:
Mode selected:
Commands or checks run:
Reviewer:
Date:
```

## 1. Mode Selection

- Did the agent choose the correct `MICRO`, `CHECKPOINT`, or `LEDGER` mode?
- Did it escalate when behavior could change?
- Did it avoid ceremony for cosmetic-only or copy-only edits?

Score: `0-3`

Notes:

```text

```

## 2. Useful Invariants

- Did it identify real behavior to preserve?
- Did it avoid generic invariants?
- Did it include state, interaction, data, layout, accessibility, or public contract concerns when relevant?

Score: `0-3`

Notes:

```text

```

## 3. Evidence Honesty

- Did it distinguish `CHECKED` from `INSPECTED`?
- Did it avoid claims such as "safe", "guaranteed", "no regressions", or "fully verified"?
- Did it mark unverified behavior clearly?

Score: `0-3`

Notes:

```text

```

## 4. Reviewer Focus

- Did it tell the reviewer where to look?
- Were the risks specific?
- Were the unknowns actionable?

Score: `0-3`

Notes:

```text

```

## 5. Output Length

- Was the output proportional to the task?
- Did `MICRO` stay short?
- Did `LEDGER` avoid unnecessary detail?

Score: `0-3`

Notes:

```text

```

## Overall Result

```text
Total score:
Pass / needs follow-up:
Risk Gate change needed:
SKILL.md guidance change needed:
Example worth adding:
```

## Evaluation Rules

- Do not count `INSPECTED` as behavior verification.
- Do not reward long output unless the task risk justifies it.
- Do not change the Risk Gate from one isolated example.
- Do change guidance when the same failure repeats across tasks.
