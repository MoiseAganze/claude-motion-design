#!/usr/bin/env python3
"""Loop a short music track to any length with seams the ear can't find.

The jump always lands a whole number of 16-bar phrases back, on the beat grid, where the music sounds most
like the point it leaves; the two copies cross over 2 bars with an equal-power fade.

usage: python3 -I tools/music_loop.py <track.mp3> --length 246 [--bpm 128] [--out assets/music/bed.wav]
       python3 -I tools/music_loop.py --selftest
"""
import argparse, json, os, subprocess, sys
import numpy as np

SR = 44100
HOP = 441  # 10 ms


def decode(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-f", "f32le", "-ac", "2", "-ar", str(SR), "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).reshape(-1, 2).copy()


def bands(x):
    """10 ms frames → (log band energies [n, 12], low-band onset envelope [n])."""
    mono = x.mean(axis=1)
    n = (len(mono) - 2048) // HOP
    idx = np.arange(2048)[None, :] + HOP * np.arange(n)[:, None]
    spec = np.abs(np.fft.rfft(mono[idx] * np.hanning(2048), axis=1)) ** 2
    freqs = np.fft.rfftfreq(2048, 1 / SR)
    edges = np.geomspace(40, 16000, 13)
    E = np.stack([spec[:, (freqs >= a) & (freqs < b)].sum(axis=1) for a, b in zip(edges[:-1], edges[1:])], axis=1)
    low = np.log1p(spec[:, (freqs >= 35) & (freqs < 160)].sum(axis=1))
    onset = np.maximum(np.diff(low, prepend=low[0]), 0)
    return np.log1p(E), onset


def beat_grid(onset, bpm):
    """Refine the tempo near `bpm`, then the phase: the offset whose beat positions collect the most kick energy."""
    best = None
    for b in np.arange(bpm - 1.0, bpm + 1.0001, 0.02):
        period = 6000.0 / b  # frames per beat
        for ph in np.arange(0, period, 1.0):
            pos = np.round(ph + period * np.arange(int((len(onset) - ph) / period))).astype(int)
            sc = onset[pos].sum()
            if best is None or sc > best[0]: best = (sc, b, ph)
    _, b, ph = best
    return b, (ph * HOP + 1024) / SR  # tempo, first beat (s), frames dated at their window centre


def choose_seam(E, bpm, t0, dur, xfade_bars=2):
    beat = 60.0 / bpm
    bar = 4 * beat
    phrase = 16 * bar
    half = xfade_bars * bar / 2
    frames = lambda s: int(round(s * SR / HOP))
    win = frames(half)
    best = None
    a = t0 + 4 * bar  # leave the first bars of the intro alone
    while a + phrase * 2 + half < dur:
        for n in range(2, 8):
            b = a + n * phrase
            if b + half > dur - 2 * bar: break
            A, B = E[frames(a - half): frames(a - half) + 2 * win], E[frames(b - half): frames(b - half) + 2 * win]
            if len(A) != len(B) or len(A) == 0: continue
            d = np.mean((A - B) ** 2)
            score = d - 0.002 * (b - a)  # prefer long loops on ties
            if best is None or score < best[0]: best = (score, a, b, d)
        a += bar
    if best is None: raise SystemExit("track too short to loop on 16-bar phrases")
    return best[1], best[2], half, best[3]


def render(x, L0, L1, half, length, fade_out=6.0):
    """Play from 0 to L1, jump back to L0, repeat; equal-power crossfade of 2·half centred on each seam."""
    s = lambda t: int(round(t * SR))
    out = np.zeros((s(length), 2), dtype=np.float32)
    n_x = s(2 * half)
    th = np.linspace(0, np.pi / 2, n_x, dtype=np.float32)[:, None]
    fo, fi = np.cos(th), np.sin(th)
    seams, pos, src = [], 0, 0  # pos: write head in out, src: read head in x
    seg_end = s(L1 - half)
    while pos < len(out):
        take = min(seg_end - src, len(out) - pos)
        out[pos:pos + take] += x[src:src + take]
        pos += take
        if pos >= len(out): break
        tail = x[seg_end:seg_end + n_x]
        head = x[s(L0 - half):s(L0 - half) + n_x]
        m = min(len(tail), len(head), len(out) - pos)
        out[pos:pos + m] += tail[:m] * fo[:m] + head[:m] * fi[:m]
        seams.append(pos / SR + half)
        pos += m
        src = s(L0 - half) + m
    nf = s(fade_out)
    out[-nf:] *= np.linspace(1, 0, nf, dtype=np.float32)[:, None] ** 2
    return out, seams


def write_wav(path, y):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", "pcm_s16le", path], input=y.astype(np.float32).tobytes(), check=True)


def selftest():
    # synthetic 128 BPM track: kick on every beat, hat on off-beats, a pitch that changes per 16-bar phrase
    bpm, beat = 128.0, 60 / 128.0
    t = np.arange(int(SR * 118)) / SR
    y = np.zeros_like(t)
    for k in range(int(118 / beat)):
        i = int((0.37 + k * beat) * SR)
        n = min(4000, len(y) - i)
        if n > 0: y[i:i + n] += np.sin(2 * np.pi * 55 * np.arange(n) / SR) * np.exp(-np.arange(n) / 900)
    y += 0.05 * np.sin(2 * np.pi * (220 + 20 * ((t // (16 * 4 * beat)) % 2)) * t)
    x = np.stack([y, y], axis=1).astype(np.float32)
    E, onset = bands(x)
    b, ph = beat_grid(onset, bpm)
    assert abs(b - 128) < 0.1, b
    assert abs(((ph - 0.37 + beat / 2) % beat) - beat / 2) < 0.03, ph
    L0, L1, half, d = choose_seam(E, b, ph, len(x) / SR)
    k = (L1 - L0) / (16 * 4 * 60 / b)
    assert abs(k - round(k)) < 1e-6 and round(k) >= 2, k
    out, seams = render(x, L0, L1, half, 246)
    assert len(out) == int(round(246 * SR)) and len(seams) >= 2
    # across every seam the kicks keep landing on the grid: onsets of the output stay a whole number of beats apart
    _, on2 = bands(out)
    peaks = np.where((on2 > on2.max() * 0.3) & (on2 >= np.roll(on2, 1)) & (on2 >= np.roll(on2, -1)))[0] * HOP / SR
    gaps = np.diff(peaks[peaks < 240])
    err = np.abs(gaps / beat - np.round(gaps / beat))
    assert err.max() < 0.06, err.max()
    print(f"✓ selftest: bpm {b:.2f}, seam {L0:.2f}s ← {L1:.2f}s, {len(seams)} seams, max off-grid {err.max():.3f} beat")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("track", nargs="?")
    ap.add_argument("--length", type=float)
    ap.add_argument("--bpm", type=float, default=128)
    ap.add_argument("--out", default="assets/music/bed.wav")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest: selftest(); sys.exit()
    x = decode(a.track)
    E, onset = bands(x)
    bpm, t0 = beat_grid(onset, a.bpm)
    L0, L1, half, d = choose_seam(E, bpm, t0, len(x) / SR)
    out, seams = render(x, L0, L1, half, a.length)
    write_wav(a.out, out)
    info = {"source": os.path.basename(a.track), "bpm": round(bpm, 3), "first_beat": round(t0, 3), "loop_from": round(L1, 3), "loop_to": round(L0, 3),
            "phrases_per_loop": round((L1 - L0) / (64 * 60 / bpm)), "xfade_s": round(2 * half, 3), "seams_at": [round(s, 2) for s in seams], "length": a.length, "seam_distance": round(float(d), 4)}
    print(json.dumps(info, indent=1))
    json.dump(info, open(os.path.splitext(a.out)[0] + ".loop.json", "w"), indent=1)
