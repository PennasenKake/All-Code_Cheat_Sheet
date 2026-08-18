#!/usr/bin/env python3
"""
Generoi jokaiselle lahdekoodi-/kuvatiedostolle (esim. .py, .js, .html, .css,
.java, .jpg) kevyen "katseluvarjostimen": <tiedosto>.md, joka sisaltaa
alkuperaisen sisallon syntaksivaritettyna koodilohkona (tai kuvana), jotta
tiedosto renderoityy Docsify-sivustolla siisteina sivuna eika vain raakana
tekstina.

Alkuperainen tiedosto pysyy aina totuuden lahteena; wrapper-sivu
generoidaan aina uudelleen kokonaan (ei kasin muokattavissa). Jos
alkuperainen tiedosto poistetaan, myos sen wrapper-sivu poistetaan
automaattisesti seuraavalla ajolla.

Kaytto:
    python3 scripts/generate_code_pages.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKIP_DIRS = {".git", ".github", "scripts", "_site", "site"}

# paate -> (kieli fenced-koodilohkoa varten)
CODE_LANGS = {
    ".py": "python",
    ".js": "javascript",
    ".jsx": "jsx",
    ".ts": "typescript",
    ".java": "java",
    ".cs": "csharp",
    ".html": "html",
    ".htm": "html",
    ".css": "css",
    ".sh": "bash",
    ".json": "json",
    ".yml": "yaml",
    ".yaml": "yaml",
}
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"}

MAX_EMBED_BYTES = 200_000  # isommat (esim. valmiiksi renderoidut export-tiedostot) ohitetaan

# repon JUURESSA olevat infratiedostot (ei sisallytetä koodisivuiksi) -
# huom: polku tarkistetaan vain juuresta, joten esim. Html/.../index.html
# (oikea esimerkkitiedosto) käsitellään edelleen normaalisti
ROOT_SKIP_FILES = {"index.html"}

STOP_WORDS = {
    "readme", "notes", "esimerkit", "esimerkkeja", "esimerkkejä", "projects",
    "projektit", "perusteet", "cheat", "sheet", "kaavat",
}


def slug(word: str) -> str:
    word = word.lower()
    word = word.replace("ä", "a").replace("ö", "o").replace("å", "a")
    word = re.sub(r"[^a-z0-9]+", "-", word).strip("-")
    return word


def guess_tags(src_path: Path, lang: str | None = None) -> list[str]:
    """Tagit koodisivuille: kieli + kansiopolku. EI tiedostonimen sanapilkontaa,
    koska esim. 'loops_and_conditions.py' -> 'and' on hyodyton, liian yleinen tagi.
    (Kasikirjoitetuille cheat sheeteille add_tags.py silti pilkkoo tiedostonimen,
    koska ne ovat harvoja ja nimetty kuvaavasti aihealueen mukaan.)"""
    rel = src_path.relative_to(ROOT)
    parts = list(rel.parts[:-1])
    candidates = ([lang] if lang else []) + [slug(p) for p in parts]
    tags = []
    for c in candidates:
        if not c or c in STOP_WORDS or c in tags:
            continue
        tags.append(c)
    return tags[:6]


def wrapper_path(src: Path) -> Path:
    return src.with_name(src.name + ".md")


def build_code_page(src: Path, lang: str) -> str:
    tags = guess_tags(src, lang)
    tag_line = f"<!-- tags: {', '.join(tags)} -->\n\n" if tags else ""
    text = src.read_text(encoding="utf-8", errors="replace")
    # varmistetaan ettei tiedoston oma sisalto voi katkaista koodilohkoa
    fence = "```"
    while fence in text:
        fence += "`"
    rel = src.relative_to(ROOT).as_posix()
    return (
        f"{tag_line}"
        f"# {src.name}\n\n"
        f"[Näytä alkuperäinen tiedosto GitHubissa]({rel})\n\n"
        f"{fence}{lang}\n"
        f"{text.rstrip(chr(10))}\n"
        f"{fence}\n"
    )


def build_image_page(src: Path) -> str:
    tags = guess_tags(src, "kuva")
    tag_line = f"<!-- tags: {', '.join(tags)} -->\n\n" if tags else ""
    rel = src.relative_to(ROOT).as_posix()
    return f"{tag_line}# {src.name}\n\n![{src.name}]({rel})\n"


def iter_source_files():
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT)
        rel_parts = rel.parts
        if any(part in SKIP_DIRS or part.startswith(".") for part in rel_parts):
            continue
        if len(rel_parts) == 1 and rel_parts[0] in ROOT_SKIP_FILES:
            continue
        ext = p.suffix.lower()
        if ext == ".md" and not p.name.endswith(".md.md"):
            # tunnista onko tama itse asiassa "<jotain>.<ext>.md" -wrapper
            # (kasitellaan wrapperit erikseen alla, ei lahdetiedostoina)
            continue
        yield p


def main():
    created, updated, unchanged, skipped_size, removed = [], [], [], [], []

    live_wrappers = set()

    for src in sorted(iter_source_files()):
        ext = src.suffix.lower()
        if ext not in CODE_LANGS and ext not in IMAGE_EXTS:
            continue

        wrapper = wrapper_path(src)
        live_wrappers.add(wrapper)

        if src.stat().st_size > MAX_EMBED_BYTES:
            skipped_size.append(src.relative_to(ROOT))
            continue

        if ext in IMAGE_EXTS:
            new_content = build_image_page(src)
        else:
            new_content = build_code_page(src, CODE_LANGS[ext])

        old_content = wrapper.read_text(encoding="utf-8") if wrapper.exists() else None
        if new_content == old_content:
            unchanged.append(wrapper.relative_to(ROOT))
            continue
        wrapper.write_text(new_content, encoding="utf-8")
        (updated if old_content is not None else created).append(wrapper.relative_to(ROOT))

    # poista orvoiksi jaaneet wrapperit (lahdetiedosto ei ole enaa olemassa)
    for candidate in ROOT.rglob("*.md"):
        rel_parts = candidate.relative_to(ROOT).parts
        if any(part in SKIP_DIRS or part.startswith(".") for part in rel_parts):
            continue
        stem_ext = Path(candidate.stem).suffix.lower()  # esim. "hello_world.py" -> ".py"
        if stem_ext not in CODE_LANGS and stem_ext not in IMAGE_EXTS:
            continue
        if candidate not in live_wrappers:
            candidate.unlink()
            removed.append(candidate.relative_to(ROOT))

    print(f"Uusia sivuja: {len(created)}, päivitettyjä: {len(updated)}, "
          f"ennallaan: {len(unchanged)}, liian isoja ohitettu: {len(skipped_size)}, "
          f"orpoja poistettu: {len(removed)}")
    for label, items in (("+ ", created), ("~ ", updated), ("! liian iso, ohitettu: ", skipped_size), ("- poistettu: ", removed)):
        for i in items:
            print(f"  {label}{i}")


if __name__ == "__main__":
    main()
