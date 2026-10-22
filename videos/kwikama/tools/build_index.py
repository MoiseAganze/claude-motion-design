#!/usr/bin/env python3
"""timeline.json -> index.html: one sub-composition per frame + voice segments (+ music when present).

usage: python3 -I tools/build_index.py [--only F01,F02]   (draft of some frames, re-timed from 0)
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tl = json.load(open(os.path.join(ROOT, "timeline.json")))
only = None
if "--only" in sys.argv:
    only = sys.argv[sys.argv.index("--only") + 1].split(",")

srcs = {}
for f in sorted(os.listdir(os.path.join(ROOT, "compositions/frames"))):
    m = re.match(r"(\d\d)-.*\.html$", f)
    if m: srcs["F" + m.group(1)] = "compositions/frames/" + f

frames = [f for f in tl["frames"] if (only is None or f["id"] in only)]
shift = frames[0]["start"] if only else 0.0
end = frames[-1]["start"] + frames[-1]["duration"] - shift
X = 0.5  # crossfade overlap: each frame starts this much before the previous one ends

rows = []
for k, f in enumerate(frames):
    if f["id"] not in srcs: continue
    src = srcs[f["id"]]
    cid = "f" + os.path.basename(src)[:-5]
    start = f["start"] - shift
    dur = f["duration"] + (X if k + 1 < len(frames) else 0)
    rows.append(f'    <div id="{cid}" data-composition-id="{cid}" data-composition-src="{src}" data-start="{start:.3f}" '
                f'data-duration="{dur:.3f}" data-track-index="{k % 2}" data-width="1920" data-height="1080"></div>')

audio = []
for c in tl["vo"]:
    at = c["at"] - shift
    if at >= end or at + c["src_to"] - c["src_from"] <= 0: continue
    audio.append(f'    <audio id="vo-{c["frame"].lower()}" src="assets/voice/take-b.mp3" data-start="{at:.3f}" '
                 f'data-media-start="{c["src_from"]:.3f}" data-duration="{c["src_to"] - c["src_from"]:.3f}" data-track-index="10" data-volume="1"></audio>')

music = os.path.join(ROOT, "assets/music/bed.wav")
if os.path.exists(music):
    mvol = json.load(open(os.path.join(ROOT, "assets/music/bed.json")))
    audio.append(f'    <audio id="music-bed" src="assets/music/bed.wav" data-start="{mvol["at"] - shift:.3f}" '
                 f'data-media-start="{max(0.0, shift - mvol["at"]):.3f}" data-duration="{end - max(0.0, mvol["at"] - shift):.3f}" '
                 f'data-track-index="11" data-volume="{mvol["volume"]}"></audio>')

html = f"""<!doctype html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <script src="compositions/lib/kit.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1920px; height: 1080px; overflow: hidden; background: #052649; }}
      #root {{ position: relative; width: 100%; height: 100%; overflow: hidden; background: #052649; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{end:.3f}" data-width="1920" data-height="1080" data-fps="60">
{chr(10).join(rows)}
{chr(10).join(audio)}
    </div>
    <script>
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
"""
open(os.path.join(ROOT, "index.html"), "w").write(html)
print(f"index.html: {len(rows)} frames, {len(audio)} audio, {end:.2f}s")
