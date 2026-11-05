---
name: voice-setup
description: 'Switch on talking instead of typing for someone whose hands hurt: Claude Code voice dictation in tap mode (no key held down), plus how to start voice typing and Voice access on Windows or Voice Control on a Mac. Use when the reader asks to talk instead of type, mentions sore hands, carpal tunnel, RSI, or asks how to use voice.'
license: MIT
metadata:
  tags: "Accessibility, Voice, Dictation, Carpal tunnel"
  category: "accessibility"
---

# voice-setup

Goal: the reader can talk to Claude and to their computer instead of typing. Do the setup yourself where you can; ask them only to speak, or to click once.

## 1. Claude Code voice dictation (do this for them)

Claude Code has built-in dictation (docs: https://code.claude.com/docs/en/voice-dictation). It needs a claude.ai sign-in, a microphone, and a local session (it does not work over SSH or in cloud sessions). Transcription does not use Claude messages or tokens.

Tap mode is best for sore hands: tap Space once to start talking, tap again to send. No key is held down.

1. Edit the user settings file (`~/.claude/settings.json`; on Windows `%USERPROFILE%\.claude\settings.json`). Read it first and keep everything already in it. Set:
   ```json
   "voice": { "enabled": true, "mode": "tap", "autoSubmit": true }
   ```
   (`autoSubmit` sends the message when they stop, if it is at least three words.)
2. Tell them, in one or two lines: "Done. Next time you open Claude, tap the Space bar once, talk, then tap Space again to send." If the change does not take effect in this session, they can also type `/voice tap` once.
3. If they prefer holding a key: `"mode": "hold"` (hold Space while talking).
4. If the microphone check fails: ask them to plug in or switch on the microphone, or on Windows to open Settings > Privacy & security > Microphone and turn on "Microphone access". Ask for a photo of the screen if it still fails.

## 2. Voice typing everywhere on Windows

- Windows key + H opens voice typing in any text box (email, Word, a browser). It needs the internet and a microphone. Say "full stop", "comma", "new line". In the voice typing settings (the gear on the toolbar), turn on "Auto punctuation".
- Voice access controls the whole computer by voice: Start > Settings > Accessibility > Speech > Voice access, switch it On. Then they can say "Click Save", "Open Edge", "Scroll down", "Show numbers" (then "Click 5"), "Show grid". Microsoft's command list: https://support.microsoft.com/en-us/topic/voice-access-command-list-dac0f091-87ce-454d-8d57-bef38d3d8563
- Tip: with Voice access on, "Voice access wake up" / "Voice access sleep" turns listening on and off.

## 3. On a Mac

- Dictation: System Settings > Keyboard > Dictation, On. Start it with the microphone key or by pressing Fn twice.
- Voice Control (whole computer by voice): System Settings > Accessibility > Voice Control, On. Then "Click Save", "Show numbers", "Scroll down".

## 4. Phone

The microphone button on the phone keyboard turns speech into text in any app, including the Claude app.

Give them only the part they need, one step at a time, with the button names exactly as they appear.
