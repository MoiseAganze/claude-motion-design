#!/usr/bin/env python3
"""Host-made narration (e.g. ElevenLabs) -> per-frame clips + audio_meta.json voices with word timings.

The product-launch audio.mjs only generates HeyGen/Kokoro TTS; this replaces it when the voice comes
from a host connector. Reads production.json ("voice" key), finds speech segments with ffmpeg
silencedetect, maps one segment per sentence (count must match), cuts each frame's sentences out of
its take, pads lead/tail silence, and spreads words over each segment by character length.

usage: python3 -I vo.py <project_dir>
"""
import json, os, subprocess, sys

proj = sys.argv[1]
cfg = json.load(open(os.path.join(proj, "production.json")))["voice"]


def probe(path):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]))


def segments(path, db, dmin):
    log = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af", f"silencedetect=noise={db}dB:d={dmin}", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    marks = [float(l.split(": ")[1].split(" ")[0]) for l in log.splitlines() if "silence_start: " in l or "silence_end: " in l]
    total, segs, t = probe(path), [], 0.0
    for i in range(0, len(marks) - 1, 2):
        if marks[i] - t > 0.05: segs.append((t, marks[i]))
        t = marks[i + 1]
    if total - t > 0.1: segs.append((t, total))
    return segs


os.makedirs(os.path.join(proj, "assets/voice"), exist_ok=True)
voices = []
for take in cfg["takes"]:
    src = os.path.join(proj, take["file"])
    segs = segments(src, take.get("silence_db", -38), take.get("min_silence", 0.18))
    sents = take["sentences"]
    if len(segs) != len(sents):
        sys.exit(f"✗ {take['file']}: {len(segs)} speech segments for {len(sents)} sentences — tune silence_db/min_silence "
                 f"or merge sentences. segments: {[(round(a, 2), round(b, 2)) for a, b in segs]}")
    total = probe(src)
    for fr in take["frames"]:
        i0, i1 = fr["sentences"]; lead, tail = fr["lead"], fr["tail"]
        a = max(0.0, segs[i0][0] - 0.04); b = min(total, segs[i1][1] + 0.08)
        dur = round(lead + (b - a) + tail, 3)
        out = f"assets/voice/{fr['frame']:02d}.wav"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", str(a), "-to", str(b), "-i", src, "-af",
                        f"volume={take.get('gain_db', 0)}dB,adelay={int(lead * 1000)}:all=1,apad=whole_dur={dur},"
                        f"afade=t=in:d=0.02:st={lead},afade=t=out:d=0.05:st={lead + (b - a) - 0.05}",
                        "-ar", "44100", "-ac", "1", os.path.join(proj, out)], check=True)
        words = []
        for k in range(i0, i1 + 1):
            s0, s1 = segs[k]
            ws = sents[k].replace(" ?", "?").replace(" !", "!").split(" ")  # keep "?"/"!" on their word
            w8 = [len(w) + 2 for w in ws]; c = s0
            for w, n in zip(ws, w8):
                d = (s1 - s0) * n / sum(w8)
                text = (w[:-1] + " " + w[-1]) if w[-1] in "?!" and len(w) > 1 else w
                words.append({"text": text, "start": round(lead + c - a, 3), "end": round(lead + c + d - a, 3)}); c += d
        for i, w in enumerate(words): w["id"] = f"w{fr['frame']:02d}_{i}"
        voices.append({"frame": fr["frame"], "path": out, "duration_s": dur, "words": words})

meta_path = os.path.join(proj, "audio_meta.json")
meta = json.load(open(meta_path)) if os.path.exists(meta_path) else {}
meta.update({"bgm": meta.get("bgm"), "bgm_pending": False, "voices": sorted(voices, key=lambda v: v["frame"])})
meta.setdefault("sfx", [])
json.dump(meta, open(meta_path, "w"), ensure_ascii=False, indent=1)
print(f"✓ vo: {len(voices)} frame clip(s), total {round(sum(v['duration_s'] for v in voices), 2)}s")
