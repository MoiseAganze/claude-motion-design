#!/usr/bin/env python3
"""Place bundled HyperFrames SFX on word cues and write audio_meta.json "sfx" (voices untouched).

Replaces `audio.mjs fetch-sfx`, which needs Openverse (blocked in the cloud), puts every cue at
offset 0 and overwrites host voices. Cues live in production.json "sfx":
  {"gain": 0.75, "cues": [[frame, "name", anchor, delta, volume], ...]}
anchor = a word prefix ("arrive", "zéro#1" for the 2nd match), a number (seconds), or "end".
Names are keys of media-use/audio/assets/sfx/manifest.json; files are copied into assets/sfx/.

usage: python3 -I sfx.py <project_dir>
"""
import json, os, shutil, sys

proj = sys.argv[1]
lib = os.path.join(os.path.dirname(__file__), "../../media-use/audio/assets/sfx")
manifest = json.load(open(os.path.join(lib, "manifest.json")))
cfg = json.load(open(os.path.join(proj, "production.json")))["sfx"]
meta_path = os.path.join(proj, "audio_meta.json")
meta = json.load(open(meta_path))
voice = {v["frame"]: v for v in meta["voices"]}


def at(frame, anchor):
    if isinstance(anchor, (int, float)): return float(anchor)
    if anchor == "end": return voice[frame]["duration_s"]
    word, _, nth = anchor.partition("#")
    hits = [w for w in voice[frame]["words"] if w["text"].lower().strip(".,?!… ").startswith(word.lower())]
    if len(hits) <= int(nth or 0): sys.exit(f"✗ sfx: no word '{anchor}' in frame {frame}")
    return hits[int(nth or 0)]["start"]


os.makedirs(os.path.join(proj, "assets/sfx"), exist_ok=True)
out = []
for frame, name, anchor, delta, vol in cfg["cues"]:
    if name not in manifest: sys.exit(f"✗ sfx: '{name}' not in bundled library: {sorted(manifest)}")
    f = manifest[name]["file"]
    shutil.copy(os.path.join(lib, f), os.path.join(proj, "assets/sfx", f))
    o = max(0.0, at(frame, anchor) + delta)
    out.append({"frame": frame, "file": f"assets/sfx/{f}", "offset_s": round(o, 3),
                "duration_s": min(manifest[name]["duration"], round(voice[frame]["duration_s"] - o + 1.0, 3)),
                "volume": round(vol * cfg.get("gain", 1.0), 3)})
meta["sfx"] = out
json.dump(meta, open(meta_path, "w"), ensure_ascii=False, indent=1)
print(f"✓ sfx: {len(out)} cue(s)")
