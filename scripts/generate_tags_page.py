#!/usr/bin/env python3
"""
Rakentaa tags.md-sivun, joka listaa kaikki cheat sheet -tiedostot ryhmiteltyna
niiden <!-- tags: ... --> -kommenttien perusteella (ks. scripts/add_tags.py).

Kaytto:
    python3 scripts/add_tags.py            # lisaa tagit ensin
    python3 scripts/generate_tags_page.py  # rakentaa tags.md niista
"""
import json
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
TAGS_PAGE = ROOT / "tags.md"
TAGS_JSON = ROOT / "tags.json"

SKIP_DIRS = {".git", ".github", "scripts", "_site", "site", "_to_delete", "_to_delete_trash"}
TAG_RE = re.compile(r"^<!--\s*tags:\s*(.+?)\s*-->\s*$", re.IGNORECASE)
HEADING_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)

# vastaa docsifyn omaa otsikko-id:n muodostustapaa (ks. generate_categories.py)
_SLUG_PUNCT_RE = re.compile(
    "[ -⁯⸀-⹿\\\\'!\"#$%&()*+,./:;<=>?@\\[\\]^`{|}~]"
)


def docsify_slugify(text: str) -> str:
    slug = text.strip().lower()
    slug = _SLUG_PUNCT_RE.sub("", slug)
    slug = re.sub(r"\s", "-", slug)
    slug = re.sub(r"^(\d)", r"_\1", slug)
    return slug


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
    categories_by_tag = defaultdict(set)

    for md_path in sorted(ROOT.rglob("*.md")):
        rel_parts = md_path.relative_to(ROOT).parts
        if any(part in SKIP_DIRS for part in rel_parts):
            continue
        if md_path.name == "tags.md":
            continue
        tags, title = read_tags_and_title(md_path)
        rel = md_path.relative_to(ROOT).as_posix()
        # juuritason kansio (esim. "Python", "Vinkit") - kaytetaan
        # tags.md-sivun kategoriasuodattimeen, jotta tagipilvea voi
        # rajata "vain nama kategoriat" ilman tekstihakua
        top_category = rel_parts[0] if rel_parts else None
        for tag in tags:
            by_tag[tag].append((title, rel))
            if top_category:
                categories_by_tag[tag].add(top_category)

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
            lines.append(f"- [{title}]({quote(rel, safe='/')})")
        lines.append("")

    TAGS_PAGE.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    # tags.json: kevyt data etusivun/tags-sivun JS-tagipilvea varten.
    # "cats" listaa juuritason kategoriat (kielet/Vinkit) joissa tama
    # tagi esiintyy - tags.md:n kategoriasuodatin kayttaa tata.
    # "pages" listaa jokaisen tagatun sivun otsikon+href:in - sisaltosivun
    # "Aiheeseen liittyvat" -osio (ks. index.html plugins-taulukko) kayttaa
    # tata loytaakseen muut samalla tagilla merkityt sivut ilman erillista
    # hakua/indeksia.
    tag_list = [
        {
            "tag": tag,
            "count": len(by_tag[tag]),
            "anchor": "#/tags?id=" + docsify_slugify(tag),
            "cats": sorted(categories_by_tag[tag]),
            "pages": [
                {"title": title, "href": "#/" + quote(rel, safe="/")}
                for title, rel in sorted(by_tag[tag])
            ],
        }
        for tag in sorted(by_tag)
    ]
    tag_list.sort(key=lambda t: t["count"], reverse=True)
    TAGS_JSON.write_text(json.dumps(tag_list, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"tags.md rakennettu, {len(by_tag)} tunnistetta.")


if __name__ == "__main__":
    main()
