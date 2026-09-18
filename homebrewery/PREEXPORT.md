# Checklist pré-export — Manuel I : L'Héritage du Wuju

Cette checklist est à suivre avant chaque export PDF de test.

## 1. Build

```bash
python3 scripts/build_manuel.py
python3 scripts/validate_manuel.py
```

Le validateur doit terminer par :

`Validation structurelle : OK`

## 2. Vérification Homebrewery

Après collage/import de `homebrewery/prologue-complet.md` et de `homebrewery/style.css` :

- vérifier la couverture ;
- vérifier que chaque chapitre commence sur une nouvelle page ;
- vérifier les colonnes qui débordent ;
- vérifier les tableaux trop larges ;
- vérifier les encadrés `note`, `wuju`, `darkin` et `encounter` ;
- vérifier qu'aucun pied de page ne chevauche le texte ;
- vérifier que les grandes illustrations ne masquent pas de contenu.

## 3. Cartes

- Chutes de Brume : carte principale lisible et sans informations MJ dans la version joueurs ;
- Temple Wuju : carte générale verticale ;
- niveau -1 : temple principal ;
- niveau -2 : dortoirs / cloître ;
- niveau -3 : reliquaire ;
- les routes d'infiltration ne figurent que dans la version MJ.

## 4. Cohérence narrative

- Kayn n'apparaît pas directement au chapitre II ;
- le Temple Wuju est toujours décrit comme creusé dans la montagne ;
- Jun accompagne le groupe aux Chutes ;
- Cassian ne révèle son magnétisme qu'au chapitre III ;
- les Seigneurs des Darkin sont liés à Xolaani ;
- Kayn n'est pas supposé mourir dans le Prologue ;
- le combat final est résolu par objectifs ou retrait de Kayn.

## 5. Cohérence technique

- chapitre I : niveau 1 → 2 ;
- chapitre II : niveau 2 → 3 ;
- chapitre III : niveau 3 ;
- Gardien des Chutes : CA 15, 45 PV ;
- Kayn : 52 PV au début de la phase finale, retrait à 25 PV ;
- 1 action d'élite/round contre 3 PJ ;
- 2 actions d'élite/round contre 4–5 PJ ;
- PCW compris entre 0 et 5.

## 6. Dernière lecture

Faire une lecture page par page en se posant une seule question :

> « Est-ce que le MJ peut jouer cette page sans devoir retourner chercher une information essentielle ailleurs ? »

Si la réponse est non, ajouter un renvoi clair ou déplacer l'information.
