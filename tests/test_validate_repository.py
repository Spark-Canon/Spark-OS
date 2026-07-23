"""Dependency-free tests for tools/validate_repository.py.

Run with: python -m unittest discover -s tests
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

import validate_repository as vr  # noqa: E402


def write(root: Path, relative: str, content: str = "") -> Path:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def base_manifest(**overrides) -> dict:
    manifest = {
        "authority": {
            "philosophy": "01-philosophy",
            "governance": "02-governance",
            "adr": "02-governance/architecture-decisions",
            "brain": "brain",
        },
        "boot": {
            "quick_resume": ["brain/constitution.md"],
            "full_architectural": ["README.md"],
        },
        "integrity": {
            "required_files": [],
            "required_headings": {},
            "retired_paths": [],
            "adr_pattern": r"^ADR-(\d{4})-[a-z0-9-]+\.md$",
            "placeholder_exclusions": [],
        },
    }
    manifest.update(overrides)
    return manifest


class ValidatorFixtureTest(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        for area in ("01-philosophy", "02-governance/architecture-decisions", "brain"):
            (self.root / area).mkdir(parents=True, exist_ok=True)
        write(self.root, "brain/constitution.md", "# Constitution\n")
        write(self.root, "README.md", "# Root\n")

    # --- required files -----------------------------------------------

    def test_missing_required_file_fails(self) -> None:
        manifest = base_manifest(integrity={**base_manifest()["integrity"], "required_files": ["CONTRIBUTING.md"]})
        errors: list[str] = []
        vr.validate_required_files(self.root, manifest, errors)
        self.assertTrue(any("Missing required file: CONTRIBUTING.md" in e for e in errors))

    def test_present_required_file_passes(self) -> None:
        write(self.root, "CONTRIBUTING.md", "# Contributing\n")
        manifest = base_manifest(integrity={**base_manifest()["integrity"], "required_files": ["CONTRIBUTING.md"]})
        errors: list[str] = []
        vr.validate_required_files(self.root, manifest, errors)
        self.assertEqual(errors, [])

    # --- required (protected) headings ---------------------------------

    def test_missing_required_heading_fails(self) -> None:
        manifest = base_manifest(
            integrity={**base_manifest()["integrity"], "required_headings": {"brain/constitution.md": ["## Purpose"]}}
        )
        errors: list[str] = []
        vr.validate_required_headings(self.root, manifest, errors)
        self.assertTrue(any("Missing required heading in brain/constitution.md: ## Purpose" in e for e in errors))

    def test_present_required_heading_passes(self) -> None:
        write(self.root, "brain/constitution.md", "# Constitution\n\n## Purpose\n")
        manifest = base_manifest(
            integrity={**base_manifest()["integrity"], "required_headings": {"brain/constitution.md": ["## Purpose"]}}
        )
        errors: list[str] = []
        vr.validate_required_headings(self.root, manifest, errors)
        self.assertEqual(errors, [])

    # --- duplicate / missing authority roots ----------------------------

    def test_duplicate_authority_root_fails(self) -> None:
        manifest = base_manifest(authority={"philosophy": "01-philosophy", "duplicate": "01-philosophy"})
        errors: list[str] = []
        vr.validate_authority(self.root, manifest, errors)
        self.assertTrue(any("Duplicate authority root" in e for e in errors))

    def test_missing_authority_root_fails(self) -> None:
        manifest = base_manifest(authority={"canon": "03-canon"})
        errors: list[str] = []
        vr.validate_authority(self.root, manifest, errors)
        self.assertTrue(any("Authority root does not exist for canon: 03-canon" in e for e in errors))

    # --- retired paths ---------------------------------------------------

    def test_retired_path_still_present_fails(self) -> None:
        write(self.root, "meta/README.md", "retired\n")
        manifest = base_manifest(integrity={**base_manifest()["integrity"], "retired_paths": ["meta"]})
        errors: list[str] = []
        vr.validate_retired_paths(self.root, manifest, errors)
        self.assertTrue(any("Retired authority path still exists: meta" in e for e in errors))

    def test_retired_path_absent_passes(self) -> None:
        manifest = base_manifest(integrity={**base_manifest()["integrity"], "retired_paths": ["meta"]})
        errors: list[str] = []
        vr.validate_retired_paths(self.root, manifest, errors)
        self.assertEqual(errors, [])

    # --- invalid boot sequences ------------------------------------------

    def test_boot_sequence_duplicate_path_fails(self) -> None:
        manifest = base_manifest(
            boot={"quick_resume": ["brain/constitution.md", "brain/constitution.md"], "full_architectural": ["README.md"]}
        )
        errors: list[str] = []
        vr.validate_boot(self.root, manifest, errors)
        self.assertTrue(any("Duplicate path in quick_resume" in e for e in errors))

    def test_boot_sequence_unresolved_path_fails(self) -> None:
        manifest = base_manifest(
            boot={"quick_resume": ["brain/constitution.md", "brain/missing.md"], "full_architectural": ["README.md"]}
        )
        errors: list[str] = []
        vr.validate_boot(self.root, manifest, errors)
        self.assertTrue(any("Unresolved quick_resume boot path: brain/missing.md" in e for e in errors))

    def test_boot_sequence_wrong_start_fails(self) -> None:
        write(self.root, "brain/other.md", "# Other\n")
        manifest = base_manifest(boot={"quick_resume": ["brain/other.md"], "full_architectural": ["README.md"]})
        errors: list[str] = []
        vr.validate_boot(self.root, manifest, errors)
        self.assertTrue(any("Quick Resume must begin with brain/constitution.md" in e for e in errors))

    # --- ADR duplicates and numbering gaps -------------------------------

    def test_adr_duplicate_number_fails(self) -> None:
        write(self.root, "02-governance/architecture-decisions/ADR-0001-a.md", "# ADR 1\n")
        write(self.root, "02-governance/architecture-decisions/ADR-0001-b.md", "# ADR 1 duplicate\n")
        errors: list[str] = []
        vr.validate_adrs(self.root, base_manifest(), errors)
        self.assertTrue(any("Duplicate ADR number 0001" in e for e in errors))

    def test_adr_numbering_gap_fails(self) -> None:
        write(self.root, "02-governance/architecture-decisions/ADR-0001-a.md", "# ADR 1\n")
        write(self.root, "02-governance/architecture-decisions/ADR-0003-c.md", "# ADR 3\n")
        errors: list[str] = []
        vr.validate_adrs(self.root, base_manifest(), errors)
        self.assertTrue(any("ADR numbering gap: 0002" in e for e in errors))

    def test_adr_sequential_passes(self) -> None:
        write(self.root, "02-governance/architecture-decisions/ADR-0001-a.md", "# ADR 1\n")
        write(self.root, "02-governance/architecture-decisions/ADR-0002-b.md", "# ADR 2\n")
        errors: list[str] = []
        vr.validate_adrs(self.root, base_manifest(), errors)
        self.assertEqual(errors, [])

    def test_adr_invalid_filename_fails(self) -> None:
        write(self.root, "02-governance/architecture-decisions/ADR-1-bad-name.md", "# Bad\n")
        errors: list[str] = []
        vr.validate_adrs(self.root, base_manifest(), errors)
        self.assertTrue(any("Invalid ADR filename" in e for e in errors))

    # --- unresolved placeholders ------------------------------------------

    def test_unresolved_placeholder_fails(self) -> None:
        write(self.root, "01-philosophy/draft.md", "# Draft\n\nTODO: finish this section.\n")
        errors: list[str] = []
        vr.validate_placeholders(self.root, base_manifest(), errors)
        self.assertTrue(any("Unresolved placeholder" in e for e in errors))

    def test_excluded_placeholder_passes(self) -> None:
        write(self.root, "00-workbench/draft.md", "# Draft\n\nTODO: finish this section.\n")
        manifest = base_manifest(integrity={**base_manifest()["integrity"], "placeholder_exclusions": ["00-workbench"]})
        errors: list[str] = []
        vr.validate_placeholders(self.root, manifest, errors)
        self.assertEqual(errors, [])

    # --- broken relative links --------------------------------------------

    def test_broken_relative_link_fails(self) -> None:
        write(self.root, "01-philosophy/index.md", "See [missing](./missing.md).\n")
        errors: list[str] = []
        vr.validate_markdown_links(self.root, errors)
        self.assertTrue(any("Broken link" in e for e in errors))

    def test_valid_relative_link_passes(self) -> None:
        write(self.root, "01-philosophy/target.md", "# Target\n")
        write(self.root, "01-philosophy/index.md", "See [target](./target.md).\n")
        errors: list[str] = []
        vr.validate_markdown_links(self.root, errors)
        self.assertEqual(errors, [])

    def test_link_escaping_repository_fails(self) -> None:
        write(self.root, "01-philosophy/index.md", "See [outside](../../../outside.md).\n")
        errors: list[str] = []
        vr.validate_markdown_links(self.root, errors)
        self.assertTrue(any("escapes repository" in e for e in errors))

    def test_external_link_is_ignored(self) -> None:
        write(self.root, "01-philosophy/index.md", "See [external](https://example.com/page#section).\n")
        errors: list[str] = []
        vr.validate_markdown_links(self.root, errors)
        self.assertEqual(errors, [])

    # --- anchor validation --------------------------------------------------

    def test_valid_anchor_passes(self) -> None:
        write(self.root, "01-philosophy/target.md", "# Target\n\n## Purpose\n")
        write(self.root, "01-philosophy/index.md", "See [purpose](./target.md#purpose).\n")
        errors: list[str] = []
        vr.validate_markdown_links(self.root, errors)
        self.assertEqual(errors, [])

    def test_missing_anchor_fails(self) -> None:
        write(self.root, "01-philosophy/target.md", "# Target\n\n## Purpose\n")
        write(self.root, "01-philosophy/index.md", "See [nowhere](./target.md#does-not-exist).\n")
        errors: list[str] = []
        vr.validate_markdown_links(self.root, errors)
        self.assertTrue(any("Broken anchor" in e for e in errors))

    def test_anchor_punctuation_is_slugified(self) -> None:
        write(self.root, "01-philosophy/target.md", "# Target\n\n## What's Next?\n")
        write(self.root, "01-philosophy/index.md", "See [next](./target.md#whats-next).\n")
        errors: list[str] = []
        vr.validate_markdown_links(self.root, errors)
        self.assertEqual(errors, [])

    def test_anchor_unslugified_punctuation_fails(self) -> None:
        write(self.root, "01-philosophy/target.md", "# Target\n\n## What's Next?\n")
        write(self.root, "01-philosophy/index.md", "See [next](./target.md#what's-next?).\n")
        errors: list[str] = []
        vr.validate_markdown_links(self.root, errors)
        self.assertTrue(any("Broken anchor" in e for e in errors))

    def test_anchor_repeated_heading_deduplication(self) -> None:
        write(self.root, "01-philosophy/target.md", "# Target\n\n## Setup\n\nFirst.\n\n## Setup\n\nSecond.\n")
        write(self.root, "01-philosophy/first.md", "See [first](./target.md#setup).\n")
        write(self.root, "01-philosophy/second.md", "See [second](./target.md#setup-1).\n")
        write(self.root, "01-philosophy/third.md", "See [missing](./target.md#setup-2).\n")
        errors: list[str] = []
        vr.validate_markdown_links(self.root, errors)
        self.assertFalse(any("first.md" in e for e in errors))
        self.assertFalse(any("second.md" in e for e in errors))
        self.assertTrue(any("third.md" in e and "Broken anchor" in e for e in errors))

    def test_anchor_with_url_encoded_path(self) -> None:
        write(self.root, "01-philosophy/target file.md", "# Target File\n\n## Overview\n")
        write(self.root, "01-philosophy/index.md", "See [overview](./target%20file.md#overview).\n")
        errors: list[str] = []
        vr.validate_markdown_links(self.root, errors)
        self.assertEqual(errors, [])

    def test_same_document_anchor_passes(self) -> None:
        write(self.root, "01-philosophy/index.md", "# Index\n\n## Section\n\nSee [section](#section).\n")
        errors: list[str] = []
        vr.validate_markdown_links(self.root, errors)
        self.assertEqual(errors, [])

    def test_same_document_missing_anchor_fails(self) -> None:
        write(self.root, "01-philosophy/index.md", "# Index\n\nSee [nowhere](#missing).\n")
        errors: list[str] = []
        vr.validate_markdown_links(self.root, errors)
        self.assertTrue(any("Broken anchor" in e for e in errors))

    def test_anchor_check_skips_code_fences(self) -> None:
        write(self.root, "01-philosophy/target.md", "# Target\n\n```text\n## Not A Heading\n```\n\n## Real Heading\n")
        write(self.root, "01-philosophy/index.md", "See [real](./target.md#real-heading).\n")
        write(self.root, "01-philosophy/other.md", "See [fake](./target.md#not-a-heading).\n")
        errors: list[str] = []
        vr.validate_markdown_links(self.root, errors)
        self.assertFalse(any("index.md" in e for e in errors))
        self.assertTrue(any("other.md" in e and "Broken anchor" in e for e in errors))

    # --- repository-map <-> manifest consistency --------------------------

    def test_map_manifest_agreement_passes(self) -> None:
        write(
            self.root,
            "brain/repository-map.md",
            "# Repository Map\n\n"
            "| Area | Canonical location | Authority |\n"
            "|---|---|---|\n"
            "| Philosophy | [`../01-philosophy/`](../01-philosophy/) | x |\n"
            "| Governance | [`../02-governance/`](../02-governance/) | x |\n"
            "| Architecture decisions | [`../02-governance/architecture-decisions/`](../02-governance/architecture-decisions/) | x |\n"
            "| Spark Brain | [`./`](./) | x |\n",
        )
        errors: list[str] = []
        vr.validate_map_manifest_consistency(self.root, base_manifest(), errors)
        self.assertEqual(errors, [])

    def test_map_manifest_disagreement_fails(self) -> None:
        write(
            self.root,
            "brain/repository-map.md",
            "# Repository Map\n\n"
            "| Area | Canonical location | Authority |\n"
            "|---|---|---|\n"
            "| Philosophy | [`../01-philosophy/`](../01-philosophy/) | x |\n"
            "| Spark Brain | [`./`](./) | x |\n",
        )
        errors: list[str] = []
        vr.validate_map_manifest_consistency(self.root, base_manifest(), errors)
        self.assertTrue(any("02-governance" in e for e in errors))

    def test_map_manifest_missing_map_file_fails(self) -> None:
        errors: list[str] = []
        vr.validate_map_manifest_consistency(self.root, base_manifest(), errors)
        self.assertTrue(any("Missing brain/repository-map.md" in e for e in errors))


class ManifestSerializationContractTest(unittest.TestCase):
    """Locks in the current, undocumented manifest.yaml <-> json.loads() contract."""

    def test_real_manifest_is_valid_json(self) -> None:
        manifest_path = TOOLS_DIR.parent / "brain" / "manifest.yaml"
        json.loads(manifest_path.read_text(encoding="utf-8"))

    def test_load_manifest_rejects_non_json_yaml_syntax(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "brain/manifest.yaml", "# a YAML comment is not valid JSON\nkey: value\n")
            errors: list[str] = []
            manifest = vr.load_manifest(root, errors)
            self.assertEqual(manifest, {})
            self.assertTrue(any("not valid JSON-compatible YAML" in e for e in errors))

    def test_load_manifest_missing_file_reports_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            errors: list[str] = []
            manifest = vr.load_manifest(root, errors)
            self.assertEqual(manifest, {})
            self.assertTrue(any("Missing brain/manifest.yaml" in e for e in errors))


class RealRepositoryIntegrationTest(unittest.TestCase):
    """Runs the full validator against the actual checked-out repository."""

    def test_actual_repository_passes(self) -> None:
        repo_root = TOOLS_DIR.parent
        self.assertEqual(vr.main(repo_root), 0)


if __name__ == "__main__":
    unittest.main()
