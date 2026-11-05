#!/usr/bin/env sh
# SessionStart hook shared by every plugin in this collection. Prints the plugin's main SKILL.md (without frontmatter) so the
# rules apply to every reply while the plugin is enabled. Off for good: `claude plugin disable <name>@claude-accessibility`,
# or create the empty file ~/.claude/.<name>-off. Never blocks session start: any failure exits 0.
# Runs in sh on Linux/macOS and in Git Bash on Windows (no Node needed).

plugin_root=$(cd -- "$(dirname -- "$0")/.." 2>/dev/null && pwd) || exit 0
name=$(basename -- "$plugin_root")
claude_dir="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
[ -f "$claude_dir/.$name-off" ] && exit 0

skill="$plugin_root/skills/$name/SKILL.md"
[ -f "$skill" ] || exit 0

body=$(awk 'NR==1 && /^---[[:space:]]*$/ {fm=1; next} fm && /^---[[:space:]]*$/ {fm=0; next} !fm {print}' "$skill") || exit 0
printf '%s MODE ACTIVE (claude-accessibility plugin "%s"). The rules below apply to every response this session.\n\n%s\n' \
  "$(printf '%s' "$name" | tr 'a-z-' 'A-Z ')" "$name" "$body"
exit 0
