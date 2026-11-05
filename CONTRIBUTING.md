# Adding a plugin for another need

1. Copy `templates/plugin` to `plugins/<name>` (lower-case, dashes). The folder name is the plugin name.
2. Rename `skills/NAME` to `skills/<name>` and write `SKILL.md`:
   - what this need changes about using a computer or reading Claude's replies (facts, not stereotypes)
   - numbered rules, each with a Bad / Good example
   - "When to break the rules" and a short pre-send check
   - persistence: on by default; "stop <name> mode" turns it off for the session
3. Fill in `.claude-plugin/plugin.json`, add the plugin to `.claude-plugin/marketplace.json`, and add a row to the README table.
4. Put the evidence in `docs/research-<name>.md`: sources you can link, and a table from finding to rule. Prefer people with that lived experience, clinical bodies and accessibility standards over vendor blogs.
5. Add 2-3 scenarios to `tests/scenarios/<name>.json` and run `python3 tests/test_hooks.py` and `claude plugin validate .`.

Keep the hook as it is (`always-on.sh` is shared and reads the plugin name from its folder). No network calls, no personal data.
