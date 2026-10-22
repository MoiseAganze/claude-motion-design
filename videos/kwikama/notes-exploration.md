# Notes d'exploration — prototype KWIKAMA

Parcours fait le 22 oct. 2026 sur https://kwikama.vercel.app/ (Playwright, Chromium, viewport 1920×1080).
Chaque point ci-dessous a été vérifié à l'écran ; les écarts avec le script sont marqués **ÉCART**.

## 1. Page d'accueil

- Hauteur ~13 200 px. Sections, dans l'ordre : héros « Dix-huit institutions. Un seul dossier. » (emblème à droite) →
  Le problème (3 causes + schéma « Aujourd'hui / Avec KWIKAMA ») → La réponse (4 piliers) →
  **Le parcours d'un dossier** (narration au scroll : zone collante, 8 étapes qui s'allument une à une) →
  **L'UNICEP — Dix-huit institutions, reliées** (roue de 18 nœuds or autour de KWIKAMA, cliquables) →
  Les rôles → Sécurité et souveraineté → **« Deux périmètres à ne pas confondre »** (La plateforme / Le laboratoire, hébergé à l'APLC) →
  **Cadre légal et conformité** (International / Résultats immédiats visés RI 6-7-8 / National) → pied de page.
- Charte : bleu nuit, crème, or. Titres Fraunces, texte Inter.

## 2. `/connexion`

- Deux cartes de filière : **Procédure UNICEP** (sélectionnée par défaut) et **Procédure APLC**.
- La liste « Accès rapide par rôle » change bien :
  - UNICEP : 9 rôles, dont **CENAREF · Point focal**.
  - APLC : 11 rôles — apparaissent Coordonnateur APLC, Coordonnateur adjoint, Archiviste ; **le Point focal disparaît**.

## 3–4. Point focal vs Coordonnateur UNICEP (filière UNICEP)

- **Point focal** (Masudi Lofombo Chantal, CENAREF, restreint) : **5 modules** — Tableau de bord, Coordination, Détection, Assistance, Notifications.
- **Coordonnateur UNICEP** (Ilunga Mwadi Josephine, confidentiel défense) : **15 modules** — Tableau de bord, Signalements, Vérification,
  Dossiers, Preuves, Enquête financière, Analyse assistée, Avoirs, Coordination, Rapports, Détection, Passerelles, Risques, Suivi du projet, Notifications.
- Écart de 10 modules : le split-screen tient. Note : *Assistance* existe chez le Point focal mais pas chez le Coordonnateur.
- Il n'y a pas de bouton « Déconnexion » : on sort par **« Changer de rôle »** (retour à `/connexion`).

## 5. Les modules

17 entrées au total sur l'ensemble des rôles (16 hors Tableau de bord) : les 15 du Coordonnateur + **Assistance** (Point focal)
+ **Administration** (rôle Administrateur uniquement). Toutes se chargent complètement.

## 6. Dossier DPJ-2026-014

« Redevances minières — permis du ressort de Kolwezi », EFP/LUALABA/2026/014, filière UNICEP, préjudice **12 600 000 $US**,
12/23 étapes, stade « Identification des avoirs ». Sept onglets, tous vérifiés :
Chronologie (U01→U23, dont revue technique, revue juridique, **Comité interne d'examen**, transmission + accusé de réception) ·
Preuves (ex. `PRV-2026-0355`, scellé `SC-00355`, empreinte `5e19a6b3…08cc4712`, registre des transferts ligne à ligne) ·
Enquête financière (entités liées) · Avoirs (5 biens, 8 900 000 $US) · Coordination · Rapport (`RAP-2026-014`, 4/7 sections) · Historique.

## 7. Les quatre actions réelles

### Vérification — fonctionne, deux écarts
- `SIG-2026-0195` (Ministère public, « Concessions forestières attribuées sans appel à concurrence ») → Oui / Oui / Non / Oui → **Valider la régularité**
  → statut « Validée », « Vérifiée par Ilunga Mwadi Josephine », compteurs À vérifier 2→1, Validées 2→3.
- **ÉCART** : le panneau a **quatre** contrôles, pas trois (4e : « Recherches initiales sur les faits », pour une saisine anonyme).
  Le 3e est formulé en négatif (« une violation des droits des tiers est-elle apparente ? » → la bonne réponse est **Non**).
- **ÉCART** : après validation, **aucun numéro de registre central** ne s'affiche ; le panneau se ferme.
- `SIG-2026-0193` existe aussi mais porte sur un « litige commercial entre deux sous-traitants » : je l'ai écarté, il appelle plutôt un rejet.

### Coordination → journal d'audit — la relance fonctionne, le journal ne suit pas
- `RQ-2026-0091` (CENAREF, DPJ-2026-007, « Déclarations d'opérations suspectes visant Nzadi Infrastructure SA ») est déjà « En retard, 1 relance ».
  **Émettre une relance** → « Relancée, 2 relances ».
- **ÉCART** : un délai ne peut pas « basculer en dépassement » sous nos yeux ; la ligne est déjà en retard.
- **ÉCART** : le journal d'audit (Administration, rôle Administrateur) est **statique** (18 opérations) et l'état de la démo est
  **réinitialisé à chaque changement de rôle**. La ligne de relance n'y apparaît jamais. Le journal contient en revanche une vraie ligne
  sur la même réquisition : « 2026-10-15 07:55:40 · Masudi Lofombo Chantal · Accusé de réception d'une réquisition · RQ-2026-0091 ».

### Analyse assistée — conforme au script
- DPJ-2026-014 présélectionné → **Lancer l'analyse** → 5 étapes (Lecture des pièces / Résolution des entités / Croisement avec les dossiers ouverts /
  Restitution et citation des sources) en ~2,5 s.
- Résultats : 148 pièces lues, 37 entités ; rapprochement **DPJ-2026-007 à 84 %** (compte BCF 00214-…-77, deux virements au libellé identique,
  **même mandataire**) ; 4 signaux avec leurs pièces ; « Ce que l'analyse n'a pas pu établir » (4 points) ; « aucun modèle n'est exécuté ici » en tête de page.
- **Retenir la piste** → « Retenu par l'agent », compteur **0 / 3 → 1 / 3**.
- Remarque : le bandeau « aucun modèle n'est exécuté » est en haut de page ; il sort du cadre quand on descend. Au montage, je l'épingle.

### Avoirs — fonctionne, un écart
- `AVR-2026-072` (trois comptes de Katanga Mineral Processing Ltd, 2 740 000 $US, dossier Kolwezi) → **Passer au statut « Saisi »**
  → tuiles Gelés 6 880 000 → 4 140 000 $US, Saisis 3 896 000 → 6 636 000 $US.
- **ÉCART** : les deux montants de tête de l'encart « Résultat immédiat 8 » (Sous main de justice 10 776 000 / Acquis à l'État 3 550 000) **ne changent pas**
  (gelé et saisi sont tous deux sous main de justice). Aucun écran « tableau de bord financier de l'État » n'existe dans le prototype.

## 8. Autres constats

- **Passerelles — ÉCART** : les 3 registres (TOFONGOLAMISO, ITIE, GUCE) sont présentés, mais **aucune interrogation interactive** n'existe,
  et un bandeau dit « Architecture simulée. Aucune connexion réelle n'est établie ». La paire raison sociale → bénéficiaire effectif existe en vrai ailleurs :
  fiche `AVR-2026-072` (« Propriétaire déclaré : Katanga Mineral Processing Ltd » / « Bénéficiaire effectif : Ilunga Mwadi Patrick »).
- Graphe de relations (Enquête financière) : graphe à forces, filtrable par dossier ; sélectionner une entité isole ses liens.
- Le script dit « la presse » ; l'interface dit « Média ».
- Coïncidence de noms dans les données fictives : le bénéficiaire effectif présumé s'appelle **Ilunga Mwadi Patrick**, la Coordonnatrice **Ilunga Mwadi Josephine**.
