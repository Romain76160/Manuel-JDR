# Revue éditoriale V1 — Manuel I : L'Héritage du Wuju

Date : septembre 2026.

## Validé dans cette passe

### Structure
- couverture / introduction / chapitre I séparés proprement dans `prologue.md` ;
- anciens placeholders des chapitres II et III supprimés ;
- marqueur de build explicite `<!-- BUILD:END_PROLOGUE_BASE -->` ;
- une seule ouverture réelle pour chacun des chapitres II, III et les annexes ;
- aucun `À reconstruire` dans le manuscrit assemblé.

### Canon
- Temple Wuju harmonisé comme sanctuaire creusé dans la montagne ;
- anciennes descriptions de grande cour/pavillons extérieurs corrigées dans le chapitre I ;
- niveaux canoniques 0, -1, -2, -3, -4 maintenus ;
- aucun niveau « Cœur oublié » n'est canonique.

### Mécanique
Constantes vérifiées :
- Kayn : 52 PV au début du final, retrait à 25 PV ;
- Rhaast : seuil à 39 PV ;
- Gardien des Chutes : CA 15, 45 PV, 1d10+3, Onde 2d8 ;
- Transfuge : 58 PV de base / 48 PV pour 3 PJ ;
- Xolaani : DD 16 - PCW ;
- rite du Gardien : DD 13 - PCW ;
- progression : 1 -> 2 -> 3.

Le script `scripts/check_canon.py` sert désormais de garde-fou.

### Visuels
Intégrés :
- Master Yi — chapitre I ;
- Jun — chapitre II ;
- Kayn — chapitre III ;
- Xolaani — annexes.

Les concepts cartographiques générés ne sont pas considérés comme finaux tant qu'ils ne respectent pas `assets/cartes/VALIDATION.md`.

### Crédits
- notice fan Riot clarifiée ;
- artistes des quatre arts LoR intégrés crédités ;
- registre des sources conservé dans `assets/SOURCES_IMAGES.md`.

---

# Reste avant le premier PDF réellement présentable

## Bloquant
1. couverture originale finale ;
2. fonds de cartes canoniques sans texte généré ;
3. annotations joueurs / MJ déterministes ;
4. insertion de ces cartes dans les cinq emplacements déjà préparés.

## Contrôle de mise en page
Après insertion des cartes :
- débordements de colonnes ;
- titres orphelins ;
- tableaux coupés ;
- densité des pages ;
- lisibilité des crédits ;
- placement des images de chapitre ;
- pages blanches involontaires.

## Contrôle éditorial final
- harmoniser une dernière fois les voix de Yi, Jun, Cassian, Kayn, Rhaast et Xolaani ;
- réduire les répétitions sémantiques entre narration et annexes uniquement si elles gênent la lecture ;
- vérifier les renvois de table après pagination réelle.

---

# Commandes avant export

```bash
python3 scripts/build_manuel.py
python3 scripts/validate_manuel.py
python3 scripts/check_canon.py
```

Les deux validateurs doivent terminer sans erreur avant l'export PDF.

---

# État

Le contenu du Prologue est **jouable et structurellement stable**.

Le travail restant est principalement :
**cartographie finale -> couverture -> mise en page -> PDF test -> corrections visuelles**.
