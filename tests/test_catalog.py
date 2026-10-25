import json
import subprocess
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


class CatalogTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run([sys.executable, "scripts/build_source_catalog.py"], cwd=REPO, check=True, capture_output=True)
        cls.rows = [json.loads(line) for line in (REPO / "data/source_catalog.jsonl").read_text().splitlines()]

    def test_expected_case_count(self):
        self.assertEqual(len(self.rows), 209)

    def test_task_group_count(self):
        groups = {(row["paper_target"], row["user_task_id"]) for row in self.rows}
        self.assertEqual(len(groups), 12)

    def test_source_hashes_and_roles(self):
        self.assertTrue(all(len(row["source_sha256"]) == 64 for row in self.rows))
        self.assertTrue(all(row["reuse_role"] == "mutation_library_only" for row in self.rows))

    def test_all_rows_have_frozen_plan_and_trace(self):
        self.assertTrue(all(row["has_frozen_plan"] for row in self.rows))
        self.assertTrue(all(row["has_tool_trace"] for row in self.rows))


if __name__ == "__main__":
    unittest.main()

