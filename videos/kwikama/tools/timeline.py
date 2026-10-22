#!/usr/bin/env python3
"""Voice take B word timings -> timeline.json: VO clip placement, frame windows, word times in video time.

usage: python3 -I tools/timeline.py            (writes timeline.json, prints the frame table)
       python3 -I tools/timeline.py cue F07 "Retenir"   (local time of a phrase inside a frame)
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = [w for w in json.load(open(os.path.join(ROOT, "assets/voice/take-b.words.json")))["words"] if w.get("type", "word") == "word" and w["text"] not in "?:"]
TAKE_END = 243.565

# frame id, first spoken words, silence inserted before this frame's voice (s)
FRAMES = [
    ("F01", "En République", None),
    ("F02", "L'UNICEP, l'Unité", None),
    ("F03", "L'APLC reçoit", 0.6),
    ("F04", "L'UNICEP est saisie par la", 0.8),
    ("F05", "Un dossier ne se", 0.8),
    ("F06", "Le dossier des redevances", 0.8),
    ("F07", "L'analyse assistée", 1.0),
    ("F08", "Quarante-huit heures pour notifier", 1.0),
    ("F09", "Avant toute transmission", 0.8),
    ("F10", "Identifier, geler", 0.8),
    ("F11", "Quickama est hébergée", 1.0),
]
F01_VO_AT = 2.0        # opening: 2 s of silence while the gold rule draws
F02_VO_AT = 23.4       # "L'UNICEP…" starts while the emblem resolves
F02_CUT_WORDS = "Quickama est son outil"  # F01 -> F02 crossfade lands on this phrase
LEAD = 0.6             # each later frame opens this long before its first word
END_HOLD = 3.0         # emblem hold after the last word
CREDITS = 8.0

norm = lambda s: s.lower().strip(".,;:!?—'’\"")


def find(phrase, after=0.0):
    toks = [norm(t) for t in phrase.split()]
    for i in range(len(W) - len(toks) + 1):
        if W[i]["start"] >= after - 1e-6 and all(norm(W[i + k]["text"]) == toks[k] for k in range(len(toks))):
            return i
    raise SystemExit(f"phrase not found: {phrase!r} after {after}")


starts = [find(p) for _, p, _ in FRAMES]
clips, offs = [], []
for k, (fid, _, breath) in enumerate(FRAMES):
    i0 = starts[k]
    i1 = (starts[k + 1] - 1) if k + 1 < len(FRAMES) else len(W) - 1
    a = max(0.0, W[i0]["start"] - 0.12) if k else 0.0
    b = min(W[i1]["end"] + 0.25, W[i1 + 1]["start"] - 0.05) if i1 + 1 < len(W) else TAKE_END
    if k == 0: off = F01_VO_AT
    elif k == 1: off = F02_VO_AT - W[i0]["start"]
    else: off = offs[-1] + breath
    offs.append(off)
    clips.append({"frame": fid, "src_from": round(a, 3), "src_to": round(b, 3), "at": round(a + off, 3)})

fstart = [0.0, round(W[find(F02_CUT_WORDS)]["start"] + offs[1] - 0.5, 3)]
for k in range(2, len(FRAMES)):
    fstart.append(round(W[starts[k]]["start"] + offs[k] - LEAD, 3))
last_end = W[-1]["end"] + offs[-1]
end11 = round(last_end + END_HOLD, 3)
frames = []
for k, (fid, _, _) in enumerate(FRAMES):
    end = fstart[k + 1] if k + 1 < len(FRAMES) else end11
    frames.append({"id": fid, "start": fstart[k], "duration": round(end - fstart[k], 3)})
frames.append({"id": "F12", "start": end11, "duration": CREDITS})
total = round(end11 + CREDITS, 3)

# every word in video time
words, k = [], 0
for i, w in enumerate(W):
    while k + 1 < len(FRAMES) and i >= starts[k + 1]: k += 1
    words.append({"t": round(w["start"] + offs[k], 3), "e": round(w["end"] + offs[k], 3), "w": w["text"]})

out = {"total": total, "frames": frames, "vo": clips, "words": words}
json.dump(out, open(os.path.join(ROOT, "timeline.json"), "w"), ensure_ascii=False, indent=1)

if len(sys.argv) > 1 and sys.argv[1] == "cue":
    f = next(x for x in frames if x["id"] == sys.argv[2])
    toks = [norm(t) for t in sys.argv[3].split()]
    for i in range(len(words) - len(toks) + 1):
        if words[i]["t"] >= f["start"] and all(norm(words[i + j]["w"]) == toks[j] for j in range(len(toks))):
            print(round(words[i]["t"] - f["start"], 3)); break
    else: sys.exit("cue not found")
else:
    for f in frames: print(f"{f['id']}  {f['start']:7.2f} → {f['start'] + f['duration']:7.2f}  ({f['duration']:.2f}s)")
    for c in clips: print(f"  VO {c['frame']}: take {c['src_from']:.2f}–{c['src_to']:.2f} @ {c['at']:.2f}")
    print("total", total, f"({int(total // 60)}:{total % 60:04.1f})")
