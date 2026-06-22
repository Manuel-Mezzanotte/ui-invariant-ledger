# UI Invariant Ledger

[![CI](https://github.com/Manuel-Mezzanotte/ui-invariant-ledger/actions/workflows/ci.yml/badge.svg)](https://github.com/Manuel-Mezzanotte/ui-invariant-ledger/actions/workflows/ci.yml)

A markdown-first, evidence-aware Agent Skill that helps AI coding agents preserve observable frontend behavior during UI edits.

## Status

Current release: `v0.1.2`.

This is a minimal, installable v0.1 Agent Skill. It intentionally avoids persistent ledgers, detector scripts, and zero-regression claims until real usage shows they are needed.

## Why

AI agents can make frontend changes that look correct on the happy path while silently breaking existing behavior:

- loading, error, empty, pending, disabled, or success states;
- form validation and submit behavior;
- modal focus, Escape, and keyboard behavior;
- inline API errors;
- sorting, pagination, filters, and row actions;
- responsive guards and overflow behavior;
- design-system primitives and accessibility attributes.

UI Invariant Ledger makes the agent state what must be preserved, what may change, what was checked, what was only inspected, and what remains unverified.

## Core Rule

If behavior can change, the task is never `MICRO`.

Risk is determined by touched concerns, not by diff size. A one-line change can be risky when it touches state, handlers, validation, accessibility, data mapping, or public component contracts.

## Install

Install the pinned public release:

```bash
gh skill install Manuel-Mezzanotte/ui-invariant-ledger ui-invariant-ledger@v0.1.2 --agent codex --scope user
```

Other supported agents:

```bash
gh skill install Manuel-Mezzanotte/ui-invariant-ledger ui-invariant-ledger@v0.1.2 --agent claude-code --scope user
gh skill install Manuel-Mezzanotte/ui-invariant-ledger ui-invariant-ledger@v0.1.2 --agent opencode --scope user
```

Restart the target agent after installing.

More install options: [docs/install.md](docs/install.md).

## Use

Invoke explicitly:

```text
Use $ui-invariant-ledger while cleaning up this SettingsModal.
```

The skill is intended for existing frontend UI code, especially:

- forms and validation;
- modals, dialogs, drawers, popovers, and menus;
- tables, filters, sorting, pagination, and empty states;
- loading, error, pending, disabled, and success states;
- data fetching and API mapping;
- navigation and routing;
- accessibility behavior;
- responsive layout and overflow-sensitive surfaces;
- shared design-system primitives.

## Modes

| Mode | Use For | Output |
|---|---|---|
| `MICRO` | Tiny changes that cannot affect observable behavior | Under 80-token micro-check |
| `CHECKPOINT` | Local UI edits where side effects are plausible | Compact `Preserve / Permit / Probe` |
| `LEDGER` | Stateful, data-driven, accessible, public-contract, or multi-surface changes | Ledger with evidence, delta, and reviewer focus |

## Evidence

The skill uses precise evidence labels:

- `CHECKED`: verified with a real command, test, browser path, viewport, keyboard path, or concrete runtime check.
- `INSPECTED`: read in code or diff, without independent verification.
- `ASSUMED`: inferred from surrounding patterns.
- `STALE`: previous evidence not reconfirmed in the current task.

It should not claim "fully verified", "safe", "no regressions", or "everything works".

## Examples

- [MICRO spacing-only change](examples/level-0-micro-change.md)
- [CHECKPOINT local layout cleanup](examples/level-1-checkpoint-change.md)
- [CHECKPOINT mobile navigation responsive change](examples/level-1-navigation-responsive-change.md)
- [LEDGER modal form cleanup](examples/level-2-ledger-change.md)
- [LEDGER table state change](examples/level-2-table-state-change.md)

## Repository Layout

```text
skills/ui-invariant-ledger/SKILL.md
skills/ui-invariant-ledger/references/risk-gate.md
skills/ui-invariant-ledger/assets/checkpoint-template.md
skills/ui-invariant-ledger/assets/ledger-template.md
docs/
examples/
scripts/validate_skill.py
```

## Validate

Run local repository validation:

```bash
python3 scripts/validate_skill.py
```

Run GitHub CLI skill validation:

```bash
gh skill publish --dry-run
```

## Roadmap

See [docs/roadmap.md](docs/roadmap.md).

## Limits

UI Invariant Ledger does not guarantee zero bugs. It makes risk, evidence, assumptions, and reviewer focus visible.

The v0.1 release does not include:

- persistent `.ui-invariants/surfaces/*.md` ledgers;
- detector rules;
- custom CLI;
- mandatory scripts inside the skill package;
- full ledger output for every tiny task.

More detail: [docs/known-limitations.md](docs/known-limitations.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
