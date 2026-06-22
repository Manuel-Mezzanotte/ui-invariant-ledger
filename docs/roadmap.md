# Roadmap

UI Invariant Ledger should evolve from real usage, not theory. Each future version should be justified by examples, failure modes, and reviewer feedback.

## v0.1.0

Status: released locally.

Scope:

- Minimal Agent Skill.
- Risk-scaled modes: `MICRO`, `CHECKPOINT`, `LEDGER`.
- Risk Gate based on touched concerns.
- `Preserve / Permit / Probe`.
- Evidence terms: `CHECKED`, `INSPECTED`, `ASSUMED`, `STALE`.
- Post-diff Risk Recheck.
- Minimal checkpoint and ledger templates.
- Verified examples for each mode.

## v0.2

Goal: improve usability after real task feedback.

Candidate work:

- Add more verified examples only after using the skill on real components.
- Tighten trigger language if agents overuse or underuse `LEDGER`.
- Improve README with clearer before/after examples.
- Add a short troubleshooting section for common misuse:
  - calling risky changes `MICRO`;
  - treating `INSPECTED` as `CHECKED`;
  - writing ledgers that are too long;
  - omitting important `Not checked` behavior.

Exit criteria:

- At least three additional real frontend tasks reviewed.
- At least one example where the skill initially overproduced output and was trimmed.
- At least one example where the skill initially underclassified risk and was corrected.

## v0.3

Goal: add lightweight evaluation notes.

Candidate work:

- Document before/after behavior on real agent edits.
- Add a manual scorecard for:
  - correct mode selection;
  - useful invariant selection;
  - honest evidence language;
  - concise reviewer focus;
  - post-diff escalation quality.
- Collect failure modes and update Risk Gate only when repeated.

Exit criteria:

- Evaluation notes are based on real diffs, not synthetic examples only.
- Scorecard is short enough to be used during review.

## v0.4

Goal: decide whether persistent surface ledgers are worth adding.

Candidate work:

- Explore optional `.ui-invariants/surfaces/*.md` files.
- Define mandatory reconciliation rules for stale evidence.
- Require `STALE` handling before any persistent ledger can influence current claims.

Do not add persistent ledgers if:

- they create stale confidence;
- agents copy old invariants without rechecking;
- maintenance cost exceeds review value.

Exit criteria:

- Persistent ledgers prove useful on repeated edits to the same surfaces.
- Stale evidence reconciliation is clear and enforceable.

## v1.0

Goal: stable public release after broader usage.

Candidate work:

- Confirm install flow across Codex, Claude Code, and OpenCode.
- Stabilize examples and docs.
- Keep the core skill small.
- Document known limits clearly.

Exit criteria:

- Used successfully across multiple real projects or agents.
- Risk Gate has repeated evidence behind it.
- Output remains proportional to risk.

## Non-Goals Until Proven Necessary

- Mandatory scripts.
- Custom CLI.
- Automated detector rules.
- Persistent ledgers by default.
- Claims of complete verification or zero regressions.
