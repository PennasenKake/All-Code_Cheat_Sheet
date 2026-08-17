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

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

SKIP_DIRS = {".git", ".github", "scripts", "_site", "site"}
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
        for f in files:
            rel = f.relative_to(ROOT).as_posix()
            title = first_heading_or_name(f)
            lines.append(f"- [{title}]({rel})")
        lines.append("")

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
