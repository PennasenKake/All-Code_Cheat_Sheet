#!/usr/bin/env python3
"""
Rakentaa tags.md-sivun, joka listaa kaikki cheat sheet -tiedostot ryhmiteltyna
niiden <!-- tags: ... --> -kommenttien perusteella (ks. scripts/add_tags.py).

Kaytto:
    python3 scripts/add_tags.py            # lisaa tagit ensin
    python3 scripts/generate_tags_page.py  # rakentaa tags.md niista
"""
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TAGS_PAGE = ROOT / "tags.md"

SKIP_DIRS = {".git", ".github", "scripts", "_site", "site"}
TAG_RE = re.compile(r"^<!--\s*tags:\s*(.+?)\s*-->\s*$", re.IGNORECASE)
HEADING_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)


def read_tags_and_title(md_path: Path):
    text = md_path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    tags = []
    if lines:
        m = TAG_RE.match(lines[0].strip())
        if m:
            tags = [t.strip() for t in m.group(1).split(",") if t.strip()]
    heading_match = HEADING_RE.search(text)
    title = heading_match.group(1).strip() if heading_match else md_path.stem
    return tags, title


def main():
    by_tag = defaultdict(list)

    for md_path in sorted(ROOT.rglob("*.md")):
        rel_parts = md_path.relative_to(ROOT).parts
        if any(part in SKIP_DIRS for part in rel_parts):
            continue
        if md_path.name == "tags.md":
            continue
        tags, title = read_tags_and_title(md_path)
        rel = md_path.relative_to(ROOT).as_posix()
        for tag in tags:
            by_tag[tag].append((title, rel))

    lines = [
        "# Tunnisteet",
        "",
        "Kaikki muistilaput ryhmiteltyna tunnisteiden mukaan. "
        "Tunnisteet generoidaan automaattisesti komennolla "
        "`python3 scripts/add_tags.py` ja tama sivu komennolla "
        "`python3 scripts/generate_tags_page.py`.",
        "",
    ]

    for tag in sorted(by_tag):
        lines.append(f"## {tag}")
        lines.append("")
        for title, rel in sorted(by_tag[tag]):
            lines.append(f"- [{title}]({rel})")
        lines.append("")

    TAGS_PAGE.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"tags.md rakennettu, {len(by_tag)} tunnistetta.")


if __name__ == "__main__":
    main()
