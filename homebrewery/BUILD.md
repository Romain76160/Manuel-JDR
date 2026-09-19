# Générer le manuscrit Homebrewery complet

Le manuel reste volontairement séparé en plusieurs fichiers pendant l'écriture.

Cette organisation évite qu'une modification du chapitre III casse la mise en page du chapitre I et permet de reprendre plus facilement le projet après plusieurs sessions.

## Sources utilisées

Le script assemble automatiquement :

1. `homebrewery/prologue.md` — couverture, introduction et chapitre I ;
2. `homebrewery/chapters/02-chutes-de-brume.md` ;
3. `homebrewery/chapters/03-assaut-du-temple.md` ;
4. `homebrewery/annexes.md`.

`prologue.md` se termine par le marqueur `<!-- BUILD:END_PROLOGUE_BASE -->`, utilisé pour séparer proprement la base des modules ajoutés au build.

## Commande

Depuis la racine du dépôt :

```bash
python3 scripts/build_manuel.py
```

Le fichier généré est :

```text
homebrewery/prologue-complet.md
```

Il peut ensuite être copié intégralement dans Homebrewery.

Le CSS à utiliser reste :

```text
homebrewery/style.css
```

## Règle de travail

Ne modifiez pas directement `prologue-complet.md` pour écrire le scénario.

Modifiez toujours les fichiers sources concernés, puis relancez le script.

Cela évite d'avoir plusieurs versions contradictoires du manuel.

## Avant un export PDF

Vérifier dans cet ordre :

1. génération sans erreur avec `scripts/build_manuel.py` ;
2. validation avec `scripts/validate_manuel.py` et `scripts/check_canon.py` ;
3. aucun saut de page vide entre les modules ;
4. ouvertures des trois chapitres sur une nouvelle page ;
5. images correctement liées ;
6. tableaux non coupés ;
7. blocs `darkin`, `wuju`, `encounter`, `note` et `descriptive` correctement rendus ;
8. sommaire et numéros de page ;
9. crédits et notice fan ;
10. export PDF ;
11. relecture du PDF page par page.
