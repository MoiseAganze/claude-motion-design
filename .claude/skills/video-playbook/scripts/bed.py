"""Extend a music track to <total>s with one equal-power crossfade at the most similar point. usage: bed.py <src.mp3> <total_s> <out.mp3>"""
import sys, subprocess, numpy as np
src, total, out = sys.argv[1], float(sys.argv[2]), sys.argv[3]
sr = 11025
x = np.frombuffer(subprocess.check_output(["ffmpeg", "-v", "error", "-i", src, "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"]), dtype=np.float32)
L = len(x) / sr; shift = total - L; cf = 1.5
def spec(t, w=2.0):
    s = x[int(t*sr):int((t+w)*sr)]; S = np.abs(np.fft.rfft(s*np.hanning(len(s))))[:4000]; return S/(np.linalg.norm(S)+1e-9)
X = max(np.arange(max(shift+3, 20), L-12, 0.05), key=lambda X: spec(X-1)@spec(X-1-shift) + spec(X)@spec(X-shift))
Y = X - shift
f = f"[0:a]atrim=0:{X+cf/2:.3f},asetpts=PTS-STARTPTS[a];[0:a]atrim={Y-cf/2:.3f},asetpts=PTS-STARTPTS[b];[a][b]acrossfade=d={cf}:c1=qsin:c2=qsin,afade=t=in:d=0.3"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-filter_complex", f, "-ar", "44100", "-b:a", "192k", out], check=True)
print(f"bed: seam at {X:.2f}s -> {Y:.2f}s, {total}s")
