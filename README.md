# UI Invariant Ledger

A markdown-first, evidence-aware Agent Skill that helps AI coding agents preserve observable frontend behavior during UI edits.

## Status

This repository is in v0.1 planning and skeleton setup.

## Core Idea

Before changing an existing UI, the agent should state:

- what must be preserved;
- what is permitted to change;
- what remains uncertain or unverified.

The key rule is simple: if behavior can change, the task is never `MICRO`.

## Repository Layout

```text
skills/ui-invariant-ledger/SKILL.md
skills/ui-invariant-ledger/references/risk-gate.md
skills/ui-invariant-ledger/assets/checkpoint-template.md
skills/ui-invariant-ledger/assets/ledger-template.md
docs/
examples/
```

## Non-Guarantee

UI Invariant Ledger does not promise zero regressions. It makes risk, evidence, assumptions, and review focus visible.
