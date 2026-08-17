#!/usr/bin/env python3
"""
Lisaa jokaisen cheat sheet -markdown-tiedoston ensimmaiselle riville nakymattoman
HTML-kommentin, jossa on kansiopolusta ja tiedostonimesta paateltyja tunnisteita
(tags), esim. <!-- tags: sql, join -->. Nama eivat nay renderoidyssa sivussa,
mutta scripts/generate_tags_page.py lukee ne ja rakentaa niista tags.md-sivun.

Ajo turvallinen useita kertoja: jos tiedostossa on jo tags-kommentti, sita ei
kosketa (poista rivi kasin, jos haluat generoida tagit uudelleen).

Kaytto:
    python3 scripts/add_tags.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKIP_DIRS = {".git", ".github", "scripts", "_site", "site"}
SKIP_FILES = {"tags.md", "_sidebar.md", "_coverpage.md"}

STOP_WORDS = {
    "readme", "notes", "esimerkit", "esimerkkeja", "esimerkkejä", "projects",
    "projektit", "perusteet", "cheat", "sheet", "kaavat",
}

TAG_RE = re.compile(r"^<!--\s*tags:\s*(.+?)\s*-->\s*$", re.IGNORECASE)


def slug(word: str) -> str:
    word = word.lower()
    word = word.replace("ä", "a").replace("ö", "o").replace("å", "a")
    word = re.sub(r"[^a-z0-9]+", "-", word).strip("-")
    return word


def guess_tags(md_path: Path) -> list[str]:
    rel = md_path.relative_to(ROOT)
    parts = list(rel.parts[:-1])
    stem = rel.stem

    candidates = [slug(p) for p in parts]
    candidates += [slug(w) for w in re.split(r"[_\-\s]+", stem)]

    tags = []
    for c in candidates:
        if not c or c in STOP_WORDS or c in tags:
            continue
        tags.append(c)
    return tags[:6]


def has_tag_comment(text: str) -> bool:
    first_line = text.splitlines()[0] if text else ""
    return bool(TAG_RE.match(first_line))


def add_tag_comment(md_path: Path) -> bool:
    text = md_path.read_text(encoding="utf-8")
    if has_tag_comment(text):
        return False
    tags = guess_tags(md_path)
    if not tags:
        return False
    comment = f"<!-- tags: {', '.join(tags)} -->\n"
    md_path.write_text(comment + text, encoding="utf-8")
    return True


def main():
    changed = []
    for md_path in sorted(ROOT.rglob("*.md")):
        rel_parts = md_path.relative_to(ROOT).parts
        if any(part in SKIP_DIRS for part in rel_parts):
            continue
        if md_path.name in SKIP_FILES:
            continue
        if add_tag_comment(md_path):
            changed.append(md_path.relative_to(ROOT))

    print(f"Lisattiin tagit {len(changed)} tiedostoon:")
    for c in changed:
        print(f"  {c}")


if __name__ == "__main__":
    main()
