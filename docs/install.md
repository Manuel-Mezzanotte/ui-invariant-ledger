# Install

## Local Development

From the parent directory of this repository:

```bash
gh skill install ./ui-invariant-ledger ui-invariant-ledger --from-local --agent codex --scope project
```

From the repository root:

```bash
gh skill install . ui-invariant-ledger --from-local --agent codex --scope project
```

## Public Install

After a public release is tagged, install from GitHub:

```bash
gh skill install <owner>/ui-invariant-ledger ui-invariant-ledger --agent codex --scope user
gh skill install <owner>/ui-invariant-ledger ui-invariant-ledger --agent claude-code --scope user
gh skill install <owner>/ui-invariant-ledger ui-invariant-ledger --agent opencode --scope user
```

Prefer a tagged release such as `v0.1.0` for stable public installation.
