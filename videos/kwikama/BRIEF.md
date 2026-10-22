---
workflow: general-video
flow: automation
storyboard: yes
message: "Dix-huit institutions. Un seul dossier."
destination: youtube
aspect: 1920x1080
language: fr
audience: "Autorités et partenaires de l'UNICEP / APLC (institutionnel, juridique)"
length: 4m25s
angle: démonstration institutionnelle d'un prototype
voice: elevenlabs:McVZB9hVxVSk3Equu8EH
---

## Intent

Vidéo de présentation YouTube de KWIKAMA, « le bouclier numérique de l'UNICEP » (https://kwikama.vercel.app/).
Voix off féminine, française, posée. Ton sobre, institutionnel, sérieux : « Rien qui ressemble à une intro de chaîne YouTube. »
Ouverture 0:00–0:24 entièrement en motion design (dix-huit sources dispersées deviennent un seul dossier), puis sept cas
filmés sur le prototype, puis souveraineté et clôture. Script complet fourni par l'utilisateur : texte dit verbatim.

## Assets

- assets/brand/logo-source.png — logo fourni (276×346, trop petit pour du plein écran) ; redessiné en SVG fidèle pour l'emblème et la résolution du réseau.
- assets/voice/ — voix ElevenLabs, voice id McVZB9hVxVSk3Equu8EH, eleven_v4, texte complet en une prise.
- capture/ — captures réelles du prototype, 3840×2160 (viewport 1920×1080 @2x), un dossier par scène.

## Customizations

- Ouverture motion design selon la Partie B du script (timings, couleurs #052649 / #0a3360, courbe cubic-bezier(0.2, 0.7, 0.3, 1), filets or en stroke-dashoffset 300 ms, fondu 400 ms sur « KWIKAMA », signature or).
- Captures : états réels capturés en 4K, souris / scrolls / zooms / clics animés au montage (choix confirmé à la place de la vidéo Playwright, trop floue).
- Texte complet conservé (673 mots, ~4 min 25–4 min 30). Générique affiché à l'écran, non lu.
- Rendu 1920×1080, 60 i/s, qualité haute.

## Notes

- Interdits absolus sur l'ouverture : pas de particules, pas de rotation 3D, pas de reflet / lens flare / halo, pas de rebond ni d'élastique,
  pas de tremblement de caméra, pas de flou de mouvement, pas de « whoosh ». `transform` et `opacity` uniquement. Fiches lisibles à tout instant.
- N'inventer aucune capture. Écarts entre le script et le prototype : voir notes-exploration.md (4 contrôles au lieu de 3 ; pas de numéro de registre affiché ;
  journal d'audit statique, la relance n'y apparaît pas ; Passerelles sans interrogation ; montants de tête de l'encart RI 8 inchangés).
- `prefers-reduced-motion` : sans objet pour un MP4.
- Pas de musique disponible (aucun fournisseur de musique dans cette session) : voix seule, sons très rares.
