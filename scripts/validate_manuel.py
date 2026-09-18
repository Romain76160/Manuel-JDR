from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "homebrewery" / "prologue-complet.md"

def count(pattern: str, text: str) -> int:
    return len(re.findall(pattern, text, flags=re.MULTILINE))

def main() -> int:
    if not MANUSCRIPT.exists():
        print("ERREUR : homebrewery/prologue-complet.md est introuvable.")
        return 1

    text = MANUSCRIPT.read_text(encoding="utf-8")
    errors = []
    warnings = []

    checks = {
        "ouverture chapitre I": count(r"\{\{chapter\s*\n\s*# Chapitre I\s*\n___", text),
        "ouverture chapitre II": count(r"\{\{chapter\s*\n\s*# Chapitre II\s*\n___", text),
        "ouverture chapitre III": count(r"\{\{chapter\s*\n\s*# Chapitre III\s*\n___", text),
        "ouverture annexes": count(r"\{\{chapter\s*\n\s*# Annexes\s*\n___", text),
    }

    for label, value in checks.items():
        if value != 1:
            errors.append(f"{label}: attendu 1, trouvé {value}")

    if re.search(r"\\page\s*\n\s*\\page", text):
        errors.append("double saut de page détecté")

    # Vérification simple des principaux blocs Homebrewery.
    for block in ["coverPage", "chapter", "note", "descriptive", "wuju", "darkin", "encounter"]:
        openings = len(re.findall(r"\{\{" + re.escape(block) + r"\b", text))
        # Les blocs Homebrewery se ferment tous par }} ; ce contrôle est volontairement simple.
        if openings and text.count("}}") < openings:
            errors.append(f"fermetures insuffisantes pour les blocs {block}")

    if "À reconstruire" in text or "TODO" in text:
        warnings.append("placeholder éditorial détecté (À reconstruire/TODO)")

    if "Temple Wuju de nuit, lanternes éteintes, Kayn sur les toits" in text:
        errors.append("ancienne direction visuelle du temple extérieur encore présente")

    print(f"Manuscrit : {MANUSCRIPT.relative_to(ROOT)}")
    print(f"Caractères : {len(text):,}")
    print(f"Sauts de page : {text.count('\\page')}")
    for label, value in checks.items():
        print(f"{label}: {value}")

    if warnings:
        print("\nAVERTISSEMENTS")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("\nERREURS")
        for error in errors:
            print(f"- {error}")
        return 1

    print("\nValidation structurelle : OK")
    return 0

if __name__ == "__main__":
    sys.exit(main())
