---
format: 1920x1080
duration: 4m24s
message: "Dix-huit institutions. Un seul dossier."
arc: Silos → L'UNICEP → Filières et périmètres → Sept cas (saisine, passerelles, preuve, analyse, coordination, qualité, recouvrement) → Souveraineté → Marque
audience: Autorités et partenaires de l'UNICEP / APLC
mode: collaborative
voice: assets/voice/take-b.mp3 (ElevenLabs McVZB9hVxVSk3Equu8EH, 243.5 s, word timings in take-b.words.json)
---

Timings below are video time. Voice is cut per sentence group from take B and placed on the timeline; real word timings drive every sync point.
Every captured screen is a real prototype state (capture/), shown full-bleed at scale ≥ 1.0; cursor drawn, 1.5 s hold after each click.

## Frame 1: Ouverture — les silos (0:00–0:22)

- act: Ouverture
- status: outline
- src: compositions/frames/01-silos.html
- duration: 22s
- transition_in: cut
- motion: compose — `svg-path-draw` (filet or, liens or), `center-outward-expansion` inversé (convergence), `viewport-change` (recul 1.0 → 0.94), `logo-assemble-lockup` (résolution en emblème)
- voiceover: "En République Démocratique du Congo, dix-huit institutions enquêtent… Un relevé bancaire ici. Une déclaration en douane là. Un registre d'entreprise ailleurs. Chacune détient une pièce. Aucune ne voit l'ensemble."

0:00 vide bleu nuit #052649, filet or 1 px tracé gauche→droite en 1,2 s. 0:02 la voix démarre ; le filet se dissout, 18 fiches
apparaissent (fondu + 12 px vers le haut, 90 ms d'écart, échelles 0,82–1,0), chacune avec un fragment réel et le sigle de
l'institution. 0:08,6 sur « Un relevé bancaire ici » : les cloisons #0a3360 montent en 1,4 s, recul caméra 1,0→0,94 ; le silo tient.
0:15,9 « Aucune ne voit l'ensemble » : arrêt net 400 ms, puis les cloisons s'effacent. Convergence sur cubic-bezier(0.2,0.7,0.3,1),
1,8 s, 40 ms d'écart, filets or tracés entre fiches voisines (300 ms). Pile unique + réseau du logo. Le réseau se contracte en emblème,
« KWIKAMA » en fondu 400 ms, signature or « le bouclier numérique de l'UNICEP ».

## Frame 2: L'UNICEP (0:22–0:43)

- act: Ouverture
- status: outline
- src: compositions/frames/02-unicep.html
- duration: 21s
- transition_in: crossfade
- motion: `viewport-change` (lente poussée sur les captures), crossfades entre états réels
- voiceover: "L'UNICEP — l'Unité Interservices de Collaboration — réunit ces institutions… La plateforme, elle, appartient à l'UNICEP."

La voix démarre sur l'emblème tenu. « KWIKAMA est son outil de travail » → fondu vers le héros de la page d'accueil
(« Dix-huit institutions. Un seul dossier. »), où « intégrité en kikongo » est écrit en toutes lettres. Puis la roue des 18
institutions ; sur « l'Agence de prévention… » clic sur le nœud APLC (son rôle s'affiche) ; sur « La plateforme… appartient à
l'UNICEP » la section « Deux périmètres à ne pas confondre ».

## Frame 3: Deux filières, chacun à sa place (0:43–1:04)

- act: Le prototype
- status: outline
- src: compositions/frames/03-filieres.html
- duration: 21s
- transition_in: crossfade
- motion: blueprint `cursor-ui-demo` + `comparison-split`
- voiceover: "L'APLC reçoit des signalements… Un point focal de la CENAREF accède aux réquisitions qui lui sont adressées. Pas au fonds de dossiers."

/connexion : clic « Procédure APLC » sur « L'APLC reçoit… » (la liste des rôles change : Coordonnateur, adjoint, Archiviste),
clic « Procédure UNICEP » sur « L'UNICEP, elle… ». Puis split-screen : à gauche la barre latérale du Point focal (5 modules),
à droite celle du Coordonnateur (15). Les 10 modules absents à gauche s'estompent un à un dans la colonne de droite.

## Frame 4: Cas 1 — La saisine et sa régularité (1:04–1:30)

- act: Sept cas
- status: outline
- src: compositions/frames/04-saisine.html
- duration: 26s
- transition_in: crossfade
- motion: blueprint `cursor-ui-demo`, `coordinate-target-zoom` sur le panneau
- voiceover: "L'UNICEP est saisie par la CENAREF, un juge d'instruction… Ce n'est qu'ensuite que le dossier est ouvert, numéroté, inscrit au registre central."

Vérification : la liste des 5 décisions (origines visibles : sonneur d'alerte, CENAREF, média, juge, ministère public) pendant
l'énumération. Clic `SIG-2026-0195` « À vérifier ». Zoom sur les contrôles : Oui sur « compétente ? », Oui sur « références ? »,
Non sur « droits des tiers » (formulé en négatif dans l'interface), puis le 4e contrôle sur « Ce n'est qu'ensuite ».
Clic « Valider la régularité » → la ligne passe « Validée », compteurs 2→1 / 2→3. Puis la liste des dossiers numérotés (registre).

## Frame 5: Cas 2 — Sortir des silos pour de bon (1:30–1:49)

- act: Sept cas
- status: outline
- src: compositions/frames/05-passerelles.html
- duration: 19s
- transition_in: crossfade
- motion: `coordinate-target-zoom` (zoom GUCE), incrustation d'un recadrage réel
- voiceover: "Un dossier ne se construit pas en vase clos… Avec lui, elle atteint une personne."

Passerelles : les 3 registres (TOFONGOLAMISO, ITIE, GUCE) chacun mis en avant à sa citation, le bandeau « Architecture simulée »
reste lisible. Zoom sur la carte GUCE. Incrustation (recadrage de la vraie fiche `AVR-2026-072`) : « Propriétaire déclaré :
Katanga Mineral Processing Ltd » sur « raison sociale », puis « Bénéficiaire effectif : Ilunga Mwadi Patrick » sur « une personne ».

## Frame 6: Cas 3 — La preuve et ce qui la rend opposable (1:49–2:17)

- act: Sept cas
- status: outline
- src: compositions/frames/06-preuve.html
- duration: 28s
- transition_in: crossfade
- motion: `viewport-change` (défilement de la chronologie), `cursor-ui-demo`, surlignage ligne à ligne
- voiceover: "Le dossier des redevances minières de Kolwezi… Le dossier se construit. Il ne se raconte pas."

`DPJ-2026-014` : en-tête (12 600 000 $US, filière UNICEP), la chronologie défile. Onglet Preuves : `PRV-2026-0355`, scellé
`SC-00355`, empreinte, puis le registre des transferts se déroule ligne à ligne au fil de « origine, date, heure… ». Graphe de
relations filtré sur DPJ-2026-014 ; clic sur « Ilunga Mwadi Patrick », ses liens s'isolent.

## Frame 7: Cas 4 — L'analyse assistée ★ (2:17–3:12)

- act: Sept cas
- status: outline
- src: compositions/frames/07-analyse.html
- duration: 55s
- transition_in: crossfade
- motion: blueprint `agent-progress-theater` (adapt, captures réelles), `coordinate-target-zoom`, `viewport-change`
- voiceover: "L'analyse assistée lit les cent quarante-huit pièces… En exploitation, le traitement reposerait sur un moteur documentaire installé sur site, et sur des serveurs souverains distincts de la plateforme."

Clic « Lancer l'analyse » : les 5 étapes réelles défilent. Résultats, chacun tenu : 1) rapprochement 84 % `DPJ-2026-007`, zoom
sur « même compte bancaire » / « même mandataire » ; 2) un signal et ses pièces ; 3) « Ce que l'analyse n'a pas pu établir »,
tenu 3 s pleines (sur « chaque constat dit ce qu'il ne démontre pas ») ; 4) clic « Retenir la piste » sur « un agent habilité qui
retient la piste », compteur DÉCISIONS 0/3 → 1/3. Le bandeau réel « aucun modèle n'est exécuté ici » est épinglé en haut tout du long.

## Frame 8: Cas 5 — La coordination se mesure (3:12–3:34)

- act: Sept cas
- status: outline
- src: compositions/frames/08-coordination.html
- duration: 22s
- transition_in: crossfade
- motion: `cursor-ui-demo`, coupe franche
- voiceover: "Quarante-huit heures pour notifier le parquet… La collaboration interinstitutionnelle se mesure."

Le tableau des délais POS (48 h / 7 j / 72 h) surligné à chaque citation. `RQ-2026-0091` « En retard » ; clic → « Émettre une
relance » → « Relancée, 2 relances ». COUPE FRANCHE vers le journal d'audit : surlignage de la vraie ligne horodatée sur
`RQ-2026-0091` (le journal du prototype est statique ; on ne montre pas une ligne « qui vient de s'inscrire »).

## Frame 9: Cas 6 — La qualité avant la transmission (3:34–3:51)

- act: Sept cas
- status: outline
- src: compositions/frames/09-qualite.html
- duration: 17s
- transition_in: crossfade
- motion: `viewport-change` + surlignage étape par étape
- voiceover: "Avant toute transmission, le dossier passe une revue technique… avec accusé de réception, et avec retour attendu."

Chronologie de DPJ-2026-014, dernières étapes : revue technique, revue juridique, Comité interne d'examen, transmission,
accusé de réception — chacune s'éclaire sur son mot.

## Frame 10: Cas 7 — Le recouvrement (3:51–4:03)

- act: Sept cas
- status: outline
- src: compositions/frames/10-recouvrement.html
- duration: 12s
- transition_in: crossfade
- motion: `cursor-ui-demo`, crossfade d'état réel
- voiceover: "Identifié. Gelé. Saisi. Confisqué. Restitué. … Une enquête qui ne récupère rien n'a rien réparé."

Avoirs : l'encart « Résultat immédiat 8 » et sa phrase « Une enquête qui ne récupère rien n'a rien réparé ». Les 5 statuts
s'éclairent sur la voix. `AVR-2026-072` : « Passer au statut « Saisi » » → tuiles Gelés 6 880 000 → 4 140 000, Saisis
3 896 000 → 6 636 000 $US.

## Frame 11: Souveraineté et clôture (4:03–4:28)

- act: Clôture
- status: outline
- src: compositions/frames/11-cloture.html
- duration: 25s
- transition_in: crossfade
- motion: blueprint `kinetic-type-beats` (aplats sobres), `constellation-hub`, `logo-assemble-lockup`
- voiceover: "KWIKAMA est hébergée sur les serveurs de l'État… Dix-huit institutions. Un seul dossier. KWIKAMA — le bouclier numérique de l'UNICEP."

Aplats sobres bleu nuit : « Serveurs de l'État · Code du numérique · ISO/IEC 27001 », puis les trois résultats immédiats du GAFI
s'inscrivent l'un sous l'autre (RI 6 · RI 7 · RI 8, mots exacts de la voix). Retour au réseau des 18 institutions (même réseau
que l'ouverture), qui se résout en emblème + KWIKAMA + signature.

## Frame 12: Générique (4:28–4:36)

- act: Clôture
- status: outline
- src: compositions/frames/12-generique.html
- duration: 8s
- transition_in: crossfade
- motion: blueprint `titlecard-reveal`
- voiceover: (aucune — texte à l'écran)

« Prototype de démonstration. Données simulées, personnes et affaires fictives. Aucun modèle d'intelligence artificielle n'est
exécuté dans ce prototype. » Inter, petit, centré bas, sur bleu nuit.
