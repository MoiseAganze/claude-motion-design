---
name: video-playbook
description: House playbook for making videos in THIS repo (cloud sessions, HyperFrames). Read right after /hyperframes routes a creation, and before any edit/re-render of a project under videos/. Covers the ElevenLabs-voice pipeline (product-launch-video has no host-narration path), bundled SFX cueing, caption fixes, 9:16 TikTok safe zones, frame-authoring pitfalls that fail lint/check, and the draft→final render loop. Scripts in scripts/ replace the steps that broke last time.
---

# Video playbook (lessons from `videos/agent-courrier`)

`/hyperframes` and the workflow skills stay the source of truth. This file only adds what they
don't know about this environment. Reference project: `videos/agent-courrier` (11 frames, 9:16, ~58s,
ElevenLabs VO + bundled SFX + CTA). Its `production.json` is the template to copy.

## 0. Environment facts (don't rediscover them)

- Network: `cdn.jsdelivr.net`, `fonts.googleapis.com`, `fonts.gstatic.com`, `storage.googleapis.com` (ElevenLabs downloads) are reachable. **Openverse, unpkg, transparenttextures are blocked** → SFX come from the bundled library only; never reference other CDNs or remote textures.
- `NODE_USE_ENV_PROXY=1` is required for the render compiler to inline CDN scripts (the SessionStart hook sets it).
- Not signed in to HeyGen; Kokoro/MusicGen not installed → `audio.mjs` cannot make narration. Voice = ElevenLabs connector (`mcp__ElevenLabs__*`).
- Studio preview is not reachable from the user's device in a cloud session → the review surface is a **draft MP4 sent with SendUserFile**.
- No emoji font in headless Chrome → draw icons as inline SVG, never emoji.

## 1. Pipeline for a narrated promo (product-launch-video)

Follow the workflow's Steps 0–4 (BRIEF → no-capture files → `build-frame.mjs` → STORYBOARD/SCRIPT with
shot sequences), then deviate here:

1. **Voice** (§2) → put the take(s) in `assets/voice/`, fill `production.json` `voice`.
2. **SFX**: write cues in `production.json` `sfx` (keys of `.claude/skills/media-use/audio/assets/sfx/manifest.json`). **Never run `audio.mjs fetch-sfx`**: it wipes host voices and puts every cue at offset 0.
3. **Frames**: `frame-packets.mjs` caps a packet at 48 KB — cite ≤ 2–3 rule ids per frame (blueprints `kinetic-type-beats`, `logo-assemble-lockup` are ~28 KB alone). Building frames yourself (sequentially) is fine and keeps the hero object consistent across frames.
4. **Everything after** — any change to voice, cues, durations, frames, captions:
   `.claude/skills/video-playbook/scripts/rebuild.sh videos/<project>` (vo → sync-durations → sfx → captions build → captions tune → assemble → transitions inject/verify → check). Use `--no-vo` to skip re-cutting audio.
5. **Review**: snapshot (`npx hyperframes snapshot --at …`, read the contact sheet), fix, then draft render (§6).

## 2. ElevenLabs voice (credits are scarce — check before spending)

- Pick the voice with `creative_list_voices` (languages, gender, search). Used so far: **Atma** `vq479zipNPD44hpCdbIh` (fr, warm, premium). Model `eleven_v4`, inline tags like `[warm, premium]` work.
- **Always `estimate_only: true` first.** ~1.27 credits/char per take; a 35s script ≈ 710 credits per take. A take past the quota fails (not charged). If 4 takes don't fit, ask for `generations_count` that fits and say why.
- Generate the **whole script as ONE take** (natural prosody, one charge), each sentence separated by a blank line. Later additions (e.g. a CTA) = a second take in `production.json`.
- Download `content_url` with curl (signed, 2h expiry) into `assets/voice/` and commit it.
- `scripts/vo.py` needs **one speech segment per sentence**: the `sentences` list must match the pauses the voice actually makes (very short sentences like "À lire." are their own segment). On mismatch it prints the segments: adjust `silence_db`/`min_silence` or merge sentences. Choose the take whose segment count matches (no need to listen).
- Per-frame `lead`/`tail` (seconds of silence) are where pacing lives: target length = sum of speech + leads + tails. Give the outro/CTA long tails so text can be read.
- Match loudness across takes with `gain_db` (compare `ffmpeg -af volumedetect` mean_volume; main take ≈ −26 dB).
- **User music bed** (e.g. a track downloaded from ElevenLabs Music — the connectors cannot list or fetch the user's saved music, ask for the MP3): copy it to `assets/bgm/`, extend it to the cut with `scripts/bed.py <src.mp3> <total_s> <out.mp3>` (one crossfade at the most similar point, so the natural ending lands on the last frame; re-run whenever the total changes), then set `audio_meta.json` `"bgm": {"path": "assets/bgm/<bed>.mp3", "source": "host"}` (keep `music: none` in the storyboard). `rebuild.sh` tags the voice clips `data-audio-group="voiceover"` and runs the hyperframes-audio carve at `production.json` `carve_strength` (default 0.8; use **0.5** with a bed at volume 0.2 — at 0.8 the level-match stacks on the low volume and the music vanishes in every pause) (needs `npm i -D @hyperframes/core@<pinned>` in the project). Reference: `videos/signal-esursi`.

## 3. Design system

- No dark preset ships. `build-frame.mjs` maps brand colors onto the preset's roles and produced a **light** theme from a dark palette → after it runs, swap `bg`/`text` (and muted/light) in `frame.md` by hand and add a "Brand override" section. `blue-professional` + night `#070B18` / blue `#3D7BFF` / violet `#7C5CFF` / mint `#38E1A6` worked well.
- Fonts must be local files. Download latin woff2 into `assets/fonts/` from `https://fonts.googleapis.com/css2?family=<Family>:wght@400..700` (send a Chrome User-Agent to get woff2) and use the **`latin`** subset (contains é à ç). `latin-ext` alone renders accents as fallback glyphs.

## 4. Frame authoring checklist (each item failed lint/check once)

- Ids: frame ids start with a digit → prefix ids/classes `fNN-` (e.g. `f07-phone`), give **every** `class="clip"` element an id.
- Register with `window.__timelines = window.__timelines || {}` before assigning.
- One `fromTo` per element+property; later moves on the same element use `.to` (repeated `fromTo` → `gsap_repeated_fromto_without_baseline`). Only `immediateRender:false` if a second fromTo is unavoidable.
- No `tl.call`, no CSS transitions/keyframes, no `Math.random` (use `Math.sin(i*12.9898+s*78.233)` hash), no repeat/yoyo.
- Hook frame: something visible at t=0 (start a few elements already mid-motion).
- Intentional overlap (stamps over text, masked flip lists, camera worlds) → `data-layout-allow-overlap` / `data-layout-allow-occlusion` / `data-layout-allow-overflow` on that element.
- Dimmed "old" text still needs ≥ 3:1 contrast (`#6b748c` on `#0E1430` passes, `#4a536b` fails).
- Elements that only matter after a camera move start at `opacity: 0` (they otherwise sit under the captions before the pan).
- Only the **last** frame exits. When a new final frame is added, delete the previous frame's exit tweens.
- Verify long headlines fit 1080 px (≈ 0.55 × font-size per char for Space Grotesk 700).

## 5. 9:16 TikTok layout + captions

- Content: y 150–1330, keep key text x ≤ ~990 (right rail icons). Hero anchored ~0.2–0.35 H.
- Captions band: `band_top 1370, band_height 170` (default 1600 sits under TikTok's description). `captions_tune.py` applies it and must re-run after every `captions.mjs build` (rebuild.sh does).
- `hide_frames`: frames whose on-screen type repeats the VO (question card, benefit slams, slogan, CTA).

## 6. Review, render, deliver

- Draft: `npx hyperframes render --skill=product-launch-video --output renders/<name>-brouillon.mp4` (~3 min for 58s) → SendUserFile, ask "rendu final ou changements ?".
- Loudness check: `ffmpeg -ss <t> -t 2 -i out.mp4 -af volumedetect -vn -f null -` at hook / mid / end. Hook SFX must not exceed the voice (keep hook cue volumes ≤ 0.2; global `gain` 0.75).
- Final: same command with `--quality high --output renders/<name>-final.mp4`.
- MP4s and `**/.hyperframes/artifacts/` are git-ignored; commit sources, `production.json`, voice takes and SFX.

## 7. Self-check for these scripts

After editing `scripts/`, run `scripts/rebuild.sh videos/agent-courrier` — it must end with `✓ check ok`
and leave `videos/agent-courrier/audio_meta.json` unchanged (`git diff --stat`).
