---
name: voice-notes
description: Take voice memos instead of typing: the person records a note (interview debrief, weekly review answers, intake answers, a post idea) and this skill transcribes it through a transcription MCP server or a local whisper install, then routes the text to the right skill. Removes the last typing step. Use when the user drops an audio file or says "voice note".
disable-model-invocation: false
allowed-tools: "Read Write Bash(whisper *) Bash(ffmpeg *) Bash(ls *) Bash(python3 *)"
---

# Voice notes

Inputs: an audio file path (m4a, mp3, wav, ogg) or a recording from a connected MCP server
(a transcription server, or a notes app that already transcribed it). Output:
`out/voice/<date>-<slug>.md` with the transcript, then the routed skill's output.

## Transcribe

1. A transcription MCP server if connected (use its tool, language from `identity.md`).
2. Else a local `whisper` command if installed (`whisper <file> --language <xx> --model small
   --output_format txt`), converting with `ffmpeg` if the format is not supported.
3. Else say what to install or connect; never upload the audio to a service the user did not
   connect.

## Route by content

- Mentions an interview that happened: `interview-debrief`.
- Answers to weekly questions (what went well, what to change, numbers): `weekly-review`.
- Onboarding answers during `intake`: back into the interview.
- A post idea or a story: `linkedin-post` draft with the transcript as the source.
- A job or company name with "apply", "skip", "follow up": `application-tracker` update.
- Unclear: show the transcript and ask which.

Clean the transcript lightly (filler words, false starts); keep the person's phrasing, it is
voice data for `voice.md`. Audio files stay in the workspace and are gitignored.
