import importlib.util
import sys
import tempfile
import unittest
import urllib.error
from contextlib import redirect_stdout
from io import StringIO
from argparse import Namespace
from unittest import mock
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "literature.py"
SPEC = importlib.util.spec_from_file_location("literature", MODULE_PATH)
literature = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = literature
SPEC.loader.exec_module(literature)

VALIDATOR_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_sources.py"
VALIDATOR_SPEC = importlib.util.spec_from_file_location("validate_sources", VALIDATOR_PATH)
validate_sources = importlib.util.module_from_spec(VALIDATOR_SPEC)
assert VALIDATOR_SPEC.loader is not None
sys.modules[VALIDATOR_SPEC.name] = validate_sources
VALIDATOR_SPEC.loader.exec_module(validate_sources)


class LiteratureHelpersTest(unittest.TestCase):
    def test_normalize_doi(self):
        self.assertEqual(literature.normalize_doi("https://doi.org/10.1000/Example."), "10.1000/example")

    def test_normalize_title(self):
        self.assertEqual(literature.normalize_title("PK/PD: A Practical Guide"), "pk pd a practical guide")

    def test_schema_validator_rejects_extra_fields(self):
        schema = {
            "type": "object",
            "required": ["id"],
            "additionalProperties": False,
            "properties": {"id": {"type": "string"}},
        }
        issues = literature.schema_issues({"id": "x", "unexpected": True}, schema, "$", MODULE_PATH)
        self.assertEqual([issue.code for issue in issues], ["schema_extra_field"])

    def test_schema_validator_handles_nullable_types(self):
        self.assertEqual(literature.schema_issues(None, {"type": ["string", "null"]}, "$.doi", MODULE_PATH), [])

    def test_reviewed_record_requires_auditable_metadata(self):
        records = {"example_2026": {"review_status": "reviewed"}}
        paths = {"example_2026": MODULE_PATH}
        issues = literature.check_review_metadata(records, paths)
        self.assertEqual([issue.code for issue in issues], ["review_metadata_missing"])

    def test_draft_count_is_reported_without_becoming_a_warning(self):
        output = StringIO()
        records = {"example_2026": {"review_status": "draft"}}
        with redirect_stdout(output):
            literature.display([], records, "text")
        self.assertIn("0 warnings | 1 drafts", output.getvalue())
        self.assertIn("Human review remains", output.getvalue())

    def test_fix_refuses_to_write_when_any_record_error_exists(self):
        issue = literature.Issue("error", "json_parse", "broken record", "papers/broken.json")
        with mock.patch.object(literature, "load_records", return_value=({}, {}, [issue])), \
             mock.patch.object(literature, "write_json") as write_json, \
             mock.patch.object(literature.subprocess, "run") as run:
            with self.assertRaises(SystemExit):
                literature.fix_library()
        write_json.assert_not_called()
        run.assert_not_called()

    def test_source_identifier_pattern(self):
        text = "Use `saini_2025_qsp_copilot`, but M4.5-A8 is an activity."
        self.assertEqual(literature.SOURCE_ID_RE.findall(text), ["saini_2025_qsp_copilot"])

    def test_compact_scalar_arrays(self):
        expanded = '{\n  "pillars": [\n    "a",\n    "b"\n  ],\n  "objects": [\n    {\n      "x": 1\n    }\n  ]\n}'
        compacted = literature.compact_scalar_arrays(expanded)
        self.assertIn('"pillars": ["a", "b"],', compacted)
        self.assertIn('"objects": [\n', compacted)

    def test_transient_metadata_error_is_not_not_found(self):
        with mock.patch.object(
            validate_sources.urllib.request,
            "urlopen",
            side_effect=urllib.error.URLError("offline"),
        ), mock.patch.object(validate_sources, "RETRY_DELAYS", (0.0,)):
            with self.assertRaises(validate_sources.MetadataServiceUnavailable):
                validate_sources._get("https://example.invalid")

    def test_confirmed_404_is_not_found(self):
        error = urllib.error.HTTPError("https://example.invalid", 404, "not found", {}, None)
        with mock.patch.object(validate_sources.urllib.request, "urlopen", side_effect=error):
            with self.assertRaises(validate_sources.IdentifierNotFound):
                validate_sources._get("https://example.invalid")

    def test_add_creates_intake_not_source_json(self):
        original_sources_dir = literature.SOURCES_DIR
        try:
            with tempfile.TemporaryDirectory() as temporary_directory:
                literature.SOURCES_DIR = Path(temporary_directory)
                literature.create_intake(
                    Namespace(
                        identifier="10.1000/example",
                        title="Example",
                        contributor="Collaborator",
                        notes="For training",
                    )
                )
                intakes = list((Path(temporary_directory) / "intake").glob("*.md"))
                self.assertEqual(len(intakes), 1)
                self.assertEqual(list(Path(temporary_directory).glob("*.json")), [])
                self.assertIn("10.1000/example", intakes[0].read_text(encoding="utf-8"))
        finally:
            literature.SOURCES_DIR = original_sources_dir


if __name__ == "__main__":
    unittest.main()
