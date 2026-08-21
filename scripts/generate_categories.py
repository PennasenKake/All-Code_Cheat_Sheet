#!/usr/bin/env python3
"""
Generoi categories.json: yhden rivin per juuritason kansio (esim. Python,
JavaScript, SQL...), sisaltaen oikean tiedostomaaran ja linkin ensimmaiseen
sisaltoon. Etusivun ("_coverpage.md") kategoriakortit lukevat taman
tiedoston suoraan selaimessa, joten kortit pysyvat aina ajan tasalla eika
niita tarvitse pitaa kasin yllä.

Sama kansioryhmittely kuin generate_readme.py:ssa, jotta lukumaarat ja
linkit tasmaavat sisallysluetteloon.

Kaytto:
    python3 scripts/generate_categories.py
"""
import json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent

SKIP_DIRS = {".git", ".github", "scripts", "_site", "site"}
SKIP_FILES = {"tags.md", "requirements.txt", ".gitattributes"}
CONTENT_EXTS = {".md", ".txt"}

# kansionimi -> (nayttonimi, lyhenne-badge, aksenttivari)
DISPLAY = {
    "Bash":         ("Bash",        "sh", "#f59e0b"),
    "Docker_":      ("Docker",      "Do", "#22d3ee"),
    "Excelit":      ("Excel",       "Xl", "#22c55e"),
    "Html":         ("HTML & CSS",  "H",  "#fb923c"),
    "Java":         ("Java",        "Jv", "#f97316"),
    "JavaScript":   ("JavaScript",  "JS", "#eab308"),
    "MFK kaavat":   ("MFK-kaavat",  "fx", "#38bdf8"),
    "Python":       ("Python",      "Py", "#3b82f6"),
    "SQL":          ("SQL",         "Db", "#a855f7"),
}


def build_categories():
    top_dirs = sorted(
        p for p in ROOT.iterdir()
        if p.is_dir() and p.name not in SKIP_DIRS and not p.name.startswith(".")
    )

    categories = []
    for d in top_dirs:
        files = sorted(
            p for p in d.rglob("*")
            if p.is_file()
            and p.suffix.lower() in CONTENT_EXTS
            and p.name not in SKIP_FILES
        )
        if not files:
            continue
        display, badge, color = DISPLAY.get(d.name, (d.name, d.name[:2], "#6366f1"))
        first = files[0].relative_to(ROOT).as_posix()
        # docsify purkaa hash-reitit decodeURIComponentilla, joten polun
        # välilyönnit ym. pitää enkoodata (mutta ei kauttaviivoja)
        href = "#/" + quote(first, safe="/")
        categories.append({
            "name": d.name,
            "display": display,
            "badge": badge,
            "color": color,
            "count": len(files),
            "href": href,
        })
    return categories


def main():
    categories = build_categories()
    out = ROOT / "categories.json"
    new_text = json.dumps(categories, ensure_ascii=False, indent=2) + "\n"
    old_text = out.read_text(encoding="utf-8") if out.exists() else None
    if new_text != old_text:
        out.write_text(new_text, encoding="utf-8")
        print(f"categories.json päivitetty ({len(categories)} kategoriaa).")
    else:
        print("categories.json oli jo ajan tasalla.")


if __name__ == "__main__":
    main()
