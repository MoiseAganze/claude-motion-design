---
format: 1080x1920
duration: 77s
message: "Un abus à l'université ? Signalez-le, en toute sécurité : le Ministère agit."
arc: Hook → Problem → Silence → Reveal → Demo citoyen (accueil · catégories · étapes · anonymat · suivi) → Côté agent (tableau de bord · carte) → Promesse → CTA
audience: étudiants, enseignants, personnel et citoyens de l'enseignement supérieur en RDC
mode: autonomous
music: none
---

## Video direction

- **Palette (frame.md, brand override):** canvas `#001B3D` navy on every frame with a soft `#007FFF` bloom; surfaces `#002654`. Blue `#007FFF` = accent (data, map, focus). Yellow `#F7D117` = action only (CTA buttons, selected item ring, Kinshasa border). Red `#CE1126` = problem beats only (frames 1–2, "Critique"). RDC flag stripe (10px) on top of every frame, like the site.
- **Type:** titles Cormorant Garamond 700 (site display serif); slams / UI / numbers Source Sans 3 700. Hero words ≥ 110px.
- **Hero objects:** the real site in a phone (frames 5–6, same phone position), the real dashboard (frame 10) and the real province map (frame 11, native SVG from the captured Leaflet layer). Steps 2–8 of the form are recreated with the site's exact labels (the real form was not filled).
- **Motion grammar:** confident `power3`/`expo.out` arrivals, no bounce, reveals cued to the VO; slow camera drift on screens; flag-stripe wipe as the brand transition.
- **Layout:** 1080×1920; key content y 150–1330, captions band 1370–1540, keep x ≤ 990.
- **SFX (no music):** soft impacts on the abuse slams, whoosh on reveals, taps/clicks in the demo, chime on the reference, sparkle on the map Kinshasa hit, riser into the slogan.
- **Privacy:** never show the "Derniers signalements" table, the institution ranking chart, or the logged-in agent's name.

## Frame 1 — Un abus ?

- scene: La bannière de campagne (étudiante) assombrie, « Un abus dans votre université ? » claque par-dessus
- voiceover: "Un abus dans votre université ?"
- duration: 2.34s
- transition_in: cut
- status: animated
- src: compositions/frames/01-hook.html
- type: hook
- asset_candidates: assets/img/abus.jpg
- sfx: whoosh-cinematic, impact-bass-1

## Frame 2 — Les abus

- scene: Quatre slams rouges : POINTS VENDUS · FRAIS ILLÉGAUX · FAUX DIPLÔMES · HARCÈLEMENT
- voiceover: "Des points qui se vendent. Des frais illégaux. De faux diplômes. Du harcèlement."
- duration: 5.819s
- transition_in: cut
- status: animated
- src: compositions/frames/02-abus.html
- type: pain_point
- asset_candidates: none (typographie)
- sfx: impact-bass-1, impact-bass-2

## Frame 3 — Le silence

- scene: Les mots s'éteignent, « Trop souvent, on se tait. » puis « Par peur, ou faute de savoir à qui parler. », un point bleu naît
- voiceover: "Trop souvent, on se tait. Par peur, ou faute de savoir à qui parler."
- duration: 5.427s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/03-silence.html
- type: tension
- asset_candidates: none
- sfx: glitch-1

## Frame 4 — La plateforme

- scene: Le point devient le sceau RDC, « ESURSI — Signalement national », puis la bannière officielle
- voiceover: "Voici la plateforme nationale de signalement du Ministère de l'Enseignement Supérieur."
- duration: 5.777s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/04-revelation.html
- type: reveal
- asset_candidates: assets/img/logo_rdc.png, assets/img/abus.jpg
- sfx: whoosh-cinematic, sparkle

## Frame 5 — Sur votre téléphone

- scene: Téléphone avec l'accueil réel ; tap sur « Déposer un signalement », la page du formulaire s'ouvre
- voiceover: "Depuis votre téléphone, vous déposez un signalement en quelques minutes."
- duration: 4.82s
- transition_in: crossfade
- status: animated
- src: compositions/frames/05-telephone.html
- type: demo
- asset_candidates: assets/img/m-home.jpg, assets/img/m-form.jpg
- sfx: whoosh, click
- handoff_out: phone x 190 y 360 w 700, screen showing m-form.jpg at scroll 0, opacity 1, static

## Frame 6 — 9 catégories

- scene: Le formulaire défile jusqu'aux 9 catégories ; Corruption, Fraude, Faux diplôme, Harcèlement s'allument
- voiceover: "Neuf catégories officielles. Corruption, fraude, faux diplôme, harcèlement…"
- duration: 5.731s
- transition_in: cut
- status: animated
- src: compositions/frames/06-categories.html
- type: demo
- asset_candidates: assets/img/m-form.jpg
- sfx: pop, click-soft
- handoff_in: phone x 190 y 360 w 700, screen showing m-form.jpg at scroll 0, opacity 1, static

## Frame 7 — 8 étapes

- scene: Stepper 8 étapes (libellés du site) ; Province « Kinshasa », Établissement, Description, Preuves s'animent
- voiceover: "Huit étapes guidées. La province, l'établissement, les faits, et vos preuves."
- duration: 5.677s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/07-etapes.html
- type: demo
- asset_candidates: none (UI recréée, libellés de /signalement)
- sfx: click, click, typing, pop

## Frame 8 — Anonyme ou identifié

- scene: Deux cartes « Signalement anonyme » / « Signalement identifié », l'anonyme est choisi, bouclier + « aucune donnée personnelle »
- voiceover: "Anonyme ou identifié : c'est vous qui choisissez. En mode anonyme, aucune donnée personnelle n'est conservée."
- duration: 6.728s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/08-anonyme.html
- type: benefit
- asset_candidates: none (UI recréée, textes de /signalement)
- sfx: click-soft, chime

## Frame 9 — Suivi

- scene: Reçu avec référence SIG-ESU-2026-ABC123 + code de suivi, puis frise Reçu → … → Clôturé
- voiceover: "Vous recevez une référence et un code de suivi. Et vous suivez votre dossier, étape par étape."
- duration: 6.425s
- transition_in: crossfade
- status: animated
- src: compositions/frames/09-suivi.html
- type: benefit
- asset_candidates: assets/img/m-suivi.png
- sfx: typing, chime, ping

## Frame 10 — Côté Ministère

- scene: « Et côté Ministère ? » → connexion agents → tableau de bord national réel, KPI 25 / 5 mis en avant
- voiceover: "Et côté Ministère ? Chaque signalement arrive sur le tableau de bord national des agents."
- duration: 5.685s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/10-ministere.html
- type: demo
- asset_candidates: assets/img/d-login.jpg, assets/img/d-admin.jpg
- sfx: whoosh, notification

## Frame 11 — La carte

- scene: Carte réelle des 26 provinces qui s'allument une à une, Kinshasa bordée de jaune « Kinshasa — 12 signalement(s) »
- voiceover: "Province par province, sur la carte de la RDC."
- duration: 5.75s
- transition_in: crossfade
- status: animated
- src: compositions/frames/11-carte.html
- type: demo
- asset_candidates: capture/extracted/map-provinces.json
- sfx: whoosh-short, sparkle

## Frame 12 — 24 heures

- scene: « Critique → 24 h » énorme, puis les délais du site : Élevée 72 h · Normale 7 j · Faible 15 j
- voiceover: "Un dossier critique doit être pris en charge sous vingt-quatre heures."
- duration: 4.42s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/12-delais.html
- type: proof
- asset_candidates: none (texte de /procedure)
- sfx: impact-bass-2, ping

## Frame 13 — Devise

- scene: « Justice. Transparence. Mérite. » en Cormorant, soulignés bleu / jaune / rouge
- voiceover: "Justice. Transparence. Mérite."
- duration: 4.177s
- transition_in: crossfade
- status: animated
- src: compositions/frames/13-devise.html
- type: brand
- asset_candidates: none
- sfx: riser, impact-bass-1

## Frame 14 — Votre voix compte

- scene: Sceau + ESURSI Signalement national, « Votre voix compte. », bouton jaune + URL signal.minesursi.gouv.cd
- voiceover: "Votre voix compte. Signalez, sur signal.minesursi.gouv.cd."
- duration: 8.696s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/14-cta.html
- type: cta
- asset_candidates: assets/img/logo_rdc.png
- sfx: whoosh-cinematic, pop, chime
