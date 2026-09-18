#!/usr/bin/env python3
"""Télécharge les illustrations officielles Riot retenues pour le Manuel I.

Source principale : Legends of Runeterra Data Dragon (Riot Games).
Les fichiers *-full.png sont les illustrations complètes sans cadre ni texte.

Usage :
    python3 scripts/fetch_riot_assets.py
    python3 scripts/fetch_riot_assets.py --dry-run
"""

from __future__ import annotations

from pathlib import Path
import argparse
import urllib.request
import urllib.error

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "illustrations" / "riot"

BASES = [
    "https://dd.b.pvp.net/latest/set6/en_us/img/cards",
    "https://dd.b.pvp.net/latest/set6cde/en_us/img/cards",
]

ASSETS = {
    "master-yi-lor.png": "06IO008-full.png",
    "jun-the-prodigy.png": "06IO011-full.png",
    "ting-vastayan-disciple.png": "06IO014-full.png",
    "disciple-of-doran.png": "06IO001-full.png",
    "wuju-style.png": "06IO013-full.png",
    "mistfall.png": "06IO030-full.png",
    "momentous-choice.png": "06IO034-full.png",
    "utter-devastation.png": "06SI036-full.png",
    "kayn-lor.png": "06RU005-full.png",
    "rhaast.png": "06RU005T2-full.png",
    "xolaani.png": "06SH004T2-full.png",
    "darkin-bloodletters.png": "06SH004-full.png",
}

USER_AGENT = "Manuel-JDR-Wuju/1.0 (fan project; Riot Data Dragon assets)"


def fetch(url: str, destination: Path) -> bool:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            content_type = response.headers.get("Content-Type", "")
            if "image" not in content_type:
                return False
            destination.write_bytes(response.read())
            return True
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
        return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Affiche les URL sans télécharger")
    args = parser.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)

    failed: list[str] = []

    for local_name, remote_name in ASSETS.items():
        destination = OUT / local_name

        if args.dry_run:
            print(f"{local_name}:")
            for base in BASES:
                print(f"  {base}/{remote_name}")
            continue

        if destination.exists() and destination.stat().st_size > 0:
            print(f"[déjà présent] {destination.relative_to(ROOT)}")
            continue

        ok = False
        for base in BASES:
            url = f"{base}/{remote_name}"
            print(f"[essai] {url}")
            if fetch(url, destination):
                print(f"[ok] {destination.relative_to(ROOT)}")
                ok = True
                break

        if not ok:
            failed.append(local_name)
            if destination.exists():
                destination.unlink()

    if failed:
        print("\nIllustrations non récupérées :")
        for name in failed:
            print(f"- {name}")
        print("\nVérifier l'identifiant de carte ou le bundle Riot correspondant.")
        return 1

    print("\nTous les assets disponibles ont été récupérés.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
