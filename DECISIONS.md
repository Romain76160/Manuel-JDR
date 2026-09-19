# DÉCISIONS DE CONCEPTION

Ce fichier explique les choix importants afin d'éviter de revenir involontairement à une ancienne structure.

---

## 1. Un manuel par grande partie de campagne

La campagne ne sera pas publiée sous la forme d'un unique livre gigantesque.

Chaque grande partie possède son propre manuel.

Le premier livre est :

**Manuel I — Prologue : L'Héritage du Wuju**

Il ne comporte que trois chapitres.

---

## 2. Abandon de l'ancienne forme « dossier de MJ »

L'ancien PDF des *Chutes de Brume* contenait de bonnes idées, mais sa structure était trop proche d'un document de conception :

- zones A/B/C ;
- nombreuses fiches et tableaux ;
- outils de maîtrise séparés ;
- informations parfois fragmentées.

Le nouveau manuel doit se lire comme un **véritable livre d'aventure publié**.

Structure préférée dans une section :

1. description du lieu ou de la situation ;
2. texte à lire aux joueurs si utile ;
3. ce qui se passe réellement ;
4. PNJ présents ;
5. indices et interactions ;
6. tests / DD ;
7. rencontre éventuelle ;
8. conséquences ;
9. « Et si les PJ… ? » pour les bifurcations importantes.

Les tableaux restent possibles lorsqu'ils améliorent réellement l'usage à la table.

---

## 3. Le manuel doit être utilisable directement en séance

Le MJ ne doit pas avoir à transformer le texte en scénario avant de jouer.

Chaque scène importante doit donner rapidement :

- ce que les PJ voient ;
- ce que le MJ sait ;
- ce que veulent les PNJ ;
- ce que les joueurs peuvent faire ;
- les conséquences probables.

---

## 4. Révélation progressive de la menace Darkin

Le Prologue ne doit pas annoncer immédiatement « voici une campagne Darkin » dans sa narration en jeu.

Progression voulue :

- **Chapitre I** : aventure Wuju et initiation ;
- **Chapitre II** : découverte de ce que le Wuju protège ;
- **Chapitre III** : preuve qu'une guerre plus vaste est déjà en mouvement.

Kayn ne doit pas dominer visuellement le livre avant le chapitre III.

---

## 5. Identité visuelle

Le Prologue doit avoir une identité ionienne / Wuju :

- jade ;
- vert doux ;
- bleu de brume ;
- blanc ;
- pierre claire ;
- végétation ;
- touches rouges ou sombres uniquement lorsque la menace Darkin progresse.

Évolution visuelle souhaitée :

- Chapitre I : lumineux et vivant ;
- Chapitre II : brume, mystère, spiritualité ;
- Chapitre III : nuit, ombres, contrastes, rouge Darkin.

---

## 6. Illustrations maîtresses

### Couverture

Paysage ionien monumental. Le Wuju et Ionia dominent l'image. La menace Darkin reste discrète.

### Chapitre I

Monastère Wuju dans les montagnes. Maître Yi peut être visible, mais le lieu doit dominer.

### Chapitre II

Les Chutes de Brume : cascade, bassin, ruines, épée d'Urong. Pas de Kayn sur l'ouverture.

### Chapitre III

Le Temple Wuju doit être représenté **creusé à l'intérieur d'une montagne**, avec une architecture verticale et plusieurs niveaux reliés par escaliers et galeries.

Kayn et Rhaast peuvent apparaître dans l'illustration d'ouverture du chapitre III, mais le temple reste un protagoniste visuel majeur.

---

## 7. Homebrewery

Le rendu final du manuel sera préparé pour **Homebrewery V3**.

Le contenu et le style doivent rester séparés autant que possible :

- manuscrit Markdown dans `homebrewery/prologue.md` et les modules de chapitre ;
- CSS dans `homebrewery/style.css`.

Le dépôt GitHub est la source de vérité. Homebrewery sert à la mise en page et à l'export.

---

## 8. Annexes

Les informations répétitives ou très techniques sont déplacées en annexes lorsque cela rend les chapitres plus fluides :

- bestiaire ;
- fiches PNJ complètes ;
- techniques Wuju ;
- objets de Doran ;
- arbre de progression ;
- cartes et handouts.

Dans les chapitres, on conserve uniquement ce qui est nécessaire pour jouer la scène.

---

## 9. Philosophie du Wuju dans le manuel

Le Wuju ne doit pas être réduit à « techniques d'épée rapides ».

Le thème central est la maîtrise de soi et le rapport à la puissance.

Question récurrente du Prologue :

> Que fait un personnage de sa puissance lorsqu'il est libre de l'utiliser ?

Cette question doit relier les trois chapitres.

---

## 10. Le Temple Wuju est une montagne habitée

Le Temple Wuju n'est plus conçu comme un monastère principalement extérieur entourant une grande cour.

La version officielle est **un sanctuaire vertical creusé dans la montagne**.

Organisation de référence :

- **niveau 0 :** entrée / vestibule ;
- **niveau -1 :** temple principal et dojo ;
- **niveau -2 :** dortoirs et cloître ;
- **niveau -3 :** reliquaire ;
- **niveau -4 :** grottes des esprits.

Ce choix sert directement le gameplay du chapitre III : les PJ commencent au milieu de la structure pendant que le Clan des Ombres attaque à la fois depuis le haut et depuis les grottes.

La verticalité doit produire des choix tactiques, pas seulement une belle carte.

---

## 11. Le final de Kayn se joue dans les profondeurs

Le duel Yi–Kayn occupe principalement le niveau -1 et les passages voisins.

Le combat tactique contre le Transfuge descend vers le niveau -3.

La confrontation finale entre les PJ et Kayn doit idéalement se dérouler **dans le reliquaire**, au plus près des Seigneurs des Darkin.

Cela permet aux trois enjeux du Prologue de se rencontrer dans un même lieu :

- le Wuju ;
- Xolaani ;
- Kayn/Rhaast.

---

## 12. Les objets de Doran sont des responsabilités, pas du butin

Les objets de Doran sont remis après l'assaut par Yi.

Ils ne récompensent pas le nombre d'ennemis vaincus. Ils récompensent la manière dont les PJ ont utilisé leur puissance.

Trois objets de référence :

- **Lame de Doran** — frapper avec maîtrise ;
- **Bouclier de Doran** — protéger et tenir ;
- **Anneau de Doran** — comprendre, soutenir et maîtriser la magie.

Chaque PJ peut recevoir un objet à la fin du Prologue.

Ces objets peuvent évoluer dans les futurs manuels, mais leur première version reste volontairement modérée pour des personnages de niveau 3.


---

## Cartographie V1 — décision de production

- Les concepts générés durant l'exploration graphique ne sont **pas automatiquement canoniques**.
- Une carte finale doit respecter `assets/cartes/VALIDATION.md`.
- Le Temple Wuju reste majoritairement **à l'intérieur de la montagne**.
- Aucun « Cœur oublié » ou niveau secret supplémentaire n'est canonique dans le Prologue.
- Les cartes finales doivent idéalement être générées **sans texte**, puis annotées de manière déterministe.
- Chapitre I : aucune battlemap n'est obligatoire pour la V1 ; une petite carte régionale reste facultative.
- Les illustrations maîtresses des chapitres I, II et III sont respectivement **Master Yi, Jun et Kayn** via les arts officiels LoR déjà intégrés.
