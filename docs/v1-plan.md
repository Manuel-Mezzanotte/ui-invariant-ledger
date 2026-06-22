# v1.0.0 Plan

UI Invariant Ledger should reach v1.0.0 only when the current task-scoped model is proven on real frontend edits.

The goal is not to add more theory. The goal is to prove that the existing workflow is useful, honest, and proportional.

## Version Path

```text
v0.2.x -> real-world validation
v0.3.x -> Risk Gate stabilization
v0.4.x -> evaluation docs
v0.5.x -> troubleshooting and misuse prevention
v0.6.x -> public hardening
v0.9.0 -> release candidate
v1.0.0 -> stable release
```

## Required v1 Principle

No `v1.0.0` without at least eight documented real frontend tasks.

Documentation quality is not enough. The skill must show that agents classify risk correctly and produce useful, proportional output on real UI work.

## Real-World Validation Tasks

At minimum, v1 validation must cover:

1. Form validation.
2. Modal or dialog refactor.
3. Table with sorting, filtering, pagination, or row actions.
4. Navigation or mobile menu.
5. Responsive layout.
6. Accessibility, focus, or keyboard behavior.
7. API loading, error, empty, pending, disabled, or success states.
8. Design-system primitive change.

For every task, record:

- prompt used;
- agent host used;
- selected mode;
- output produced;
- problems found;
- skill changes needed.

## Risk Gate Stabilization

The Risk Gate must be tuned against two failure modes.

### Underclassification

Underclassification happens when the agent chooses a lower-risk mode even though behavior can change.

Examples:

- `MICRO` after touching `onClick`;
- `MICRO` after changing conditional rendering;
- `MICRO` after changing disabled state;
- `CHECKPOINT` when a modal form touches validation, focus, and API errors.

Repeated underclassification should harden `risk-gate.md`.

### Overclassification

Overclassification happens when the agent produces more ceremony than the task needs.

Examples:

- `LEDGER` for copy-only text edits;
- `LEDGER` for spacing-only class changes;
- long invariant output for a cosmetic-only diff.

Repeated overclassification should tighten `SKILL.md` output guidance.

## Evaluation

Use [docs/evaluation.md](evaluation.md) to score real tasks.

The scorecard should answer whether the agent:

- selected the right mode;
- named useful invariants;
- used evidence labels honestly;
- gave specific reviewer focus;
- kept output proportional to risk.

## Troubleshooting

Use [docs/troubleshooting.md](troubleshooting.md) to capture repeated misuse.

Troubleshooting should stay practical and concrete. It should correct common failures without expanding the core skill.

## Public Hardening

Before `v1.0.0`, the repository should have:

- [SECURITY.md](../SECURITY.md);
- [docs/release-checklist.md](release-checklist.md);
- branch protection reviewed manually;
- version tag protection reviewed manually;
- immutable release setting reviewed manually if available;
- install tests on Codex, Claude Code, and OpenCode.

## Persistent Ledgers Decision

Persistent ledgers are out of v1.0.0 scope.

UI Invariant Ledger v1 is task-scoped. It does not maintain persistent `.ui-invariants/surfaces/*.md` files because stale records can create false confidence.

Persistent ledgers may be explored later only with mandatory reconciliation and `STALE` evidence rules.

## v1.0.0 Release Standard

`v1.0.0` can ship when:

- at least eight real frontend tasks are documented;
- underclassification and overclassification failures have been reviewed;
- Risk Gate changes are evidence-backed;
- docs and examples are stable;
- known limitations are explicit;
- install verification passes for Codex, Claude Code, and OpenCode;
- CI passes;
- `gh skill publish --dry-run` passes.
