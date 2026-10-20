---
workflow: product-launch-video
flow: automation
storyboard: no
message: "Vos courriers se traitent tout seuls."
destination: tiktok
aspect: 1080x1920
language: fr
audience: "Organisations (administrations, cabinets, entreprises) qui reçoivent beaucoup de courriers par mail"
length: 50s
angle: problem-solution-demo
voice: "ElevenLabs — féminine, chaleureuse, premium (fr)"
---

## Intent

Publicité TikTok pour « Agent Courrier », un agent IA qui automatise le traitement des courriers reçus par mail :
détection, lecture OCR (même scanné), compréhension IA (objet, expéditeur, date, priorité), enregistrement,
accusé de réception automatique, cas douteux transmis à un humain, publicités ignorées. Générique — ne cite
aucune organisation ni ministère. Ton premium, rythme TikTok (coupe toutes les 2-3 s, hook dès la 1re seconde),
démo concrète : on suit UN courrier de bout en bout. Doit être impressionnant.

## Assets

- Aucun asset utilisateur. Tout est inventé (UI boîte mail, document scanné fictif, fiche, registre, téléphone).

## Customizations

- Voix off ElevenLabs (connecteur hôte), voix féminine chaleureuse, ton premium.
- Sous-titres animés mot par mot, hors zones UI TikTok.
- Bruitages (whoosh, tampon, notification, scan…) : oui.
- Fin : slogan « Vos courriers se traitent tout seuls. » + nom « Agent Courrier », transition fluide.

## Notes

- PAS de musique (l'utilisateur l'ajoute lui-même) → `music: none`.
- PAS d'appel à l'action, numéro ou contact pour l'instant.
- Pas de mention d'OpenRouter / coûts.
- Source : user_script.txt (script validé dans la conversation), VO_MODE: verbatim.
