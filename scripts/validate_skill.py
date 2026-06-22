#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "ui-invariant-ledger"
SKILL_MD = SKILL_DIR / "SKILL.md"
EXPECTED_FILES = [
    SKILL_MD,
    SKILL_DIR / "references" / "risk-gate.md",
    SKILL_DIR / "assets" / "checkpoint-template.md",
    SKILL_DIR / "assets" / "ledger-template.md",
    SKILL_DIR / "agents" / "openai.yaml",
    ROOT / "README.md",
    ROOT / "CHANGELOG.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "docs" / "install.md",
    ROOT / "docs" / "known-limitations.md",
    ROOT / "docs" / "additional-tests.md",
    ROOT / "examples" / "level-0-micro-change.md",
    ROOT / "examples" / "level-1-checkpoint-change.md",
    ROOT / "examples" / "level-1-navigation-responsive-change.md",
    ROOT / "examples" / "level-2-ledger-change.md",
    ROOT / "examples" / "level-2-table-state-change.md",
    ROOT / ".github" / "ISSUE_TEMPLATE" / "bug_report.yml",
    ROOT / ".github" / "ISSUE_TEMPLATE" / "example_request.yml",
    ROOT / ".github" / "workflows" / "ci.yml",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    try:
        _, raw, _ = text.split("---", 2)
    except ValueError:
        fail("SKILL.md frontmatter must be closed")

    data: dict[str, str] = {}
    for line in raw.strip().splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"unsupported frontmatter line: {line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def check_expected_files() -> None:
    for path in EXPECTED_FILES:
        if not path.is_file():
            fail(f"missing expected file: {path.relative_to(ROOT)}")


def check_skill_frontmatter() -> None:
    text = SKILL_MD.read_text(encoding="utf-8")
    data = parse_frontmatter(text)

    if data.get("name") != SKILL_DIR.name:
        fail("frontmatter name must match skill directory")
    if not data.get("description"):
        fail("frontmatter description is required")
    if len(data["description"]) > 1024:
        fail("frontmatter description must be <= 1024 characters")
    if data.get("license") != "MIT":
        fail("frontmatter license must be MIT")
    if len(text.splitlines()) > 500:
        fail("SKILL.md should stay under 500 lines")

    for required in [
        "references/risk-gate.md",
        "assets/checkpoint-template.md",
        "assets/ledger-template.md",
        "if behavior can change, the task is never `MICRO`",
        "CHECKED",
        "INSPECTED",
        "ASSUMED",
        "STALE",
    ]:
        if required not in text:
            fail(f"SKILL.md missing required text: {required}")


def check_no_public_placeholders() -> None:
    for path in [ROOT / "README.md", ROOT / "docs" / "install.md", ROOT / "CHANGELOG.md"]:
        text = path.read_text(encoding="utf-8")
        if "<owner>" in text:
            fail(f"{path.relative_to(ROOT)} still contains <owner>")
        if "Manuel-Mezzanotte/ui-invariant-ledger" not in (text + "\n"):
            if path.name == "install.md":
                fail("docs/install.md must contain the public GitHub repo")


def check_local_markdown_links() -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in link_pattern.findall(text):
            if "://" in target or target.startswith("#") or target.startswith("mailto:"):
                continue
            clean_target = target.split("#", 1)[0]
            if not clean_target:
                continue
            resolved = (path.parent / clean_target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                fail(f"{path.relative_to(ROOT)} has link outside repo: {target}")
            if not resolved.exists():
                fail(f"{path.relative_to(ROOT)} has broken link: {target}")


def check_examples() -> None:
    expected = {
        "level-0-micro-change.md": "Micro-check:",
        "level-1-checkpoint-change.md": "UI Invariant Checkpoint",
        "level-1-navigation-responsive-change.md": "UI Invariant Checkpoint",
        "level-2-ledger-change.md": "# UI Invariant Ledger",
        "level-2-table-state-change.md": "# UI Invariant Ledger",
    }
    for filename, needle in expected.items():
        text = (ROOT / "examples" / filename).read_text(encoding="utf-8")
        if needle not in text:
            fail(f"example {filename} missing expected output marker")
        if "Placeholder" in text:
            fail(f"example {filename} still contains placeholder text")


def main() -> None:
    check_expected_files()
    check_skill_frontmatter()
    check_no_public_placeholders()
    check_local_markdown_links()
    check_examples()
    print("Skill repository validation passed.")


if __name__ == "__main__":
    main()
