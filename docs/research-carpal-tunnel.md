# Research behind the carpal-tunnel plugin (November 2026)

The plugin changes how Claude works with someone whose hands hurt. It is not medical advice.

## What the evidence says

- **Computer work and carpal tunnel.** Mayo Clinic says there is not enough evidence that computer use directly causes carpal tunnel syndrome, and that some evidence links **mouse** use, not keyboard use, to it. It recommends short, frequent breaks, a neutral wrist, and a mouse that does not strain the wrist; there are no proven ways to prevent it. [Mayo Clinic: symptoms and causes](https://www.mayoclinic.org/diseases-conditions/carpal-tunnel-syndrome/symptoms-causes/syc-20355603), [Mayo Clinic Orthopedics: prevention](https://sportsmedicine.mayoclinic.org/condition/carpal-tunnel/page/7)
- **An older systematic review** (Thomsen, Gerr and Atroshi, BMC Musculoskeletal Disorders, 2008) found insufficient evidence that computer work causes CTS. Either way, people who already have it report that typing and especially mouse work aggravate it.
- **Alternative input helps symptoms.** A CDC-hosted study found an alternative mouse design cut wrist/hand pain in symptomatic workers. [CDC stacks](https://stacks.cdc.gov/view/cdc/188384/cdc_188384_DS1.pdf)
- **Dictation moves load off the hands**, with the trade-off that heavy correction work can cancel the benefit; dictation is best for longer text and works best when the listener tolerates recognition errors. (Several sources, mostly vendors of voice software, so weighed cautiously: [Willow](https://willowvoice.com/blog/typing-with-carpal-tunnel-when-to-switch-to-voice-input), [VoiceDash](https://voicedash.ai/typing-with-carpal-tunnel/).)
- **Motor-accessibility standards** (WCAG 2.2) require that anything done by dragging can also be done with a single click or tap, that gestures have simple alternatives, and that targets are big enough (24x24 px minimum, 44x44 enhanced) because some people cannot hit small, close buttons. [Dragging movements 2.5.7](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html), [Pointer gestures 2.5.1](https://www.w3.org/WAI/WCAG22/Understanding/pointer-gestures.html), [WCAG 2.2](https://www.w3.org/TR/WCAG22/)

## Tools the plugin points people to

- **Claude Code voice dictation**: `/voice` (hold Space) or `/voice tap` (tap to start, tap to send; nothing held down). Settings object `voice: {enabled, mode, autoSubmit}`. Needs a claude.ai sign-in; not over SSH or cloud sessions; does not use Claude tokens. [Docs](https://code.claude.com/docs/en/voice-dictation)
- **Windows voice typing**: Windows key + H in any text box; auto punctuation setting. [Microsoft](https://support.microsoft.com/en-us/accessibility/windows/use-voice-typing-to-talk-instead-of-type-on-your-pc)
- **Windows Voice access**: Settings > Accessibility > Speech. "Click <name>", "Show numbers", "Show grid", dictation with spoken punctuation; English, Spanish, French, German. [Command list](https://support.microsoft.com/en-us/topic/voice-access-command-list-dac0f091-87ce-454d-8d57-bef38d3d8563), [Interact with items](https://support.microsoft.com/en-US/accessibility/windows/voice-access/use-voice-to-interact-with-items-on-the-screen), [AbilityNet guide](https://mcmw.abilitynet.org.uk/how-to-use-voice-access-in-windows-11)
- **macOS Dictation and Voice Control**; **phone keyboard microphone**.

## How that became rules

| Finding | Rule in SKILL.md |
|---|---|
| Every keystroke and click costs; copying/retyping is worst | 1 Do it yourself first; 7 Keep text they must type tiny |
| Replies cost effort; round trips multiply it | 2 One-word answers; 3 Ask once, not in drips; 8 Fewer, bigger steps |
| Dictation brings recognition errors; correcting them cancels the benefit | 4 Read dictated replies generously, confirm only when a wrong guess matters |
| Voice input moves load off the hands | 5 Steer to the voice (tap mode first), say button names exactly so "Click <name>" works |
| Mouse, dragging, small targets and stretches are the hard parts (Mayo, WCAG 2.5.x) | 6 Easiest physical action first; alternatives to drag, double-click, right-click, 3-key combos |
| No proven prevention; not our role to diagnose | 9 If they say it hurts: take over more work, no lectures, suggest a clinician only if new/severe |
