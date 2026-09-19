# Homebrewery — assemblage du Prologue

Ce dossier contient la version destinée à la mise en page finale dans Homebrewery.

## Fichiers

- `prologue.md` : source de la couverture, de l'introduction et du chapitre I.
- `prologue-complet.md` : **V1 assemblée du manuel complet**, générée à partir des modules.
- `chapters/02-chutes-de-brume.md` : chapitre II mis en page.
- `chapters/03-assaut-du-temple.md` : chapitre III mis en page.
- `style.css` : identité visuelle commune du manuel.

## Ordre d'assemblage final

1. couverture et crédits ;
2. sommaire et introduction MJ ;
3. chapitre I — Les Épreuves du Wuju ;
4. chapitre II — Les Chutes de Brume ;
5. chapitre III — L'Assaut du Temple ;
6. annexes ;
7. épilogue / fin du Prologue.

## Règle de travail

Les fichiers `manuel/prologue/*.md` restent la référence narrative.

Les fichiers de ce dossier servent à transformer ce contenu en pages directement exploitables dans Homebrewery.

Une modification de scénario doit donc d'abord être répercutée dans le manuscrit narratif et le canon, puis dans la version Homebrewery correspondante.

## Encadrés visuels

Le CSS commun définit quatre familles principales :

- `{{descriptive ...}}` : texte à lire / description importante ;
- `{{note ...}}` : conseil MJ ou rappel de règle ;
- `{{wuju ...}}` : enseignement, vision ou interaction spirituelle ;
- `{{darkin ...}}` : tentation, murmure ou révélation Darkin ;
- `{{encounter ...}}` : rencontre et information tactique.

## Illustrations maîtresses

### Couverture

Ionia et le Wuju dominent l'image ; menace Darkin discrète.

### Chapitre I

**Master Yi** — art officiel Legends of Runeterra intégré via Riot Data Dragon.

### Chapitre II

**Jun, the Prodigy** — art officiel Legends of Runeterra intégré. La carte des Chutes reste à insérer séparément.

### Chapitre III

**Kayn** — art officiel Legends of Runeterra intégré. Les cartes tactiques doivent, elles, conserver le Temple Wuju creusé dans la montagne et la structure verticale canonique.

## Build

Le manuscrit complet est généré avec :

```bash
python3 scripts/build_manuel.py
```

Sortie : `homebrewery/prologue-complet.md`.

La V1 assemblée existe déjà dans le dépôt. Les prochaines passes concernent surtout les cartes finales, la couverture, les sauts de page, la densité des pages et le premier export PDF.
