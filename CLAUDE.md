# claude-motion-design

Video projects built with [HyperFrames](https://github.com/heygen-com/hyperframes) (HTML → MP4).

- Start any video request with the `/hyperframes` skill (router); all 21 skills live in `.agents/skills` (symlinked into `.claude/skills`).
- CLI: `npx hyperframes init <name>`, `lint`, `preview`, `render`. Run `npx hyperframes doctor` if something breaks.
- Cloud sessions: the SessionStart hook runs `npm install` + `npx hyperframes browser ensure`.
- If the network policy blocks CDNs (`cdn.jsdelivr.net`, …), render fails with `sub_timeline_script_failure`: vendor the lib from npm (`npm pack gsap@<ver>`, copy `dist/gsap.min.js` next to `index.html`) and point the `<script src>` at the local file.
- Refresh skills: `npx skills add heygen-com/hyperframes --all -a claude-code -y`.
