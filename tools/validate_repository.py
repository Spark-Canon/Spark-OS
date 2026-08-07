#!/usr/bin/env python3
"""Validate Spark OS repository architecture and Spark Brain integrity."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
PLACEHOLDER_PATTERN = re.compile(r"\b(?:TODO|TBD|FIXME)\b|\[PLACEHOLDER\]", re.IGNORECASE)

# brain/manifest.yaml is parsed exclusively via json.loads() below: it must remain
# valid JSON despite its .yaml extension (no comments, anchors, or non-JSON YAML
# syntax). This is the current parsing contract, not a documented architectural
# decision; see brain/health.md for the durable explanation.
MAP_TABLE_ROW_PATTERN = re.compile(r"^\|[^|]*\|\s*\[[^\]]*\]\(([^)]+)\)\s*\|")

# The following slug functions approximate GitHub's heading-anchor algorithm.
# They are proportionate for this repository's current content but do not
# guarantee full fidelity for every Unicode edge case (e.g. combining
# diacritics); see brain/health.md, "Extending Validation".
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*#*$")
INLINE_CODE_PATTERN = re.compile(r"`([^`]*)`")
MD_INLINE_LINK_PATTERN = re.compile(r"\[([^\]]*)\]\([^)]*\)")
EMPHASIS_PATTERN = re.compile(r"(\*\*\*|\*\*|\*|___|__|_)(.+?)\1")
SLUG_STRIP_PATTERN = re.compile(r"[^\w\- ]", re.UNICODE)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_manifest(root: Path, errors: list[str]) -> dict:
    manifest_path = root / "brain" / "manifest.yaml"
    try:
        return json.loads(manifest_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(errors, "Missing brain/manifest.yaml")
    except json.JSONDecodeError as exc:
        fail(errors, f"brain/manifest.yaml is not valid JSON-compatible YAML: {exc}")
    return {}


def validate_required_files(root: Path, manifest: dict, errors: list[str]) -> None:
    for relative in manifest.get("integrity", {}).get("required_files", []):
        if not (root / relative).is_file():
            fail(errors, f"Missing required file: {relative}")


def validate_required_headings(root: Path, manifest: dict, errors: list[str]) -> None:
    requirements = manifest.get("integrity", {}).get("required_headings", {})
    for relative, headings in requirements.items():
        path = root / relative
        if not path.is_file():
            continue
        lines = set(path.read_text(encoding="utf-8").splitlines())
        for heading in headings:
            if heading not in lines:
                fail(errors, f"Missing required heading in {relative}: {heading}")


def validate_authority(root: Path, manifest: dict, errors: list[str]) -> None:
    authority = manifest.get("authority", {})
    seen: dict[Path, str] = {}
    for name, relative in authority.items():
        path = (root / relative).resolve()
        if not path.is_dir():
            fail(errors, f"Authority root does not exist for {name}: {relative}")
        if path in seen:
            fail(errors, f"Duplicate authority root: {name} and {seen[path]} both use {relative}")
        seen[path] = name


def validate_retired_paths(root: Path, manifest: dict, errors: list[str]) -> None:
    for relative in manifest.get("integrity", {}).get("retired_paths", []):
        if (root / relative).exists():
            fail(errors, f"Retired authority path still exists: {relative}")


def validate_boot(root: Path, manifest: dict, errors: list[str]) -> None:
    boot = manifest.get("boot", {})
    for mode, paths in boot.items():
        if len(paths) != len(set(paths)):
            fail(errors, f"Duplicate path in {mode} boot sequence")
        for relative in paths:
            if not (root / relative).exists():
                fail(errors, f"Unresolved {mode} boot path: {relative}")
    quick = boot.get("quick_resume", [])
    full = boot.get("full_architectural", [])
    if quick and quick[0] != "brain/constitution.md":
        fail(errors, "Quick Resume must begin with brain/constitution.md")
    if full and full[0] != "README.md":
        fail(errors, "Full Architectural Boot must begin with README.md")


def normalize_map_target(raw: str) -> str:
    target = raw.strip()
    if target in (".", "./"):
        return "brain"
    if target.startswith("../"):
        target = target[3:]
    return target.rstrip("/")


def parse_repository_map_targets(root: Path, errors: list[str]) -> set[str] | None:
    path = root / "brain" / "repository-map.md"
    if not path.is_file():
        fail(errors, "Missing brain/repository-map.md")
        return None
    targets: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        match = MAP_TABLE_ROW_PATTERN.match(line.strip())
        if not match:
            continue
        targets.add(normalize_map_target(match.group(1)))
    return targets


def validate_map_manifest_consistency(root: Path, manifest: dict, errors: list[str]) -> None:
    map_targets = parse_repository_map_targets(root, errors)
    if map_targets is None:
        return
    manifest_targets = {value.rstrip("/") for value in manifest.get("authority", {}).values()}
    for relative in sorted(manifest_targets - map_targets):
        fail(errors, f"manifest.yaml authority root not declared in repository-map.md: {relative}")
    for relative in sorted(map_targets - manifest_targets):
        fail(errors, f"repository-map.md canonical location not declared in manifest.yaml: {relative}")


def split_link_target(raw_target: str) -> tuple[str, str | None]:
    target = raw_target.strip()
    path_part, _, fragment = target.partition("#")
    path_part = path_part.strip()
    fragment = fragment.strip()
    return path_part, (unquote(fragment) if fragment else None)


def resolve_link_path(source: Path, path_part: str) -> Path | None:
    if not path_part:
        return source
    if path_part.startswith(("http://", "https://", "mailto:")):
        return None
    return (source.parent / unquote(path_part)).resolve()


def heading_to_slug_text(raw: str) -> str:
    text = INLINE_CODE_PATTERN.sub(r"\1", raw)
    text = MD_INLINE_LINK_PATTERN.sub(r"\1", text)
    previous = None
    while previous != text:
        previous = text
        text = EMPHASIS_PATTERN.sub(r"\2", text)
    text = text.strip().lower()
    text = SLUG_STRIP_PATTERN.sub("", text)
    return re.sub(r"\s+", "-", text)


def extract_heading_slugs(text: str) -> set[str]:
    seen: dict[str, int] = {}
    slugs: set[str] = set()
    in_fence = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = HEADING_PATTERN.match(line)
        if not match:
            continue
        base = heading_to_slug_text(match.group(2))
        count = seen.get(base, 0)
        slugs.add(base if count == 0 else f"{base}-{count}")
        seen[base] = count + 1
    return slugs


def validate_markdown_links(root: Path, errors: list[str]) -> None:
    heading_cache: dict[Path, set[str]] = {}
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in LINK_PATTERN.findall(text):
            path_part, fragment = split_link_target(raw_target)
            if not path_part and fragment is None:
                continue
            target = resolve_link_path(path, path_part)
            if target is None:
                continue
            try:
                target.relative_to(root)
            except ValueError:
                fail(errors, f"Relative link escapes repository in {path.relative_to(root)}: {raw_target}")
                continue
            if not target.exists():
                fail(errors, f"Broken link in {path.relative_to(root)}: {raw_target}")
                continue
            if fragment and target.suffix == ".md":
                if target not in heading_cache:
                    heading_cache[target] = extract_heading_slugs(target.read_text(encoding="utf-8"))
                if fragment not in heading_cache[target]:
                    fail(errors, f"Broken anchor in {path.relative_to(root)}: {raw_target}")


def validate_adrs(root: Path, manifest: dict, errors: list[str]) -> None:
    adr_dir = root / manifest.get("authority", {}).get("adr", "")
    pattern = re.compile(manifest.get("integrity", {}).get("adr_pattern", ""))
    numbers: dict[int, str] = {}
    if not adr_dir.is_dir():
        return
    for path in sorted(adr_dir.glob("ADR-*.md")):
        if path.name == "ADR-TEMPLATE.md":
            continue
        match = pattern.match(path.name)
        if not match:
            fail(errors, f"Invalid ADR filename: {path.relative_to(root)}")
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


def excluded(root: Path, path: Path, exclusions: list[str]) -> bool:
    relative = path.relative_to(root).as_posix()
    return any(relative == item or relative.startswith(item.rstrip("/") + "/") for item in exclusions)


def validate_placeholders(root: Path, manifest: dict, errors: list[str]) -> None:
    exclusions = manifest.get("integrity", {}).get("placeholder_exclusions", [])
    for path in root.rglob("*.md"):
        if ".git" in path.parts or excluded(root, path, exclusions):
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if PLACEHOLDER_PATTERN.search(line):
                fail(errors, f"Unresolved placeholder in {path.relative_to(root)}:{line_number}")


def main(root: Path | None = None) -> int:
    root = root or ROOT
    errors: list[str] = []
    manifest = load_manifest(root, errors)
    if manifest:
        validate_required_files(root, manifest, errors)
        validate_required_headings(root, manifest, errors)
        validate_authority(root, manifest, errors)
        validate_retired_paths(root, manifest, errors)
        validate_boot(root, manifest, errors)
        validate_map_manifest_consistency(root, manifest, errors)
        validate_adrs(root, manifest, errors)
        validate_placeholders(root, manifest, errors)
    validate_markdown_links(root, errors)

    if errors:
        print("Repository integrity validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository integrity validation PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
