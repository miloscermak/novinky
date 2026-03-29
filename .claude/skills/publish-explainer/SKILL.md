# Publish Explainer — publikační skill

Publikuje hotový explainer článek na ai.inspiruj.se (repo miloscermak/novinky).

## Trigger

Použij tento skill když uživatel řekne: "publikuj", "publish", "dej to ven", "nasaď článek", "publikuj článek", nebo když je článek hotový a připravený k publikaci.

## Předpoklady

V kořenové složce Explainer (`/sessions/.../mnt/Explainer/`) musí existovat:
1. Hotový `.md` soubor článku (s YAML frontmatter: title, date, image, source_name, source_url, excerpt)
2. PNG ilustrace (soubor uvedený v `image:` frontmatteru)

## Workflow

### 1. Identifikace souborů
- Najdi nový `.md` článek v kořenu Explainer (ne v `_articles/`, ne v `site/`)
- Ověř, že má kompletní frontmatter
- Najdi odpovídající ilustraci (PNG)

### 2. Přesun do _articles/
```bash
cp /sessions/.../mnt/Explainer/clanek.md /sessions/.../mnt/Explainer/_articles/clanek.md
```

### 3. Ověření ilustrace
Ilustrace (PNG) musí být v kořenové složce Explainer — build.py ji automaticky zkopíruje do `site/images/`.

### 4. Build test
```bash
cd /sessions/.../mnt/Explainer && python3 build.py
```
Ověř, že build proběhl bez chyb.

### 5. Git commit a push
```bash
cd /sessions/.../mnt/Explainer
git add _articles/clanek.md clanek-ilustrace.png
git commit -m "Nový článek: Titulek článku"
git push origin main
```

### 6. Informování uživatele
Po úspěšném push:
- Oznámit, že článek bude live za ~30 sekund (Netlify rebuild)
- Poskytnout URL článku: `https://novinky.inspiruj.se/articles/slug.html`
- Poskytnout admin editor URL: `https://novinky.inspiruj.se/admin/` pro případné rychlé úpravy
- Poznámka: v admin editoru je potřeba GitHub Personal Access Token (ghp_...)

## Důležité

- NIKDY nepublikuj bez explicitního pokynu uživatele
- Ověř frontmatter před publikací (title, date, image jsou povinné)
- Pokud chybí excerpt, build.py ho vygeneruje automaticky z prvního odstavce
- Admin editor na /admin/ umožňuje rychlé úpravy po publikaci
