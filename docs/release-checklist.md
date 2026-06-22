# Release Checklist

Use this checklist before publishing a public release.

## Preflight

- [ ] Confirm working tree only contains intended changes.
- [ ] Confirm `UI_Invariant_Ledger_Project_Plan.pdf` remains ignored.
- [ ] Run `python3 scripts/validate_skill.py`.
- [ ] Run `gh skill publish --dry-run`.
- [ ] Confirm README release badge and install commands use the target version.
- [ ] Confirm `docs/install.md` uses the target version.
- [ ] Confirm `CHANGELOG.md` has the target version and date.

## Install Tests

- [ ] Test install with Codex.
- [ ] Test install with Claude Code.
- [ ] Test install with OpenCode.
- [ ] Restart or re-open the target agent when needed.
- [ ] Confirm installed metadata points to the target tag.

## Git And GitHub

- [ ] Create the release commit.
- [ ] Push `main`.
- [ ] Publish with `gh skill publish --tag <version>`.
- [ ] Verify the release URL.
- [ ] Verify tag points to the expected commit.
- [ ] Verify GitHub Actions CI passes.

## Hardening Review

- [ ] Main branch protection reviewed.
- [ ] Version tag protection reviewed.
- [ ] Immutable releases reviewed in GitHub settings if available.

If immutable releases are enabled, create the release as a draft first, attach or verify all assets, then publish. After publication, release assets and associated tags may become immutable depending on repository settings.

## Release Notes Template

```md
# UI Invariant Ledger <version>

## Changes

- 

## Validation

- `python3 scripts/validate_skill.py`
- `gh skill publish --dry-run`
- Codex install
- Claude Code install
- OpenCode install

## Known limits

UI Invariant Ledger does not guarantee zero regressions. It makes risk, evidence, assumptions, and reviewer focus visible.
```
