# Post-Restart Test

Date: 2026-06-22

## Goal

Verify that `ui-invariant-ledger` is discoverable and usable after restarting Codex.

## Checks

### Codex Skill List

Command:

```bash
gh skill list --agent codex --scope user
```

Observed result:

```text
ui-invariant-ledger  codex  user  Manuel-Mezzanotte/ui-invariant-ledger
```

### Installed Skill Validation

Command:

```bash
python3 /Users/manuelmezzanotte/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  /Users/manuelmezzanotte/.codex/skills/ui-invariant-ledger
```

Observed result:

```text
Skill is valid!
```

### Installed Source Metadata

The installed `SKILL.md` contains GitHub source metadata:

```yaml
metadata:
  github-ref: refs/tags/v0.1.0
  github-repo: https://github.com/Manuel-Mezzanotte/ui-invariant-ledger
```

### Public Preview

Command:

```bash
gh skill preview Manuel-Mezzanotte/ui-invariant-ledger ui-invariant-ledger@v0.1.0
```

Observed result: the command resolved the remote skill, showed the expected file tree, and rendered `SKILL.md`.

### Publish Dry Run

Command:

```bash
gh skill publish --dry-run
```

Observed result:

```text
Dry run complete. Use without --dry-run to publish.
```

## Functional Smoke Test

Prompt shape tested against the installed skill:

```text
Use $ui-invariant-ledger for a SettingsModal visual cleanup that touches a modal form with pending state, inline API errors, aria-describedby, cancel button behavior, and mobile width guard.
```

Expected behavior:

- classify as `LEDGER`;
- preserve submit disabled while saving;
- preserve inline API error with `role="alert"`;
- preserve `aria-describedby`;
- preserve cancel `type="button"`;
- preserve dialog primitive and responsive guard;
- mark browser, keyboard, focus, API, and mobile runtime checks as not checked unless actually run.

Result: matches the Phase 6 LEDGER test expectations.
