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

If `gh` is not available, install manually for Codex:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/ui-invariant-ledger "${CODEX_HOME:-$HOME/.codex}/skills/ui-invariant-ledger"
```

Restart Codex after installing so the new skill is picked up.

## Public Install

After a public release is tagged, install from GitHub:

```bash
gh skill install Manuel-Mezzanotte/ui-invariant-ledger ui-invariant-ledger@v0.1.4 --agent codex --scope user
gh skill install Manuel-Mezzanotte/ui-invariant-ledger ui-invariant-ledger@v0.1.4 --agent claude-code --scope user
gh skill install Manuel-Mezzanotte/ui-invariant-ledger ui-invariant-ledger@v0.1.4 --agent opencode --scope user
```

Prefer a tagged release such as `v0.1.4` for stable public installation.
