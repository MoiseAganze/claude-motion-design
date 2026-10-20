---
format: 1080x1920
duration: 50s
message: "Vos courriers se traitent tout seuls."
arc: Hook → Problem → Turn → Demo (détecter · lire · comprendre · agir · trier) → Benefits → Brand_Outro
audience: organisations qui reçoivent beaucoup de courriers par mail
mode: autonomous
music: none
---

## Video direction

- **Palette (frame.md, dark override):** canvas `#070B18` deep night on every frame; surfaces `#0E1430` with 7% blue tint + 20% blue border; ink `#F4F6FB`; muted `#9AA3B8`. Electric blue `#3D7BFF` = THE accent (agent, scan beam, glow, data). Violet `#7C5CFF` only mixed into blue glows. Mint `#38E1A6` = success only (✓, "Enregistré", accusé). Red-pink `#FF5C7A` only for the pain beats (overflow counter, "à la main").
- **Type:** display/numerals/chrome = Space Grotesk 700 (tight, -0.02em); body/UI = Inter. 9:16 means BIG: hero words ≥ 120px, UI text ≥ 30px.
- **One hero object:** the same courrier (a PDF letter, "Demande de partenariat — Société Lumen") travels through frames 4→7: same document art, same subject line, same sender. Continuity sells the demo.
- **Motion grammar:** smooth long-tail settles (`power3` / `expo.out` for fast arrivals); no bounce; reveals cued to the VO, nothing front-loaded; held reads stay still (subtle jitter at most). Depth via soft blue bloom (`ambient-glow-bloom`) and depth-of-field blur, never hard shadows. Seams inside frames are velocity-matched (cut-catalog).
- **Rhythm:** frames 1–2 fast and cluttered (pain), frame 3 a held breath (black + one line), frames 4–8 the demo at a steady confident pace, frame 9 rapid-fire slams, frame 10 slow premium landing. Held/breather frames: 3 and 10.
- **Layout:** 1080×1920; all content in the top ~75% (TikTok UI + captions own the bottom band and the right ~120px edge); hero element ≥ 40% of canvas; ≥ 3 depth layers.
- **SFX (no music):** whoosh on pushes, soft impact on slams, mail "ding" on arrival, scanner hum on OCR, paper/stamp on registration, notification chime on the accusé, soft riser into the logo.
- **Negative list:** no stock photos, no ministry/organisation names, no CTA/phone/URL, no bouncy overshoot, no infinite loops, no randomness, no slideshow (front-load-then-freeze), no screensaver (everything floating), no purple "AI blob" backgrounds.

## Frame 1 — L'avalanche

- scene: Des enveloppes tombent en cascade et remplissent l'écran pendant qu'un compteur s'emballe
- voiceover: "Des centaines de courriers par mois…"
- duration: 3.331s
- transition_in: cut
- status: animated
- src: compositions/frames/01-avalanche.html
- type: hook
- persuasion: Pain agitation
- beat: overwhelm
- blueprint: dataviz-countup (Adapt)
- focal: count-up number
- roles: envelopes = supporting (falling layers, 3 depths) · counter = cutout hero
- asset_candidates:
- sfx: whoosh-cinematic, impact-bass-1

narrativeRole: open on the pain in the first second — volume.
keyMessage: il y en a beaucoup trop.

Adapt: keep the exploding-statistic count-up signature; the "chart" is a pile of envelope cards accumulating.
Scene 1 (0.0–0.8s): black canvas; first envelope cards (flat vector, ink-on-surface, a few with red "!" priority dot) drop from the top on three depth layers (far ones small + blurred), accelerating — layered-depth.
Scene 2 (0.8–2.2s): as the VO says "des centaines", a giant counter in Space Grotesk 700 lands upper-center and counts 12 → 247 (`counting-dynamic-scale`), the font growing with the value; envelopes keep piling at the bottom, the stack rising toward the counter.
Scene 3 (2.2–3.0s): "courriers / mois" label snaps under the number; the envelope pile has filled ~60% of the frame; hold with subtle jitter on the counter.

## Frame 2 — À la main

- scene: LIRE · TRIER · SAISIR · RÉPONDRE claquent un par un comme des tampons, puis « À la main. Chaque jour. »
- voiceover: "À lire, trier, saisir, répondre. À la main. Chaque jour."
- duration: 6.486s
- transition_in: crossfade
- status: animated
- src: compositions/frames/02-a-la-main.html
- type: pain_point
- persuasion: Rule of three (+1) — repetitive chores stacked
- beat: frustration
- blueprint: kinetic-type-beats (Reproduce)
- focal: the four chore words
- roles: chore words = cutout · clock = supporting · faint envelope pile = background (dim ~30%)
- asset_candidates:
- sfx: impact-bass-2, click

narrativeRole: name the manual chores — the pain is repetition.
keyMessage: c'est répétitif, manuel, sans fin.

Scene 1 (0.0–2.4s): the frame-1 envelope pile blurred and dimmed in the back; each chore word slams in centered on its spoken cue with a stamp-like scale-down impact (`kinetic-beat-slam`) — LIRE, TRIER, SAISIR, RÉPONDRE — each new one pushing the previous up into a tight stack (left-aligned column, ~70% width).
Scene 2 (2.4–3.8s): on "À la main", a red-pink rubber-stamp outline "À LA MAIN" stamps diagonally across the stack (stamp impact, scale-down + slight rotation settle).
Scene 3 (3.8–5.0s): on "Chaque jour", a minimal clock face upper-right spins its hands fast (finite tween on the SVG hands) and a day counter flips LUN → MAR → MER → JEU → VEN (`discrete-text-sequence`); hold.

## Frame 3 — Et si…

- scene: Tout se fige, glitch, l'écran se vide ; une seule question lumineuse sur fond nuit
- voiceover: "Et si vos courriers se traitaient tout seuls ?"
- duration: 3.91s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/03-et-si.html
- type: product_intro
- persuasion: Curiosity gap / pattern interrupt
- beat: curiosity → relief
- blueprint: kinetic-type-beats (Adapt)
- focal: the question line
- roles: question = cutout · blue bloom = background
- asset_candidates:
- sfx: glitch-1, sparkle

narrativeRole: the turn — break the pain pattern, tease the promise.
keyMessage: ça peut se faire tout seul.

Adapt: one statement built word-by-word onto a payoff word, instead of token swaps.
Scene 1 (0.0–0.4s): a short RGB-split glitch shard on the incoming dark canvas, then silence-dark.
Scene 2 (0.4–2.6s): "Et si vos courriers" reveals per word (`dynamic-content-sequencing`) centered, ink white, big; "se traitaient" follows; "tout seuls ?" lands last in electric blue with a soft blue bloom opening behind it.
Scene 3 (2.6–3.5s): held read, perfectly still — the breather before the demo.

## Frame 4 — Un mail arrive

- scene: Une boîte mail flottante en 3D ; un mail avec PDF arrive, une onde radar pulse, l'horloge affiche 03:12
- voiceover: "Un mail arrive. L'agent le détecte aussitôt. Même à trois heures du matin."
- duration: 5.73s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/04-reception.html
- type: feature_showcase
- persuasion: Show-don't-tell proof
- beat: intrigue → confidence
- blueprint: device-surface-showcase (Adapt)
- focal: inbox card with the new mail row
- roles: inbox window = cutout hero · radar rings = supporting · night clock = supporting
- asset_candidates:
- sfx: notification, ping

narrativeRole: first demo step — detection, 24/7.
keyMessage: rien n'échappe à l'agent, même la nuit.

Adapt: floating-window variant — one inbox window (no device bezel), slightly tilted in 3D, lit by the blue glow.
Scene 1 (0.0–1.6s): a dark glass inbox window tilts into frame (rotateX ~12°, settles flat-ish) occupying ~80% width; two greyed old rows; on "Un mail arrive" a NEW row slides in at the top — sender "Société Lumen", subject "Demande de partenariat", 📎 courrier.pdf chip — with a blue unread dot.
Scene 2 (1.6–3.4s): on "l'agent le détecte", concentric radar rings pulse out from the row (3 rings, staggered, finite) and an "Agent Courrier" chip with a small blue core icon lights up: "Courrier détecté" ✓.
Scene 3 (3.4–5.5s): on "trois heures du matin", a large night clock "03:12" (Space Grotesk, tabular nums) fades in top-center with a small moon glyph, the window dims slightly (depth-of-field) — hold.

## Frame 5 — Il lit

- scene: Zoom dans le PDF scanné, un laser bleu balaie la page, le texte flou devient net et surligné ligne par ligne
- voiceover: "Il lit la pièce jointe. Même un document scanné."
- duration: 4.404s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/05-lecture.html
- type: feature_showcase
- persuasion: Show-don't-tell proof
- beat: awe
- blueprint: agent-progress-theater (Adapt)
- focal: scanned letter page
- roles: letter page = cutout hero · scan beam = supporting · OCR text boxes = supporting
- asset_candidates:
- sfx: typing

narrativeRole: OCR — even messy scans.
keyMessage: il lit vraiment le contenu.

Adapt: the "working-state theater" is the scan itself; the receipt is the text lighting up.
Scene 1 (0.0–1.2s): the courrier.pdf page fills ~85% of height, slightly rotated (-2°), paper-grey with scanner noise, its text lines rendered as blurred grey bars (unreadable); a status pill "Lecture OCR…" top.
Scene 2 (1.2–3.2s): a horizontal electric-blue laser beam sweeps top→bottom; above the beam the lines turn sharp, readable (real letter text) and get thin blue bounding boxes, line by line (`dynamic-content-sequencing`); on "même un document scanné" the page straightens to 0° as it is read.
Scene 3 (3.2–4.0s): pill flips to "Texte extrait ✓" (mint); hold.

## Frame 6 — Il comprend

- scene: Les mots-clés s'arrachent du document et volent former une fiche : Objet, Expéditeur, Date, Priorité HAUTE
- voiceover: "Il comprend le courrier, et en extrait l'essentiel."
- duration: 4.812s
- transition_in: cut
- status: animated
- src: compositions/frames/06-comprehension.html
- type: feature_showcase
- persuasion: Feature-to-benefit translation
- beat: clarity
- blueprint: compose
- focal: extraction card
- roles: letter page = background (dimmed, top) · flying keyword chips = supporting · extraction card = cutout hero
- asset_candidates:
- sfx: whoosh-short, pop

narrativeRole: AI understanding → structured data.
keyMessage: il en tire exactement ce qu'il faut.

Compose: continuous from frame 5 (same page, same position at t=0 → handoff), then a card-build.
Scene 1 (0.0–1.0s): the read page (frame-5 end state) shrinks up into the upper third and dims; four highlighted phrases on it glow blue (`asr-keyword-glow`) on "Il comprend le courrier".
Scene 2 (1.0–3.4s): on "en extrait l'essentiel", each highlighted phrase detaches as a chip and flies along a curved path down into an empty card (directional blur while in flight), landing in its row one after another: Objet « Demande de partenariat » · Expéditeur « Société Lumen » · Date « 14/10 » · Priorité « HAUTE » (blue pill).
Scene 3 (3.4–4.5s): a badge "Courrier identifié ✓" spring-settles on the card corner (mint, smooth, no bounce); card glow blooms; hold.

## Frame 7 — Il agit

- scene: La fiche se range dans le registre, un accusé part en traînée lumineuse vers un téléphone qui vibre ; chrono 8 s
- voiceover: "Il l'enregistre. Et l'expéditeur reçoit son accusé de réception. En quelques secondes."
- duration: 6.629s
- transition_in: crossfade
- status: animated
- src: compositions/frames/07-action.html
- type: feature_showcase
- persuasion: Show-don't-tell proof + speed
- beat: control → satisfaction
- blueprint: camera-journey (Adapt)
- focal: phone notification
- roles: register table = supporting · flying envelope = supporting · phone = cutout hero · stopwatch = supporting
- asset_candidates:
- sfx: click-soft, whoosh, chime

narrativeRole: the payoff of the demo — registered + acknowledged.
keyMessage: c'est fait, et l'expéditeur le sait.

Adapt: action-roundtrip sub-shape (A) — the fire is the registration; the camera travels down to the consequence on the phone.
Scene 1 (0.0–2.0s): the extraction card (handoff from frame 6) slides into the top row of a register table "Registre des courriers" (N° 2026-0417 · Lumen · Partenariat · Haute · ✓ Enregistré mint); a mint "ENREGISTRÉ" stamp prints on the row on "Il l'enregistre".
Scene 2 (2.0–4.2s): on "l'expéditeur reçoit", a small envelope with a blue light trail launches from the row and the camera pans DOWN with it (`viewport-change`) to a phone (rounded glass mockup, no brand) lower-center; the envelope dives into it.
Scene 3 (4.2–6.5s): the phone lights up and nudges (a small finite shake = vibration); a notification card drops in: "Accusé de réception — Votre courrier a bien été reçu et enregistré." On "en quelques secondes", a stopwatch chip next to the phone stops at "00:08"; hold.

## Frame 8 — Il trie

- scene: Le flux de mails se divise en trois voies : enregistré, transmis à un humain, publicité ignorée
- voiceover: "Un doute ? Il vous le transmet. Une pub ? Il l'ignore."
- duration: 4.977s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/08-tri.html
- type: feature_showcase
- persuasion: Risk reversal (l'humain garde la main)
- beat: trust
- blueprint: compose
- focal: the three-way split
- roles: incoming mail chips = supporting · three destination nodes = cutout · connector lines = supporting
- asset_candidates:
- sfx: whoosh-short, error

narrativeRole: show judgment + safety — humans keep control, spam disappears.
keyMessage: il sait quand vous demander, et quoi ignorer.

Scene 1 (0.0–0.8s): central agent core (blue glowing node) top-center; a line drops from it and splits into three SVG paths drawn with `svg-path-draw` toward three nodes at the bottom area (left/center/right, upper 75% of canvas): ✓ Registre (mint) already lit.
Scene 2 (0.8–2.4s): on "Un doute ?", a mail chip with a "?" travels down the center path to a node "👤 Équipe — à valider" (blue) which lights with a soft pulse; label "Transmis avec le document".
Scene 3 (2.4–4.5s): on "Une pub ?", a chip labelled "PROMO -50 %" travels right, hits the node "Ignoré", greys out and dissolves into particles of fixed positions (deterministic) / fades down; hold on the three lit nodes.

## Frame 9 — Zéro

- scene: Trois énoncés géants claquent en coupes rapides : ZÉRO SAISIE · ZÉRO OUBLI · TOUT EST TRACÉ
- voiceover: "Zéro saisie. Zéro oubli. Tout est tracé."
- duration: 4.028s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/09-benefices.html
- type: benefit_highlight
- persuasion: Rule of three
- beat: confidence
- blueprint: kinetic-type-beats (Reproduce)
- focal: the three statements
- roles: statements = cutout · small 24/7 chip = supporting
- asset_candidates:
- sfx: impact-bass-1, impact-bass-2

narrativeRole: compress the value into three memorable slams.
keyMessage: zéro travail manuel, zéro perte.

Scene 1 (0.0–1.1s): "ZÉRO" huge (blue) stays pinned; "SAISIE" slams under it on its cue (`kinetic-beat-slam`).
Scene 2 (1.1–2.2s): in-place token swap (`discrete-text-sequence`): "SAISIE" → "OUBLI" on a hard cut with a micro zoom punch.
Scene 3 (2.2–3.5s): the whole block cuts to "TOUT EST TRACÉ" with a thin journal-log line list (timestamps 03:12:04 · détecté / lu / enregistré / accusé envoyé) typing in beneath in muted mono; chip "24h/24 · 7j/7" settles at the top; hold.

## Frame 10 — Agent Courrier

- scene: Une enveloppe se pose au centre, se plie et devient le logo Agent Courrier ; le slogan s'écrit ; fondu premium
- voiceover: "Agent Courrier. Vos courriers se traitent tout seuls."
- duration: 6.552s
- transition_in: crossfade
- status: animated
- src: compositions/frames/10-outro.html
- type: branding
- persuasion: Brand recall
- beat: peace of mind
- blueprint: logo-assemble-lockup (Adapt)
- focal: logo lockup
- roles: logo mark = cutout hero · wordmark = cutout · slogan = supporting · bloom = background
- asset_candidates:
- sfx: whoosh-cinematic, sparkle

narrativeRole: brand lockup and promise; smooth ending.
keyMessage: Agent Courrier = vos courriers se traitent tout seuls.

Adapt: morph-from-object variant — the envelope itself becomes the mark (an envelope outline whose flap is an upward chevron/spark = "automatique").
Scene 1 (0.0–1.4s): a single envelope glides in from below and settles center; its outline redraws as the mark (`svg-path-draw`) while a blue/violet bloom opens behind (`ambient-glow-bloom`).
Scene 2 (1.4–2.8s): on "Agent Courrier", the wordmark reveals letter-cascade under the mark (Space Grotesk 700, ink white, "Courrier" in blue).
Scene 3 (2.8–4.4s): on "Vos courriers se traitent tout seuls.", the slogan reveals per word beneath in Inter, muted→white.
Scene 4 (4.4–5.0s): smooth ending — the bloom gently contracts and the whole lockup eases to the canvas color (final frame exit; no hard cut).
