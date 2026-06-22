# Roadmap

UI Invariant Ledger should evolve from real usage, not theory. Each future version must be justified by examples, failure modes, and reviewer feedback.

## Current Release

Current public release: `v0.1.6`.

The v0.1 line is installable and public. It includes the minimal Agent Skill, public README, examples, CI validation, issue templates, contribution guide, known limitations, and public install verification.

## v0.2.x - Real-World Validation

Goal: prove the skill on real frontend tasks.

Required task categories:

- Form validation.
- Modal or dialog refactor.
- Table with sorting, filtering, pagination, or row actions.
- Navigation or mobile menu.
- Responsive layout.
- Accessibility, focus, or keyboard behavior.
- API loading, error, empty, pending, disabled, or success states.
- Design-system primitive change.

For each task, document:

- prompt used;
- agent host used: Codex, Claude Code, OpenCode, or another host;
- selected mode: `MICRO`, `CHECKPOINT`, or `LEDGER`;
- output produced;
- problems found;
- changes needed in the skill.

Exit criteria:

- At least eight documented real frontend tasks.
- At least one task per required category.
- Install flow still verified on Codex, Claude Code, and OpenCode.

## v0.3.x - Risk Gate Stabilization

Goal: make mode selection neither too weak nor too ceremonial.

Fix underclassification:

- `MICRO` used after touching handlers, state, conditional rendering, validation, accessibility, routing, data mapping, or responsive behavior.
- `CHECKPOINT` used where `LEDGER` is required by stateful, data-driven, accessible, public-contract, or multi-surface risk.

Fix overclassification:

- `LEDGER` used for copy-only or cosmetic-only changes.
- Long output produced where a short `MICRO` or compact `CHECKPOINT` would be more useful.

Exit criteria:

- Repeated underclassification cases are reflected in `risk-gate.md`.
- Repeated overclassification cases are reflected in `SKILL.md` output guidance.
- `MICRO`, `CHECKPOINT`, and `LEDGER` boundaries are supported by examples.

## v0.4.x - Evaluation Docs

Goal: make usefulness measurable.

Candidate work:

- Maintain [docs/evaluation.md](evaluation.md).
- Add before/after task notes from real edits.
- Use the scorecard for:
  - mode selection;
  - useful invariants;
  - evidence honesty;
  - reviewer focus;
  - output length.

Exit criteria:

- Evaluation notes are based on real diffs, not synthetic examples only.
- The scorecard is short enough to use during review.
- Failure modes are collected before changing the Risk Gate.

## v0.5.x - Troubleshooting And Misuse Prevention

Goal: help users correct bad outputs quickly.

Candidate work:

- Maintain [docs/troubleshooting.md](troubleshooting.md).
- Add concrete examples for:
  - `MICRO` misuse;
  - `CHECKED` versus `INSPECTED`;
  - oversized ledgers;
  - vague `Probe` entries;
  - unavailable browser verification.

Exit criteria:

- Troubleshooting covers repeated misuse from real tasks.
- The guidance reinforces proportional output instead of adding ceremony.

## v0.6.x - Public Hardening

Goal: prepare the repository for a stable public release.

Candidate work:

- Maintain [SECURITY.md](../SECURITY.md).
- Maintain [docs/release-checklist.md](release-checklist.md).
- Keep `CODEOWNERS` current.
- Document branch protection, version tag protection, and immutable release notes.
- Keep install docs resilient if `gh skill` behavior changes.

Exit criteria:

- Release checklist is usable without extra context.
- Security policy is visible from the repository root.
- GitHub branch/tag/release hardening has been reviewed manually.

## v0.9.0 - Release Candidate

Goal: final public trial before stable.

Required before release:

- At least eight documented real frontend tasks.
- [docs/evaluation.md](evaluation.md) present and used.
- [docs/troubleshooting.md](troubleshooting.md) present.
- [SECURITY.md](../SECURITY.md) present.
- [docs/release-checklist.md](release-checklist.md) present.
- Persistent ledgers declared out of v1.0.0 scope.
- Install tests pass on Codex, Claude Code, and OpenCode.
- `python3 scripts/validate_skill.py` passes.
- `gh skill publish --dry-run` passes.

## v1.0.0 - Stable Release

Goal: stable task-scoped invariant checkpoints.

v1.0.0 means the scope is stable, not that frontend behavior is guaranteed.

Stable scope:

- Risk-scaled `MICRO`, `CHECKPOINT`, and `LEDGER` modes.
- Risk Gate based on touched frontend concerns.
- `Preserve / Permit / Probe`.
- `CHECKED`, `INSPECTED`, `ASSUMED`, and `STALE` evidence language.
- Post-diff Risk Recheck.
- Task-scoped output only.

Exit criteria:

- Used successfully across multiple real frontend projects or agent hosts.
- Risk Gate has repeated evidence behind it.
- Output remains proportional to risk.
- Users can understand what the skill does not guarantee.

## Non-Goals Until Proven Necessary

- Mandatory scripts inside the skill package.
- Custom CLI.
- Automated detector rules.
- Persistent ledgers by default.
- Claims of complete verification or zero regressions.
