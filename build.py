#!/usr/bin/env python3
"""
Build skript pro Explainer blog.
Konvertuje .md články z _articles/ na HTML stránky v site/.

Použití:
    python build.py          # Buildne celý web
    python build.py --watch  # Sleduje změny a přebuilďuje

Každý .md soubor v _articles/ musí mít YAML frontmatter:
---
title: Titulek článku
date: 2026-03-25
image: sora-konec-ilustrace.png
source_name: Název zdroje
source_url: https://example.com/zdroj
excerpt: Krátký popis pro homepage (volitelné)
---

Obsah článku v markdownu...
"""

import os
import re
import sys
import html
import shutil
from pathlib import Path
from datetime import datetime

# Cesty
BASE_DIR = Path(__file__).parent
ARTICLES_DIR = BASE_DIR / "_articles"
SITE_DIR = BASE_DIR / "site"
ARTICLES_OUT = SITE_DIR / "articles"
IMAGES_OUT = SITE_DIR / "images"

# České měsíce
MONTHS_CS = {
    1: "ledna", 2: "února", 3: "března", 4: "dubna",
    5: "května", 6: "června", 7: "července", 8: "srpna",
    9: "září", 10: "října", 11: "listopadu", 12: "prosince"
}


def format_date_cs(date: datetime) -> str:
    """Formátuje datum česky: '25. března 2026'."""
    return f"{date.day}. {MONTHS_CS[date.month]} {date.year}"


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parsuje YAML frontmatter z .md souboru. Vrací (metadata, body)."""
    if not content.startswith("---"):
        return {}, content

    end = content.find("---", 3)
    if end == -1:
        return {}, content

    fm_text = content[3:end].strip()
    body = content[end + 3:].strip()

    meta = {}
    for line in fm_text.split("\n"):
        line = line.strip()
        if ":" in line:
            key, _, value = line.partition(":")
            val = value.strip().strip('"').strip("'")
            val = val.replace('\\"', '"').replace("\\'", "'")
            meta[key.strip()] = val

    return meta, body


def md_to_html(text: str) -> str:
    """Jednoduchý markdown → HTML konvertor (odstavce)."""
    paragraphs = re.split(r'\n\s*\n', text.strip())
    html_parts = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        # Inline formátování
        p = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', p)
        p = re.sub(r'\*(.+?)\*', r'<em>\1</em>', p)
        p = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', p)
        # Odstavec
        p = p.replace("\n", " ")
        html_parts.append(f"<p>{p}</p>")
    return "\n".join(html_parts)


def make_slug(filename: str) -> str:
    """Vytvoří slug z názvu souboru."""
    return Path(filename).stem


def build_article_page(meta: dict, body_html: str, slug: str) -> str:
    """Sestaví kompletní HTML stránku článku."""
    title = html.escape(meta.get("title", "Bez názvu"))
    date_str = meta.get("date", "")
    image = meta.get("image", "")
    source_name = meta.get("source_name", "")
    source_url = meta.get("source_url", "")

    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        date_formatted = format_date_cs(date_obj)
    except (ValueError, TypeError):
        date_formatted = date_str

    image_html = ""
    if image:
        image_html = f'<img src="../images/{html.escape(image)}" alt="{title}" class="article-hero">'

    source_html = ""
    if source_name and source_url:
        source_html = f'''<div class="article-source">
    Zdroj: <a href="{html.escape(source_url)}" target="_blank" rel="noopener">{html.escape(source_name)}</a>
</div>'''
    elif source_name:
        source_html = f'<div class="article-source">Zdroj: {html.escape(source_name)}</div>'

    return f"""<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — AI Inspiruj.se</title>
    <link rel="stylesheet" href="../style.css">
    <meta property="og:title" content="{title}">
    <meta property="og:type" content="article">
    {f'<meta property="og:image" content="images/{html.escape(image)}">' if image else ''}
</head>
<body>
    <header class="site-header">
        <h1><a href="../">AI Inspiruj.se</a></h1>
        <p class="tagline">AI svět v kontextu</p>
    </header>
    <main>
        <a href="../" class="back-link">&larr; Zpět na přehled</a>
        <article>
            <div class="article-header">
                <span class="date">{date_formatted}</span>
                <h1>{title}</h1>
            </div>
            {image_html}
            <div class="article-body">
                {body_html}
            </div>
            {source_html}
        </article>
    </main>
    <footer class="site-footer">
        <a href="https://inspiruj.se">Inspiruj.se</a> &middot; AI vzdělávání pro firmy
    </footer>
</body>
</html>"""


def build_index(articles: list[dict]) -> str:
    """Sestaví index.html s přehledem článků."""
    # Seřadit od nejnovějšího
    articles.sort(key=lambda a: a.get("date", ""), reverse=True)

    items_html = ""
    for a in articles:
        title = html.escape(a.get("title", "Bez názvu"))
        slug = a["slug"]
        date_str = a.get("date", "")
        excerpt = html.escape(a.get("excerpt", ""))
        image = a.get("image", "")

        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            date_formatted = format_date_cs(date_obj)
        except (ValueError, TypeError):
            date_formatted = date_str

        thumb_html = ""
        if image:
            thumb_html = f'<a href="articles/{slug}.html"><img src="images/{html.escape(image)}" alt="{title}" class="thumb"></a>'

        items_html += f"""
        <li>
            {thumb_html}
            <span class="date">{date_formatted}</span>
            <h2><a href="articles/{slug}.html">{title}</a></h2>
            {f'<p class="excerpt">{excerpt}</p>' if excerpt else ''}
        </li>"""

    return f"""<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Inspiruj.se — AI svět v kontextu</title>
    <link rel="stylesheet" href="style.css">
    <meta property="og:title" content="AI Inspiruj.se">
    <meta property="og:description" content="AI svět v kontextu. Explainer články o umělé inteligenci.">
    <link rel="alternate" type="application/rss+xml" title="AI Inspiruj.se" href="feed.xml">
</head>
<body>
    <header class="site-header">
        <h1><a href="./">AI Inspiruj.se</a></h1>
        <p class="tagline">AI svět v kontextu</p>
    </header>
    <main>
        <ul class="article-list">{items_html}
        </ul>
    </main>
    <footer class="site-footer">
        <a href="https://inspiruj.se">Inspiruj.se</a> &middot; AI vzdělávání pro firmy
    </footer>
</body>
</html>"""


def build_rss(articles: list[dict], site_url: str = "https://ai.inspiruj.se") -> str:
    """Generuje RSS feed."""
    articles.sort(key=lambda a: a.get("date", ""), reverse=True)

    items = ""
    for a in articles[:20]:
        title = html.escape(a.get("title", ""))
        slug = a["slug"]
        excerpt = html.escape(a.get("excerpt", ""))
        date_str = a.get("date", "")
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            pub_date = date_obj.strftime("%a, %d %b %Y 00:00:00 +0100")
        except (ValueError, TypeError):
            pub_date = ""

        items += f"""
    <item>
        <title>{title}</title>
        <link>{site_url}/articles/{slug}.html</link>
        <description>{excerpt}</description>
        <pubDate>{pub_date}</pubDate>
        <guid>{site_url}/articles/{slug}.html</guid>
    </item>"""

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
    <title>AI Inspiruj.se</title>
    <link>{site_url}</link>
    <description>AI svět v kontextu. Explainer články o umělé inteligenci.</description>
    <language>cs</language>
    <atom:link href="{site_url}/feed.xml" rel="self" type="application/rss+xml"/>
    {items}
</channel>
</rss>"""


def copy_images():
    """Zkopíruje obrázky ze složky Explainer do site/images/."""
    # Hledáme PNG/JPG soubory v kořenové složce
    for ext in ("*.png", "*.jpg", "*.jpeg", "*.webp"):
        for img in BASE_DIR.glob(ext):
            dest = IMAGES_OUT / img.name
            if not dest.exists() or img.stat().st_mtime > dest.stat().st_mtime:
                shutil.copy2(img, dest)
                print(f"  📷 {img.name}")


def build():
    """Hlavní build funkce."""
    print("🔨 Building Explainer blog...")

    # Zajisti adresáře
    ARTICLES_OUT.mkdir(parents=True, exist_ok=True)
    IMAGES_OUT.mkdir(parents=True, exist_ok=True)

    # Kopíruj obrázky
    print("\nObrázky:")
    copy_images()

    # Zpracuj články
    print("\nČlánky:")
    articles_meta = []

    if not ARTICLES_DIR.exists():
        ARTICLES_DIR.mkdir()
        print("  (žádné články v _articles/)")
    else:
        for md_file in sorted(ARTICLES_DIR.glob("*.md")):
            content = md_file.read_text(encoding="utf-8")
            meta, body = parse_frontmatter(content)

            if not meta.get("title"):
                print(f"  ⚠️  {md_file.name}: chybí title ve frontmatter, přeskakuji")
                continue

            slug = make_slug(md_file.name)
            body_html = md_to_html(body)

            # Generuj excerpt z prvního odstavce pokud chybí
            if not meta.get("excerpt"):
                first_p = body.split("\n\n")[0] if body else ""
                meta["excerpt"] = first_p[:200].rstrip() + ("..." if len(first_p) > 200 else "")

            # Zapiš HTML článku
            article_html = build_article_page(meta, body_html, slug)
            out_path = ARTICLES_OUT / f"{slug}.html"
            out_path.write_text(article_html, encoding="utf-8")
            print(f"  ✅ {slug}.html ({meta.get('title', '')[:50]})")

            articles_meta.append({**meta, "slug": slug})

    # Generuj index
    index_html = build_index(articles_meta)
    (SITE_DIR / "index.html").write_text(index_html, encoding="utf-8")
    print(f"\n📄 index.html ({len(articles_meta)} článků)")

    # Generuj RSS
    rss = build_rss(articles_meta)
    (SITE_DIR / "feed.xml").write_text(rss, encoding="utf-8")
    print("📡 feed.xml")

    print(f"\n✨ Hotovo! Výstup v {SITE_DIR}/")


if __name__ == "__main__":
    if "--watch" in sys.argv:
        import time
        print("👀 Watching for changes... (Ctrl+C to stop)")
        last_build = 0
        while True:
            # Kontroluj změny v _articles/ a obrázcích
            latest = 0
            for f in ARTICLES_DIR.glob("*.md"):
                latest = max(latest, f.stat().st_mtime)
            for ext in ("*.png", "*.jpg"):
                for f in BASE_DIR.glob(ext):
                    latest = max(latest, f.stat().st_mtime)

            if latest > last_build:
                build()
                last_build = time.time()
            time.sleep(2)
    else:
        build()
