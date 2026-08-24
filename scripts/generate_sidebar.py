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


def build_dir_tree(files, base: Path) -> dict:
    """Rakentaa sisakkaisen hakemistopuun tiedostoista (suhteessa base-kansioon),
    jotta alikansiot (esim. Vinkit/AI-ML, Html/Esimerkit/formsit) nakyvat
    sivupalkissa omina supistettavina ryhminaan sen sijaan etta kaikki
    tiedostot listattaisiin yhdessa litteassa listassa."""
    tree: dict = {}
    for f in files:
        parts = f.relative_to(base).parts
        node = tree
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        node.setdefault("__files__", []).append(f)
    return tree


def emit_tree(node: dict, depth: int, lines: list) -> None:
    indent = "  " * depth
    for dirname in sorted(k for k in node if k != "__files__"):
        lines.append(f"{indent}- {dirname}")
        emit_tree(node[dirname], depth + 1, lines)
    file_items = []
    for f in node.get("__files__", []):
        rel = f.relative_to(ROOT).as_posix()
        href = quote(rel, safe="/")
        title = first_heading_or_name(f)
        file_items.append((title, href))
    for title, href in sorted(file_items, key=lambda t: t[0].lower()):
        lines.append(f"{indent}- [{title}]({href})")


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
        tree = build_dir_tree(files, d)
        emit_tree(tree, 1, lines)

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
