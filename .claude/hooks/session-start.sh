#!/bin/bash
# Installs HyperFrames CLI + headless Chrome in Claude Code cloud sessions.
set -euo pipefail
[ "${CLAUDE_CODE_REMOTE:-}" = "true" ] || exit 0
cd "$CLAUDE_PROJECT_DIR"
npm install --no-audit --no-fund
npx hyperframes browser ensure
# Node's fetch ignores HTTPS_PROXY unless told; the render compiler needs it to inline CDN scripts.
[ -n "${CLAUDE_ENV_FILE:-}" ] && echo 'export NODE_USE_ENV_PROXY=1' >> "$CLAUDE_ENV_FILE"
