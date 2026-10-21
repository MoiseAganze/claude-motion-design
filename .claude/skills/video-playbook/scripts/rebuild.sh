#!/bin/bash
# Rebuild a product-launch project after ANY change to voice, sfx, durations, frames or captions.
# Order matters: assemble rewrites index.html (transitions must be re-injected) and captions.mjs
# rewrites captions.html (must be re-tuned). Never run `audio.mjs fetch-sfx` (overwrites voices).
# usage: rebuild.sh <project_dir> [--no-vo]
set -euo pipefail
DIR="$(cd "$1" && pwd)"; HERE="$(cd "$(dirname "$0")" && pwd)"
PL="$HERE/../../product-launch-video/scripts"
quiet() { "$@" 2>&1 | grep -v -E "EHPA|trace-warnings" || true; }
cd "$DIR"
[ "${2:-}" = "--no-vo" ] || python3 -I "$HERE/vo.py" .
quiet node "$PL/audio.mjs" sync-durations --audio-meta ./audio_meta.json --storyboard ./STORYBOARD.md
python3 -I "$HERE/sfx.py" .
quiet node "$PL/captions.mjs" build --storyboard ./STORYBOARD.md --audio-meta ./audio_meta.json --hyperframes . --out ./caption_groups.json
python3 -I "$HERE/captions_tune.py" .
quiet node "$PL/assemble-index.mjs" --storyboard ./STORYBOARD.md --hyperframes . | grep -E "✓|total duration|warn|✗" || true
quiet node "$PL/transitions.mjs" inject --storyboard ./STORYBOARD.md --hyperframes . | grep -E "✓|✗" || true
quiet node "$PL/transitions.mjs" verify --storyboard ./STORYBOARD.md --index ./index.html
# music bed under the voice → group the narration clips and carve the bed (assemble drops both)
if grep -q 'id="el-bgm"' index.html && grep -q -- '-voice"' index.html; then
  sed -i -E 's/(id="el-[0-9]{2}-[a-z0-9-]+-voice")( data-audio-group="voiceover")?/\1 data-audio-group="voiceover"/' index.html
  quiet node "$HERE/../../hyperframes-audio/scripts/carve.mjs" --comp ./index.html | grep -E "^carve|^wrote|rror" || true
fi
npx hyperframes check --json 2>/dev/null | python3 -c "
import json,sys; d=json.load(sys.stdin); errs=[]
def w(o):
    if isinstance(o,dict):
        if o.get('severity')=='error': errs.append((o.get('code'),o.get('time'),(o.get('selector') or '')[:60]))
        [w(v) for v in o.values()]
    elif isinstance(o,list): [w(v) for v in o]
w(d); [print('  ✗',*e) for e in errs]; print('✓ check ok' if d.get('ok') else '✗ check failed'); sys.exit(0 if d.get('ok') else 1)"
