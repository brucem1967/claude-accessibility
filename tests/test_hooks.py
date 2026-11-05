"""Every plugin's start-up hook prints its own rules (no frontmatter) and stays silent when switched off."""
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGINS = sorted(p for p in (ROOT / "plugins").iterdir() if (p / ".claude-plugin" / "plugin.json").exists())


class HookTest(unittest.TestCase):
    def run_hook(self, plugin: Path, cfg: Path):
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, True)
        dest = tmp / "plugin cache with spaces" / plugin.name
        shutil.copytree(plugin, dest)
        env = dict(os.environ, CLAUDE_CONFIG_DIR=str(cfg))
        return subprocess.run([shutil.which("sh"), str(dest / "hooks" / "always-on.sh")],
                              capture_output=True, text=True, env=env, timeout=30)

    def test_each_plugin(self):
        self.assertGreaterEqual(len(PLUGINS), 2)
        for plugin in PLUGINS:
            with self.subTest(plugin=plugin.name):
                cfg = Path(tempfile.mkdtemp())
                self.addCleanup(shutil.rmtree, cfg, True)
                r = self.run_hook(plugin, cfg)
                self.assertEqual(r.returncode, 0, r.stderr)
                self.assertIn("MODE ACTIVE", r.stdout)
                self.assertIn(f'plugin "{plugin.name}"', r.stdout)
                self.assertIn(f"# {plugin.name}", r.stdout)
                self.assertNotIn("disable-model-invocation", r.stdout)       # frontmatter stripped
                (cfg / f".{plugin.name}-off").write_text("")
                r = self.run_hook(plugin, cfg)
                self.assertEqual((r.returncode, r.stdout), (0, ""))

    def test_marketplace_lists_every_plugin(self):
        mp = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
        listed = {p["name"]: p["source"] for p in mp["plugins"]}
        self.assertEqual(set(listed), {p.name for p in PLUGINS})
        for name, src in listed.items():
            self.assertEqual((ROOT / src).resolve(), (ROOT / "plugins" / name).resolve())
            pj = json.loads((ROOT / "plugins" / name / ".claude-plugin" / "plugin.json").read_text())
            self.assertEqual(pj["name"], name)

    def test_every_skill_has_frontmatter_name(self):
        for skill in ROOT.glob("plugins/*/skills/*/SKILL.md"):
            with self.subTest(skill=str(skill.relative_to(ROOT))):
                head = skill.read_text(encoding="utf-8").split("---")[1]
                self.assertIn(f"name: {skill.parent.name}", head)


if __name__ == "__main__":
    unittest.main()
