#!/usr/bin/env python3
"""Post-process compositions/captions.html after every `captions.mjs build` (it regenerates the file).

- moves the caption band (default sits at 83% = under the TikTok/Reels UI on 9:16)
- drops groups of frames whose on-screen type already says the VO (no double print)
- fixes the last kept group staying visible until the end of the video
- points @font-face at the "latin" woff2 (captions.mjs picks "latin-ext", which has no é/à/ç)
Config: production.json "captions": {"band_top": 1370, "band_height": 170, "hide_frames": [3, 9]}

usage: python3 -I captions_tune.py <project_dir>
"""
import json, os, re, sys

proj = sys.argv[1]
cfg = json.load(open(os.path.join(proj, "production.json"))).get("captions", {})
p = os.path.join(proj, "compositions/captions.html")
s = open(p).read()
if "band_top" in cfg: s = re.sub(r"--cap-band-top: \d+px;", f"--cap-band-top: {cfg['band_top']}px;", s)
if "band_height" in cfg: s = re.sub(r"--cap-band-height: \d+px;", f"--cap-band-height: {cfg['band_height']}px;", s)
s = s.replace("var end = isLast ? DURATION : Math.min(", "var end = isLast ? Number(group.end) + 0.3 : Math.min(")
s = re.sub(r"(\w+)-latin-ext\.woff2", r"\1-latin.woff2", s)
m = re.search(r"var GROUPS = (\[.*?\]);\n", s, re.S)
groups = [g for g in json.loads(m.group(1)) if g["frame"] not in set(cfg.get("hide_frames", []))]
s = s[:m.start(1)] + json.dumps(groups, ensure_ascii=False) + s[m.end(1):]
open(p, "w").write(s)
print(f"✓ captions tune: {len(groups)} group(s) kept")
