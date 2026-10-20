# claude-motion-design

Video projects built with [HyperFrames](https://github.com/heygen-com/hyperframes) (HTML → MP4).

- Start any video request with the `/hyperframes` skill (router); all 21 skills live in `.agents/skills` (symlinked into `.claude/skills`).
- CLI: `npx hyperframes init <name>`, `lint`, `preview`, `render`. Run `npx hyperframes doctor` if something breaks.
- Cloud sessions: the SessionStart hook runs `npm install` + `npx hyperframes browser ensure`.
- Cloud network: `cdn.jsdelivr.net` + `fonts.googleapis.com` are allowlisted; any other CDN must be added in the environment's Network access settings. `NODE_USE_ENV_PROXY=1` (set by the hook) lets the render compiler fetch through the proxy.
- Refresh skills: `npx skills add heygen-com/hyperframes --all -a claude-code -y`.
