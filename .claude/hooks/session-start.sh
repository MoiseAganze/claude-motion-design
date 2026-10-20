#!/bin/bash
# Installs HyperFrames CLI + headless Chrome in Claude Code cloud sessions.
set -euo pipefail
[ "${CLAUDE_CODE_REMOTE:-}" = "true" ] || exit 0
cd "$CLAUDE_PROJECT_DIR"
npm install --no-audit --no-fund
npx hyperframes browser ensure
