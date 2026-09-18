# Validation des cartes — Temple Wuju et Chutes de Brume

> **Statut : règles obligatoires avant intégration dans le manuel.**

Les concepts générés pendant la phase d'exploration graphique servent de **références de style uniquement** tant qu'ils ne respectent pas tous les critères ci-dessous.

---

# 1. Canon non négociable — Temple Wuju

Le Temple Wuju n'est **pas** un grand monastère extérieur posé sur une montagne.

Il s'agit d'un **sanctuaire vertical creusé dans la montagne**.

La vue générale finale doit donc montrer clairement :

- une entrée dans le flanc rocheux ;
- des niveaux superposés à l'intérieur de la masse montagneuse ;
- des galeries de pierre ;
- des puits de lumière et ouvertures naturelles limités ;
- de l'eau et des cascades traversant certains niveaux ;
- des jardins spirituels intérieurs ou semi-ouverts ;
- une connexion souterraine vers les grottes des esprits.

Une terrasse extérieure, un balcon ou une entrée monumentale sont possibles, mais ils ne doivent jamais donner l'impression que la majorité du temple est à ciel ouvert.

---

# 2. Niveaux officiels

## Niveau 0 — Entrée / Vestibule

Doit contenir :

- entrée principale ;
- vestibule ;
- râteliers d'armes ;
- poste de garde ;
- accès descendant vers -1.

## Niveau -1 — Temple principal

Doit contenir :

- grand bassin intérieur ;
- arbre Wuju ;
- dojo ;
- grande cloche ;
- circulations vers 0 et -2.

Usage principal : duel Yi / Kayn.

## Niveau -2 — Dortoirs / Cloître

Doit contenir :

- dortoirs des disciples ;
- cloître intérieur ;
- bibliothèque / archives ;
- zones de repos ;
- accès vers -1 et -3.

Usage principal : départ des PJ pendant l'assaut.

## Niveau -3 — Reliquaire

Doit contenir :

- salle centrale du reliquaire ;
- chambre des esprits ;
- alcôves ;
- colonnes / couvert ;
- bassin ou conduits spirituels ;
- accès vers -2 et -4.

Usage principal : Transfuge, Jun/Xolaani, combat final contre Kayn.

## Niveau -4 — Grottes des esprits

Doit contenir :

- grottes naturelles ;
- eau souterraine ;
- passage oublié vers l'extérieur ;
- route d'infiltration du Clan des Ombres.

Il n'existe **pas de “niveau secret / cœur oublié” officiel dans le Prologue**.

---

# 3. Règles de texte sur les cartes

Les versions finales générées doivent idéalement être **sans texte intégré à l'image**.

Pourquoi :

- les générateurs d'images commettent facilement des fautes ;
- les numéros peuvent ne plus correspondre au canon ;
- le français doit rester parfaitement contrôlé ;
- une même base graphique doit servir aux versions joueurs et MJ.

Le texte, la légende, les numéros et les flèches seront ajoutés séparément.

Acceptable dans l'image :

- architecture ;
- grille éventuelle ;
- compass rose sans lettres ;
- symboles décoratifs ;
- éléments naturels.

À éviter :

- noms de salles générés ;
- citations générées ;
- listes ;
- numérotation automatique ;
- faux caractères asiatiques.

---

# 4. Différence joueurs / MJ

## Joueurs

Aucun :

- ennemi ;
- trajet d'infiltration ;
- passage secret non découvert ;
- position initiale ennemie ;
- emplacement caché d'une relique.

## MJ

Peut ajouter en surimpression :

- flèches rouges d'infiltration ;
- position initiale des PJ ;
- position du Transfuge ;
- position de Kayn ;
- passages secrets ;
- objectifs ;
- numéros de référence.

Les deux versions doivent être basées sur **la même image de fond**.

---

# 5. Chutes de Brume

La carte finale doit correspondre au chapitre II et ne doit pas transformer les Chutes en second Temple Wuju.

Elle doit montrer :

- sentier d'arrivée ;
- grande cascade ;
- Bassin du Silence ;
- épée / mémorial d'Urong ;
- ruines sous la cascade ;
- quelques chemins et promontoires ;
- cairns sur le trajet ;
- environnement isolé.

Le Temple Wuju peut être indiqué comme une **direction éloignée**, mais il ne doit pas dominer le site.

---

# 6. Critères de rejet automatique

Une carte est rejetée comme finale si elle :

- représente le Temple Wuju principalement à l'extérieur ;
- invente un niveau majeur non canonique ;
- inverse les fonctions des niveaux -1 et -2 ;
- transforme le chapitre II en visite d'un grand village ou d'un autre temple ;
- contient du texte faux ou illisible impossible à retirer ;
- montre Kayn ou des ennemis dans une carte joueurs ;
- révèle les Seigneurs des Darkin aux joueurs avant leur découverte.

---

# 7. Workflow final

1. générer un fond **sans texte** ;
2. vérifier architecture et connexions ;
3. valider contre `lore/temple-wuju.md` ;
4. ajouter légende et numéros avec un outil déterministe ;
5. produire version joueurs ;
6. dupliquer le même fond ;
7. ajouter informations MJ ;
8. intégrer seulement ces exports dans Homebrewery.

Les concepts précédents restent utiles comme références de palette, texture, cadrage et densité visuelle, mais ne doivent pas être considérés comme canoniques automatiquement.
