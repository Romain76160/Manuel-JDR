#!/usr/bin/env python3
"""Contrôles de cohérence canonique et mécanique du Manuel I."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

FILES = {
    "c1": ROOT / "homebrewery" / "prologue.md",
    "c2": ROOT / "homebrewery" / "chapters" / "02-chutes-de-brume.md",
    "c3": ROOT / "homebrewery" / "chapters" / "03-assaut-du-temple.md",
    "annex": ROOT / "homebrewery" / "annexes.md",
    "bestiaire": ROOT / "manuel" / "prologue" / "bestiaire.md",
    "lore": ROOT / "lore" / "temple-wuju.md",
}

def read(key: str) -> str:
    return FILES[key].read_text(encoding="utf-8")

def require(text: str, pattern: str, label: str, errors: list[str]) -> None:
    if not re.search(pattern, text, flags=re.I | re.S):
        errors.append(f"manquant : {label}")

def forbid(text: str, pattern: str, label: str, errors: list[str]) -> None:
    if re.search(pattern, text, flags=re.I | re.S):
        errors.append(f"terme interdit : {label}")

def main() -> int:
    errors: list[str] = []
    c1, c2, c3 = read("c1"), read("c2"), read("c3")
    annex, bestiaire, lore = read("annex"), read("bestiaire"), read("lore")

    # Architecture canonique.
    require(lore, r"creusé dans une montagne", "Temple creusé dans la montagne", errors)
    for level in ["niveau supérieur", "niveau intermédiaire", "niveau inférieur"]:
        require(lore, re.escape(level), f"architecture {level}", errors)
    require(lore, r"Grottes des esprits", "connexion des Grottes des esprits", errors)
    forbid(lore, r"niveau\s*-4|niveau\s*-3|niveau\s*-2|niveau\s*-1|niveau\s*0", "ancienne architecture numérotée 0 à -4", errors)

    # Chapitre III.
    require(c3, r"52 PV", "Kayn commence le final à 52 PV", errors)
    require(c3, r"25 PV", "Kayn se retire à 25 PV", errors)
    require(c3, r"3 succès d'objectif", "victoire par 3 objectifs", errors)
    require(c3, r"niveau intermédiaire", "départ des PJ au niveau intermédiaire", errors)
    require(c3, r"niveau inférieur", "final au reliquaire du niveau inférieur", errors)

    # Bestiaire Kayn.
    require(bestiaire, r"À \*\*39 PV ou moins\*\*", "seuil d'éveil de Rhaast à 39 PV", errors)
    require(bestiaire, r"\+1d4 nécrotiques", "bonus de Rhaast", errors)

    # Chapitre II / PCW.
    require(c2, r"DD 16 [−-] PCW", "contact Xolaani DD 16-PCW", errors)
    require(annex, r"DD 13 [−-] PCW", "rite Gardien DD 13-PCW", errors)
    require(annex, r"CA\*\* 15|CA 15", "Gardien CA 15", errors)
    require(annex, r"PV\*\* 45|PV 45", "Gardien 45 PV", errors)
    require(annex, r"1d10 \+ 3", "Coup de jade 1d10+3", errors)
    require(annex, r"2d8", "Onde de brume 2d8", errors)

    # Progression.
    require(annex, r"Début du chapitre I\s*\|\s*1", "niveau 1 au début du chapitre I", errors)
    require(annex, r"Fin du chapitre I\s*\|\s*2", "niveau 2 fin chapitre I", errors)
    require(annex, r"Fin du chapitre II\s*\|\s*3", "niveau 3 fin chapitre II", errors)

    # Anciennes représentations interdites dans les textes de jeu.
    for label, text in [("chapitre I", c1), ("chapitre II", c2), ("chapitre III", c3)]:
        forbid(text, r"grande cour extérieure", f"{label}: grande cour extérieure", errors)
        forbid(text, r"niveau secret|cœur oublié|coeur oublié", f"{label}: niveau inventé", errors)

    # Kayn ne doit pas combattre les PJ au chapitre II.
    forbid(c2, r"combat (?:contre|avec) Kayn", "combat Kayn au chapitre II", errors)

    if errors:
        print("COHÉRENCE : ÉCHEC")
        for e in errors:
            print(f"- {e}")
        return 1

    print("COHÉRENCE : OK")
    print("- architecture à trois niveaux : supérieur / intermédiaire / inférieur + grottes")
    print("- Kayn 52 -> 25 PV, Rhaast à 39 PV")
    print("- Gardien 45 PV / CA 15 / 1d10+3 / 2d8")
    print("- Xolaani DD 16-PCW")
    print("- progression 1 -> 2 -> 3")
    return 0

if __name__ == "__main__":
    sys.exit(main())
