# Générer le manuscrit Homebrewery complet

Le manuel reste volontairement séparé en plusieurs fichiers pendant l'écriture.

Cette organisation évite qu'une modification du chapitre III casse la mise en page du chapitre I et permet de reprendre plus facilement le projet après plusieurs sessions.

## Sources utilisées

Le script assemble automatiquement :

1. `homebrewery/prologue.md` — couverture, introduction et chapitre I ;
2. `homebrewery/chapters/02-chutes-de-brume.md` ;
3. `homebrewery/chapters/03-assaut-du-temple.md` ;
4. `homebrewery/annexes.md`.

Les anciens placeholders des chapitres II et III présents à la fin de `prologue.md` sont ignorés.

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

1. génération sans erreur ;
2. aucun saut de page vide entre les modules ;
3. ouvertures des trois chapitres sur une nouvelle page ;
4. images correctement liées ;
5. tableaux non coupés ;
6. blocs `darkin`, `wuju`, `encounter`, `note` et `descriptive` correctement rendus ;
7. sommaire et numéros de page ;
8. crédits et notice fan ;
9. export PDF ;
10. relecture du PDF page par page.
