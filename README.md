# UI Invariant Ledger

A markdown-first, evidence-aware Agent Skill that helps AI coding agents preserve observable frontend behavior during UI edits.

## Status

Current release: `v0.1.0`.

This is a minimal, installable v0.1 Agent Skill. It intentionally avoids persistent ledgers, detector scripts, and zero-regression claims until real usage shows they are needed.

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

## Examples

- [MICRO spacing-only change](examples/level-0-micro-change.md)
- [CHECKPOINT local layout cleanup](examples/level-1-checkpoint-change.md)
- [LEDGER modal form cleanup](examples/level-2-ledger-change.md)

## Install

See [docs/install.md](docs/install.md).

## Roadmap

See [docs/roadmap.md](docs/roadmap.md).

## Non-Guarantee

UI Invariant Ledger does not promise zero regressions. It makes risk, evidence, assumptions, and review focus visible.
