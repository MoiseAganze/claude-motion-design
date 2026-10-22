---
workflow: product-launch-video
flow: automation
storyboard: no
message: "Un abus à l'université ? Signalez-le, en toute sécurité : le Ministère agit."
destination: tiktok
aspect: 1080x1920
language: fr
audience: "Étudiants, enseignants, personnel et citoyens concernés par l'enseignement supérieur en RDC"
length: 60-90s
angle: problem-solution-demo
voice: "ElevenLabs — Hugo from Paris (DbbNuBL7lf62XwY7arQb), homme, grave, sérieux"
---

## Intent

Publicité TikTok + démo de la plateforme nationale de signalement du Ministère ESURSI (RDC),
https://signal.minesursi.gouv.cd/. Montrer le parcours citoyen (accueil → catégories → 8 étapes →
anonyme/identifié → référence + code de suivi), puis survoler rapidement l'espace agent `/admin` :
uniquement la page d'accueil du tableau de bord, la carte de la RDC en particulier. Ton institutionnel
mais moderne et rassurant. Scénario validé dans la conversation (accroche → silence → révélation →
démo citoyen → côté agent → promesse → CTA).

## Assets

- Captures réelles du site (mobile 1080 px de large) et de l'espace agent (desktop 2×), logo RDC, bannière de campagne `abus.png`.
- Carte : tracés SVG réels des 26 provinces extraits du tableau de bord (comptes réels).

## Customizations

- Voix off ElevenLabs « Hugo from Paris » (voix choisie par l'utilisateur, id DbbNuBL7lf62XwY7arQb).
- Sous-titres animés hors zones UI TikTok, bruitages de la bibliothèque locale.
- Fin : « Justice · Transparence · Mérite » (devise du site) + URL signal.minesursi.gouv.cd.

## Notes

- Confidentialité : ne jamais montrer le tableau « Derniers signalements », le graphique « Établissements les plus signalés », ni le nom de l'agent connecté. KPI + carte seulement.
- Le formulaire réel n'a pas été rempli (refus de sécurité : pas d'action sur le vrai système) → étapes 2-8 recréées en UI animée avec les libellés exacts du site ; référence d'exemple = celle du site (SIG-ESU-2026-ABC123).
- Identifiants agents fournis dans la conversation : jamais écrits dans le dépôt.
- Musique de fond : « Digital Horizons » (MP3 fourni par l'utilisateur ; « Complicit - Cinematic » introuvable via les connecteurs ElevenLabs). Prolongée à 77,5 s par fondu calé sur le tempo, creusée sous la voix (carve). Storyboard garde `music: none` (bgm hôte dans audio_meta.json).
- 2026-10-22 : catégories passées à 13 sur le site → scène 6 refaite (grille des 13 libellés exacts, VO « Treize catégories officielles… », prise `cat13-take.mp3`) ; référence SIG-ESURSI-2026-9C8CCC ; captures et chiffres du tableau de bord rafraîchis (26 / 6, Kinshasa 13). Version sœur : `videos/signal-recherche`.
