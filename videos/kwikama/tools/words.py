#!/usr/bin/env python3
"""Print a frame's words in frame-local time: python3 -I tools/words.py F04"""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tl = json.load(open(os.path.join(ROOT, "timeline.json")))
f = next(x for x in tl["frames"] if x["id"] == sys.argv[1])
a, b = f["start"], f["start"] + f["duration"]
print(f"{f['id']} start {a} dur {f['duration']}")
print("  ".join(f"{w['w']}@{w['t'] - a:.2f}" for w in tl["words"] if a <= w["t"] < b))
