# claude-accessibility

Claude Code plugins that change how Claude works with you, depending on what you need. Pick the ones that fit; they combine.

| If this sounds like you | Install | What changes |
|---|---|---|
| My hands hurt or tire: carpal tunnel, RSI, arthritis, hand pain | `carpal-tunnel` | Claude does the work itself, asks questions you can answer in one word, reads dictated text generously, offers voice first, avoids drags, double-clicks and finger-twisting shortcuts. Includes `voice-setup`, which switches on talking instead of typing. |
| Too much information at once overwhelms me; I am not technical | `i-get-overwhelmed` | Calm first line, one thing at a time, plain words, click-by-click steps that say what you will see, one easy question. |
| ADHD | use [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | Action first, numbered steps, no tangents. |

Wanted next (help welcome, see [CONTRIBUTING.md](CONTRIBUTING.md)): low vision, screen reader users, dyslexia, memory or brain injury, tremor and limited dexterity, chronic fatigue.

## Install

In Claude Code:

```
claude plugin marketplace add bamboostack/claude-accessibility
claude plugin install carpal-tunnel@claude-accessibility
claude plugin install i-get-overwhelmed@claude-accessibility
```

Install only the ones you want. Each is **on in every session while it is enabled**.

- Off for one session: say "stop carpal tunnel mode" (or "stop overwhelm mode").
- Off for good: `claude plugin disable carpal-tunnel@claude-accessibility`, or create the empty file `~/.claude/.carpal-tunnel-off`.
- Updates: `claude plugin marketplace update claude-accessibility`, then `claude plugin update <name>@claude-accessibility`.

## Tell Claude about yourself (optional)

These plugins are general. Anything personal ("I work nights", "my partner handles the banking", "I use Dragon") belongs in your own `~/.claude/CLAUDE.md`, which Claude Code reads in every session. Keep it out of any public repo.

## How it works

Each plugin has one main skill (`plugins/<name>/skills/<name>/SKILL.md`) and a small start-up hook that loads it into every session. The hook is a plain shell script: no network, no Node, it only reads its own file. Read them before installing; they are short.

## Research

The rules come from published guidance, linked in [docs/research-carpal-tunnel.md](docs/research-carpal-tunnel.md).

## Tests

```
python3 tests/test_hooks.py          # every plugin's hook: prints its rules, stays silent when switched off
python3 tests/run_scenarios.py       # optional: real Claude replies to sample requests, checked against each plugin's rules
```

For a fair scenario run, use a Claude config without your own CLAUDE.md or other style plugins (set `CLAUDE_CONFIG_DIR` to an empty folder holding only your sign-in) and run it from a folder with no CLAUDE.md above it.

```
```

## Credits and licence

MIT. `i-get-overwhelmed` is a fork of [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) by Ayoub G. (MIT).
