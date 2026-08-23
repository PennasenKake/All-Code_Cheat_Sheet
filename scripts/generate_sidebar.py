#!/usr/bin/env python3
"""
Regeneroi Docsify-sivuston _sidebar.md-tiedoston kansiorakenteen perusteella,
jotta navigointipalkki ei paase vanhenemaan kun tiedostoja lisataan/poistetaan.

Kaytto:
    python3 scripts/generate_sidebar.py
"""
import re
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
SIDEBAR = ROOT / "_sidebar.md"

SKIP_DIRS = {".git", ".github", "scripts", "_site", "site", "_to_delete", "_to_delete_trash"}
SKIP_FILES = {"tags.md", "requirements.txt", ".gitattributes"}
CONTENT_EXTS = {".md", ".txt"}


def strip_leading_comment(text: str) -> str:
    lines = text.splitlines()
    while lines and lines[0].strip().startswith("<!--"):
        lines.pop(0)
    return "\n".join(lines)


def first_heading_or_name(path: Path) -> str:
    try:
        text = strip_leading_comment(path.read_text(encoding="utf-8", errors="ignore"))
    except OSError:
        return path.stem
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return path.stem


def build_sidebar() -> str:
    top_dirs = sorted(
        p for p in ROOT.iterdir()
        if p.is_dir() and p.name not in SKIP_DIRS and not p.name.startswith(".")
    )

    lines = ["- [Etusivu](/)", "- [Tunnisteet (tags)](tags.md)", ""]

    for d in top_dirs:
        files = sorted(
            p for p in d.rglob("*")
            if p.is_file()
            and p.suffix.lower() in CONTENT_EXTS
            and p.name not in SKIP_FILES
        )
        if not files:
            continue
        lines.append(f"- {d.name}")
        for f in files:
            rel = f.relative_to(ROOT).as_posix()
            href = quote(rel, safe="/")
            title = first_heading_or_name(f)
            lines.append(f"  - [{title}]({href})")

    return "\n".join(lines).rstrip() + "\n"


def main():
    new_content = build_sidebar()
    old_content = SIDEBAR.read_text(encoding="utf-8") if SIDEBAR.exists() else None
    if new_content != old_content:
        SIDEBAR.write_text(new_content, encoding="utf-8")
        print("_sidebar.md paivitetty.")
    else:
        print("_sidebar.md oli jo ajan tasalla.")


if __name__ == "__main__":
    main()
