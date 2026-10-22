---
format: 1080x1920
duration: 89s
message: "Intégrité scientifique : signaler, c'est protéger."
arc: Labo → Constat → Que faire ? → Plateforme → Démo (catégorie · lieu · faits/preuves · anonyme · accusé · suivi) → Morale → CTA
audience: chercheurs et personnels de la recherche (RDC)
mode: autonomous
music: none
---

## Video direction

- Same design system as `videos/signal-esursi` (frame.md copied): navy `#001B3D`, blue `#007FFF` accent, yellow `#F7D117` = action/selection, red `#CE1126` = falsified data only, RDC flag stripe on top. Titles Cormorant Garamond 700, UI Source Sans 3.
- Lab = flat SVG illustration (flasks, analyser, chart) in brand colours, no stock imagery. Form steps recreated with exact site labels; the real form is never filled.
- Key messages emphasised (doc §6): anonymat possible, identité chiffrée, code de suivi confidentiel, messagerie sécurisée.
- Layout: key content y 150–1330; captions band 1370–1540; x ≤ 990. On-screen tag « Scénario fictif » on the story frames.

## Frame 1 — Laboratoire

- scene: Illustration animée d'un labo d'analyse des eaux (flacons, appareil, courbe) ; titre « Intégrité scientifique : signaler, c'est protéger » ; des valeurs sont raturées
- voiceover: "Au Centre de Recherche en Eau et Environnement, une chercheuse découvre que des résultats d'analyse ont été modifiés avant publication."
- duration: 7.773s
- transition_in: cut
- status: animated
- src: compositions/frames/01-labo.html
- type: hook
- asset_candidates: illustration SVG
- sfx: whoosh-cinematic, glitch-1

## Frame 2 — 48 → 31

- scene: 48 cases d'échantillons ; 17 en rouge (Pb, Hg) disparaissent ; compteur 48 → 31
- voiceover: "Quarante-huit échantillons analysés. Trente et un seulement dans le rapport. Les valeurs non conformes en plomb et en mercure ont tout simplement disparu."
- duration: 8.897s
- transition_in: crossfade
- status: animated
- src: compositions/frames/02-echantillons.html
- type: pain_point
- asset_candidates: none
- sfx: impact-bass-1, error

## Frame 3 — Que faire ?

- scene: « Que faire ? » claque seul
- voiceover: "Que faire?"
- duration: 1.425s
- transition_in: cut
- status: animated
- src: compositions/frames/03-que-faire.html
- type: tension
- asset_candidates: none
- sfx: whoosh-short

## Frame 4 — La plateforme

- scene: Sceau + ESURSI ; téléphone avec l'accueil réel ; chips chercheur · agent · étudiant · citoyen
- voiceover: "Le Ministère met à disposition une plateforme sécurisée, ouverte à tout chercheur, agent, étudiant ou citoyen."
- duration: 7.331s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/04-plateforme.html
- type: reveal
- asset_candidates: assets/img/m-home.jpg, assets/img/logo_rdc.png
- sfx: whoosh, pop

## Frame 5 — Catégorie

- scene: Les 13 catégories ; les 4 catégories recherche s'allument ; Intégrité scientifique sélectionnée ; type « Manipulation de résultats de recherche »
- voiceover: "Parmi treize catégories, elle choisit : Intégrité scientifique. Type de faits : manipulation de résultats de recherche."
- duration: 8.14s
- transition_in: crossfade
- status: animated
- src: compositions/frames/05-categorie.html
- type: demo
- asset_candidates: none (libellés /signalement)
- sfx: pop, click

## Frame 6 — Lieu et service

- scene: Province Kinshasa ; recherche « CREE » → Centre de Recherche en Eau et Environnement (CREE) ; Un service : Laboratoire d'analyse de la qualité des eaux
- voiceover: "Province : Kinshasa. Établissement : son centre de recherche, retrouvé en quelques lettres. En cause : le service, sans accusation nominative."
- duration: 9.901s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/06-lieu.html
- type: demo
- asset_candidates: none (référentiel national)
- sfx: click, typing

## Frame 7 — Faits et preuves

- scene: Objet + description qui défile ; gravité Élevée ; 3 fichiers de preuve déposés
- voiceover: "Elle décrit les faits, précis et datés. Gravité : élevée. Il y va de la santé des riverains. Et elle joint ses preuves : les relevés bruts, et le rapport final."
- duration: 10.318s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/07-faits.html
- type: demo
- asset_candidates: none
- sfx: typing, click, pop

## Frame 8 — Anonyme

- scene: Mode anonyme choisi ; option identifiée survolée ; identité chiffrée
- voiceover: "Elle choisit le mode anonyme. Identifiée, son identité serait chiffrée, et réservée aux seuls agents habilités."
- duration: 7.465s
- transition_in: crossfade
- status: animated
- src: compositions/frames/08-anonyme.html
- type: benefit
- asset_candidates: none
- sfx: click-soft, chime

## Frame 9 — Accusé de réception

- scene: Certification cochée, envoi ; accusé : SIG-ESURSI-2026-9C8CCC + code 4F9A1C7E2B3D
- voiceover: "Elle certifie, elle envoie… et reçoit une référence, et un code de suivi confidentiel."
- duration: 6.559s
- transition_in: crossfade
- status: animated
- src: compositions/frames/09-accuse.html
- type: benefit
- asset_candidates: none
- sfx: click, chime, typing

## Frame 10 — Suivi et messagerie

- scene: Frise Reçu → … → Investigation en cours ; message de l'enquêteur ; messagerie sécurisée
- voiceover: "Elle suit son dossier, et échange avec l'enquêteur par messagerie sécurisée, sans jamais révéler son identité."
- duration: 6.816s
- transition_in: crossfade
- status: animated
- src: compositions/frames/10-suivi.html
- type: benefit
- asset_candidates: none
- sfx: notification, ping

## Frame 11 — Trahir la science

- scene: « Falsifier des résultats, c'est trahir la science, et mettre des vies en danger. » sur le labo assombri
- voiceover: "Falsifier des résultats, c'est trahir la science, et mettre des vies en danger."
- duration: 5.555s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/11-trahir.html
- type: brand
- asset_candidates: illustration SVG
- sfx: riser, impact-bass-2

## Frame 12 — Signalez-le

- scene: Vous êtes témoin ? Signalez-le, en toute sécurité. Bouton + URL + sceau
- voiceover: "Vous êtes témoin ? Signalez-le, en toute sécurité, sur signal.minesursi.gouv.cd."
- duration: 8.787s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/12-cta.html
- type: cta
- asset_candidates: assets/img/logo_rdc.png
- sfx: whoosh-cinematic, pop, chime
