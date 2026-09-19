from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HOMEBREWERY = ROOT / "homebrewery"

SOURCE_BASE = HOMEBREWERY / "prologue.md"
CHAPTER_2 = HOMEBREWERY / "chapters" / "02-chutes-de-brume.md"
CHAPTER_3 = HOMEBREWERY / "chapters" / "03-assaut-du-temple.md"
ANNEXES = HOMEBREWERY / "annexes.md"
OUTPUT = HOMEBREWERY / "prologue-complet.md"

BUILD_MARKER = "<!-- BUILD:END_PROLOGUE_BASE -->"


def read(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {path}")
    return path.read_text(encoding="utf-8").strip()


def remove_trailing_page_break(text: str) -> str:
    """Évite les doubles pages blanches entre deux modules."""
    return re.sub(r"\n\\page\s*$", "", text.rstrip())


def main() -> None:
    base = read(SOURCE_BASE)

    if BUILD_MARKER not in base:
        raise RuntimeError(
            "Le marqueur de fin de base n'a pas été trouvé dans homebrewery/prologue.md."
        )

    # prologue.md contient uniquement la couverture, l'introduction et le chapitre I.
    # Le marqueur explicite ci-dessous sépare cette base des modules ajoutés au build.
    front_and_chapter_1 = base.split(BUILD_MARKER, 1)[0]
    front_and_chapter_1 = remove_trailing_page_break(front_and_chapter_1)

    modules = [
        front_and_chapter_1,
        read(CHAPTER_2),
        read(CHAPTER_3),
        read(ANNEXES),
    ]

    modules = [remove_trailing_page_break(module) for module in modules]

    manuscript = "\n\n\\page\n\n".join(modules).rstrip() + "\n"

    OUTPUT.write_text(manuscript, encoding="utf-8")

    page_breaks = manuscript.count("\\page")
    print(f"Manuscrit généré : {OUTPUT.relative_to(ROOT)}")
    print(f"Taille : {len(manuscript):,} caractères")
    print(f"Sauts de page explicites : {page_breaks}")


if __name__ == "__main__":
    main()
