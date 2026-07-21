#!/usr/bin/env python3
"""Validate Spark OS repository architecture and Spark Brain integrity."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "brain" / "manifest.yaml"
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
PLACEHOLDER_PATTERN = re.compile(r"\b(?:TODO|TBD|FIXME)\b|\[PLACEHOLDER\]", re.IGNORECASE)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_manifest(errors: list[str]) -> dict:
    try:
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(errors, "Missing brain/manifest.yaml")
    except json.JSONDecodeError as exc:
        fail(errors, f"brain/manifest.yaml is not valid JSON-compatible YAML: {exc}")
    return {}


def validate_required_files(manifest: dict, errors: list[str]) -> None:
    for relative in manifest.get("integrity", {}).get("required_files", []):
        if not (ROOT / relative).is_file():
            fail(errors, f"Missing required file: {relative}")


def validate_required_headings(manifest: dict, errors: list[str]) -> None:
    requirements = manifest.get("integrity", {}).get("required_headings", {})
    for relative, headings in requirements.items():
        path = ROOT / relative
        if not path.is_file():
            continue
        lines = set(path.read_text(encoding="utf-8").splitlines())
        for heading in headings:
            if heading not in lines:
                fail(errors, f"Missing required heading in {relative}: {heading}")


def validate_authority(manifest: dict, errors: list[str]) -> None:
    authority = manifest.get("authority", {})
    seen: dict[Path, str] = {}
    for name, relative in authority.items():
        path = (ROOT / relative).resolve()
        if not path.is_dir():
            fail(errors, f"Authority root does not exist for {name}: {relative}")
        if path in seen:
            fail(errors, f"Duplicate authority root: {name} and {seen[path]} both use {relative}")
        seen[path] = name


def validate_retired_paths(manifest: dict, errors: list[str]) -> None:
    for relative in manifest.get("integrity", {}).get("retired_paths", []):
        if (ROOT / relative).exists():
            fail(errors, f"Retired authority path still exists: {relative}")


def validate_boot(manifest: dict, errors: list[str]) -> None:
    boot = manifest.get("boot", {})
    for mode, paths in boot.items():
        if len(paths) != len(set(paths)):
            fail(errors, f"Duplicate path in {mode} boot sequence")
        for relative in paths:
            if not (ROOT / relative).exists():
                fail(errors, f"Unresolved {mode} boot path: {relative}")
    quick = boot.get("quick_resume", [])
    full = boot.get("full_architectural", [])
    if quick and quick[0] != "brain/constitution.md":
        fail(errors, "Quick Resume must begin with brain/constitution.md")
    if full and full[0] != "README.md":
        fail(errors, "Full Architectural Boot must begin with README.md")


def normalized_link_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().split("#", 1)[0].strip()
    if not target or target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    target = unquote(target)
    return (source.parent / target).resolve()


def validate_markdown_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in LINK_PATTERN.findall(text):
            target = normalized_link_target(path, raw_target)
            if target is None:
                continue
            try:
                target.relative_to(ROOT)
            except ValueError:
                fail(errors, f"Relative link escapes repository in {path.relative_to(ROOT)}: {raw_target}")
                continue
            if not target.exists():
                fail(errors, f"Broken link in {path.relative_to(ROOT)}: {raw_target}")


def validate_adrs(manifest: dict, errors: list[str]) -> None:
    adr_dir = ROOT / manifest.get("authority", {}).get("adr", "")
    pattern = re.compile(manifest.get("integrity", {}).get("adr_pattern", ""))
    numbers: dict[int, str] = {}
    if not adr_dir.is_dir():
        return
    for path in sorted(adr_dir.glob("ADR-*.md")):
        if path.name == "ADR-TEMPLATE.md":
            continue
        match = pattern.match(path.name)
        if not match:
            fail(errors, f"Invalid ADR filename: {path.relative_to(ROOT)}")
            continue
        number = int(match.group(1))
        if number in numbers:
            fail(errors, f"Duplicate ADR number {number:04d}: {numbers[number]} and {path.name}")
        numbers[number] = path.name
    if numbers:
        expected = set(range(min(numbers), max(numbers) + 1))
        missing = sorted(expected - set(numbers))
        if missing:
            fail(errors, "ADR numbering gap: " + ", ".join(f"{number:04d}" for number in missing))


def excluded(path: Path, exclusions: list[str]) -> bool:
    relative = path.relative_to(ROOT).as_posix()
    return any(relative == item or relative.startswith(item.rstrip("/") + "/") for item in exclusions)


def validate_placeholders(manifest: dict, errors: list[str]) -> None:
    exclusions = manifest.get("integrity", {}).get("placeholder_exclusions", [])
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or excluded(path, exclusions):
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if PLACEHOLDER_PATTERN.search(line):
                fail(errors, f"Unresolved placeholder in {path.relative_to(ROOT)}:{line_number}")


def main() -> int:
    errors: list[str] = []
    manifest = load_manifest(errors)
    if manifest:
        validate_required_files(manifest, errors)
        validate_required_headings(manifest, errors)
        validate_authority(manifest, errors)
        validate_retired_paths(manifest, errors)
        validate_boot(manifest, errors)
        validate_adrs(manifest, errors)
        validate_placeholders(manifest, errors)
    validate_markdown_links(errors)

    if errors:
        print("Repository integrity validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository integrity validation PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
