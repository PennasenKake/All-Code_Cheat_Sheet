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
import re
from pathlib import Path
from urllib.parse import quote

TAG_COMMENT_RE = re.compile(r"^<!--\s*tags:.*-->\s*$", re.IGNORECASE)
HEADING_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)


def strip_leading_comment(text: str) -> str:
    lines = text.splitlines()
    while lines and TAG_COMMENT_RE.match(lines[0].strip()):
        lines.pop(0)
    return "\n".join(lines)


def first_heading_or_name(path: Path) -> str:
    try:
        text = strip_leading_comment(path.read_text(encoding="utf-8", errors="ignore"))
    except OSError:
        return path.stem
    m = HEADING_RE.search(text)
    if m:
        return m.group(1).strip()
    return path.stem

ROOT = Path(__file__).resolve().parent.parent

SKIP_DIRS = {".git", ".github", "scripts", "_site", "site", "_to_delete", "_to_delete_trash"}
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
        preview = []
        for f in files[:4]:
            title = first_heading_or_name(f)
            if title not in preview:
                preview.append(title)
        categories.append({
            "name": d.name,
            "display": display,
            "badge": badge,
            "color": color,
            "count": len(files),
            "href": href,
            "preview": preview,
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
