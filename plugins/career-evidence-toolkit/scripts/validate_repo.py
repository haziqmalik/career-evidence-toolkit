#!/usr/bin/env python3
"""Dependency-free repository validator for Career Evidence Toolkit."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path


EXPECTED_SKILLS = {
    "career-onboarding",
    "master-resume-maintainer",
    "certificate-registry-sync",
    "targeted-resume-generator",
    "ats-professional-resume",
    "executive-technical-resume",
}

BANNED_PRIVATE_PATTERNS = {
    "hard-coded Google document": re.compile(
        r"https://docs\.google\.com/document/d/[A-Za-z0-9_-]{20,}"
    ),
    "hard-coded Google Drive folder": re.compile(
        r"https://drive\.google\.com/drive/folders/[A-Za-z0-9_-]{20,}"
    ),
    "internal generated skill identifier": re.compile(r"skill-[0-9a-f]{20,}"),
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def validate_skill(path: Path, errors: list[str]) -> None:
    manifest = path / "SKILL.md"
    if not manifest.exists():
        fail(errors, f"Missing {manifest}")
        return
    text = manifest.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        fail(errors, f"Invalid frontmatter in {manifest}")
        return
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
    if fields.get("name") != path.name:
        fail(errors, f"Skill name mismatch in {manifest}")
    if not fields.get("description"):
        fail(errors, f"Missing description in {manifest}")
    if "[TODO" in text:
        fail(errors, f"Unfinished placeholder in {manifest}")

    for target in re.findall(r"\[[^]]+\]\(([^)]+\.md)\)", text):
        if not (path / target).exists():
            fail(errors, f"Broken reference {target} in {manifest}")


def validate_docx(path: Path, errors: list[str]) -> None:
    if not zipfile.is_zipfile(path):
        fail(errors, f"Invalid DOCX archive: {path}")
        return
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        forbidden = [
            name
            for name in names
            if name.startswith(("customXml/", "customXML/", "word/comments", "word/people"))
        ]
        if forbidden:
            fail(errors, f"Unsanitized DOCX parts in {path}: {', '.join(forbidden)}")
        visible = b"".join(
            archive.read(name)
            for name in names
            if name.startswith("word/") and name.endswith(".xml")
        ).decode("utf-8", errors="ignore")
        if "{{" not in visible or "}}" not in visible:
            fail(errors, f"Template has no visible placeholders: {path}")
        if re.search(r"<w:(?:ins|del)\b", visible):
            fail(errors, f"Tracked revisions remain in {path}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", nargs="?", default=".", type=Path)
    args = parser.parse_args()
    repo = args.repo.resolve()
    plugin = repo / "plugins" / "career-evidence-toolkit"
    errors: list[str] = []

    for manifest in [plugin / "plugin.json", plugin / ".codex-plugin" / "plugin.json"]:
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
            if data.get("name") != "career-evidence-toolkit":
                fail(errors, f"Unexpected plugin name in {manifest}")
            if not re.fullmatch(r"\d+\.\d+\.\d+", data.get("version", "")):
                fail(errors, f"Invalid semantic version in {manifest}")
        except (OSError, json.JSONDecodeError) as exc:
            fail(errors, f"Cannot read {manifest}: {exc}")

    marketplace = repo / ".agents" / "plugins" / "marketplace.json"
    try:
        json.loads(marketplace.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"Cannot read {marketplace}: {exc}")

    skills_root = plugin / "skills"
    found = {path.name for path in skills_root.iterdir() if path.is_dir()}
    if found != EXPECTED_SKILLS:
        fail(errors, f"Unexpected skills: expected {sorted(EXPECTED_SKILLS)}, found {sorted(found)}")
    for name in EXPECTED_SKILLS:
        validate_skill(skills_root / name, errors)

    for docx in skills_root.glob("*/assets/*.docx"):
        validate_docx(docx, errors)

    text_extensions = {".md", ".yaml", ".yml", ".json", ".py", ".txt"}
    for path in repo.rglob("*"):
        if path.is_file() and path.suffix.lower() in text_extensions:
            content = path.read_text(encoding="utf-8", errors="ignore")
            for label, pattern in BANNED_PRIVATE_PATTERNS.items():
                if pattern.search(content):
                    fail(errors, f"Possible {label} found in {path}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(EXPECTED_SKILLS)} skills, manifests, privacy markers, and DOCX assets.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
