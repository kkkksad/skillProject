"""CLI regression tests; every generated artifact stays in a temporary directory."""

import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "scaffold_repo_docs.py"


class ScaffoldTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="skill-scaffold-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, "-X", "utf8", "-B", str(SCRIPT), str(self.root), *args],
            capture_output=True,
            text=True,
            encoding="utf-8",
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )

    def snapshot(self):
        return {
            str(path.relative_to(self.root)): path.read_bytes()
            for path in self.root.rglob("*") if path.is_file()
        }

    def test_distinct_chinese_titles_create_distinct_plans(self):
        for title in ("新增评论", "修改权限"):
            self.assertEqual(self.run_cli("--task-title", title).returncode, 0)
        plans = list((self.root / "docs/exec-plans/active").glob("*.md"))
        self.assertEqual(len(plans), 2)
        for title in ("新增评论", "修改权限"):
            self.assertTrue(any(p.read_text(encoding="utf-8").startswith(f"# {title}\n") for p in plans))

    def test_punctuation_only_titles_do_not_collide(self):
        for title in ("!!!", "???"):
            self.assertEqual(self.run_cli("--task-title", title).returncode, 0)
        self.assertEqual(len(list((self.root / "docs/exec-plans/active").glob("*.md"))), 2)

    def test_explicit_slug_collision_fails_before_writing(self):
        plans = self.root / "docs/exec-plans/active"
        plans.mkdir(parents=True)
        (plans / "shared.md").write_text("# First task\n\nUser notes\n", encoding="utf-8")
        before = self.snapshot()
        result = self.run_cli("--task-title", "Second task", "--task-slug", "shared")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--task-slug", result.stderr)
        self.assertEqual(before, self.snapshot())

    def test_dry_run_creates_nothing(self):
        result = self.run_cli("--dry-run", "--task-title", "新增评论")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Would create", result.stdout)
        self.assertEqual(list(self.root.iterdir()), [])

    def test_repeated_task_preserves_edited_plan_and_baseline(self):
        self.assertEqual(self.run_cli("--task-title", "Add comments").returncode, 0)
        plan = next((self.root / "docs/exec-plans/active").glob("*.md"))
        plan.write_text("# Add comments\n\nUser approved content\n", encoding="utf-8")
        before = self.snapshot()
        self.assertEqual(self.run_cli("--task-title", "Add comments").returncode, 0)
        self.assertEqual(before, self.snapshot())

    def test_existing_agents_is_preserved(self):
        agents = self.root / "AGENTS.md"
        agents.write_text("Existing project rules\n", encoding="utf-8")
        self.assertEqual(self.run_cli().returncode, 0)
        self.assertEqual(agents.read_text(encoding="utf-8"), "Existing project rules\n")

    def test_slug_stays_in_active_directory(self):
        result = self.run_cli("--task-title", "Safe plan", "--task-slug", "../../outside")
        self.assertEqual(result.returncode, 0)
        plans = list((self.root / "docs/exec-plans/active").glob("*.md"))
        self.assertEqual(len(plans), 1)
        self.assertEqual(plans[0].parent, self.root / "docs/exec-plans/active")

    def test_windows_reserved_name_can_be_used_as_title(self):
        result = self.run_cli("--task-title", "NUL")
        self.assertEqual(result.returncode, 0, result.stderr)
        plans = list((self.root / "docs/exec-plans/active").glob("*.md"))
        self.assertEqual(len(plans), 1)
        self.assertTrue(plans[0].read_text(encoding="utf-8").startswith("# NUL\n"))

    def test_slug_without_title_is_rejected(self):
        result = self.run_cli("--task-slug", "orphan")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(list(self.root.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
