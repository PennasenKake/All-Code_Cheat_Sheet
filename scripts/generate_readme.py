#!/usr/bin/env python3
"""
Regeneroi README.md:n sisallysluettelo-osion automaattisesti kansiorakenteen
perusteella, jotta lista ei paase vanhenemaan kun tiedostoja lisataan/poistetaan.

README.md:ssa taytyy olla merkinnat:

    <!-- TOC:START -->
    ...
    <!-- TOC:END -->

Kaikki naiden merkintojen valissa oleva sisalto korvataan. Muu README:n sisalto
(otsikko, kuvausteksti, "Muuta"-osio ym.) sailyy koskemattomana.

Kaytto:
    python3 scripts/generate_readme.py
"""
import re
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

SKIP_DIRS = {".git", ".github", "scripts", "_site", "site", "_to_delete", "_to_delete_trash"}
SKIP_FILES = {"tags.md", "requirements.txt", ".gitattributes"}
CONTENT_EXTS = {".md", ".txt"}

START = "<!-- TOC:START -->"
END = "<!-- TOC:END -->"

TAG_COMMENT_RE = re.compile(r"^<!--\s*tags:.*-->\s*$", re.IGNORECASE)


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
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return path.stem


def build_dir_tree(files, base: Path) -> dict:
    """Sama sisakkainen hakemistopuu kuin generate_sidebar.py:ssa, jotta
    sisallysluettelo ryhmittelee alikansiot (esim. Vinkit/AI-ML) omiksi
    otsikoikseen litean listan sijaan."""
    tree: dict = {}
    for f in files:
        parts = f.relative_to(base).parts
        node = tree
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        node.setdefault("__files__", []).append(f)
    return tree


def emit_tree(node: dict, depth: int, lines: list) -> None:
    heading_level = min(depth + 3, 6)  # d.name on ###, alikansiot ####, #####...
    file_items = []
    for f in node.get("__files__", []):
        rel = f.relative_to(ROOT).as_posix()
        href = quote(rel, safe="/")
        title = first_heading_or_name(f)
        file_items.append((title, href))
    for title, href in sorted(file_items, key=lambda t: t[0].lower()):
        lines.append(f"- [{title}]({href})")
    if file_items:
        lines.append("")
    for dirname in sorted(k for k in node if k != "__files__"):
        lines.append(f"{'#' * heading_level} {dirname}\n")
        emit_tree(node[dirname], depth + 1, lines)


def build_toc() -> str:
    top_dirs = sorted(
        p for p in ROOT.iterdir()
        if p.is_dir() and p.name not in SKIP_DIRS and not p.name.startswith(".")
    )

    lines = []
    for d in top_dirs:
        files = sorted(
            p for p in d.rglob("*")
            if p.is_file()
            and p.suffix.lower() in CONTENT_EXTS
            and p.name not in SKIP_FILES
        )
        lines.append(f"### {d.name}\n")
        if not files:
            lines.append("Ei viela sisaltoa.\n")
            continue
        tree = build_dir_tree(files, d)
        emit_tree(tree, 1, lines)

    return "\n".join(lines).rstrip() + "\n"


def main():
    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise SystemExit(
            f"README.md:sta puuttuu {START} / {END} -merkinnat. "
            "Lisaa ne kasin sisallysluettelo-osion ymparille kertaalleen ensin."
        )

    toc = build_toc()
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    replacement = f"{START}\n\n{toc}\n{END}"
    new_text = pattern.sub(replacement, text)

    if new_text != text:
        README.write_text(new_text, encoding="utf-8")
        print("README.md paivitetty.")
    else:
        print("README.md oli jo ajan tasalla.")


if __name__ == "__main__":
    main()
