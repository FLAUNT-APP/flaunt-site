#!/usr/bin/env python3
"""Builds the public legal pages from legal/*.md into public/legal/.

The Markdown is the single source; the HTML here is generated, never hand-edited.
No dependencies beyond the standard library, so `make legal` works on any Mac.
Supports what the documents use: #/##/### headings, paragraphs, **bold**, bullet and
numbered lists, pipe tables, and bare emails (made into mailto links).
"""
import html, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "legal"
OUT = ROOT / "public" / "legal"
SITE = "https://flaunt.ae"
COMPANY = "Flaunt Technologies L.L.C-FZ"
EMAIL = "biz@flaunt.ae"

# slug on disk → URL path, in index order
PAGES = [
    ("terms-of-service", "terms"),
    ("privacy-policy", "privacy"),
    ("community-guidelines", "community-guidelines"),
    ("takedown-and-appeals", "takedown-and-appeals"),
    ("form-check-notice", "form-check-notice"),
]

CSS = """
:root{--bg:#fff;--ink:#111;--ink2:#444;--hair:#ddd;--link:#0b57d0;--cell:#f6f6f6}
@media (prefers-color-scheme:dark){:root{--bg:#121212;--ink:#eee;--ink2:#bbb;--hair:#333;--link:#8ab4f8;--cell:#1c1c1c}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
main{max-width:38rem;margin:0 auto;padding:1.25rem 1rem 3rem}
header.site{border-bottom:1px solid var(--hair)}
header.site div{max-width:38rem;margin:0 auto;padding:.75rem 1rem;font-weight:700;letter-spacing:.04em}
header.site a{color:var(--ink);text-decoration:none}
h1{font-size:1.6rem;line-height:1.25;margin:.5rem 0 .25rem}
.meta{color:var(--ink2);margin:0 0 1.5rem;font-size:.95rem}
h2{font-size:1.2rem;margin:1.8rem 0 .5rem}
h3{font-size:1.05rem;margin:1.4rem 0 .4rem}
p,li{margin:0 0 .9rem}
ul,ol{padding-left:1.4rem}
li{margin-bottom:.4rem}
a{color:var(--link)}
.table{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:0 0 1rem;border:1px solid var(--hair);border-radius:6px}
table{border-collapse:collapse;min-width:100%;font-size:.95rem}
th,td{text-align:left;vertical-align:top;padding:.5rem .6rem;border-bottom:1px solid var(--hair);white-space:normal;min-width:9rem}
th{background:var(--cell);font-weight:600}
tr:last-child td{border-bottom:0}
footer{max-width:38rem;margin:0 auto;padding:1.5rem 1rem 3rem;border-top:1px solid var(--hair);color:var(--ink2);font-size:.9rem}
footer a{color:var(--ink2)}
nav.index a{display:block;padding:.9rem 0;border-bottom:1px solid var(--hair);text-decoration:none;color:var(--ink)}
nav.index span{display:block;color:var(--ink2);font-size:.9rem}
"""

def inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+|mailto:[^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"(?<![\w@/])([\w.+-]+@[\w-]+(?:\.[\w-]+)+)(?=[^\w.-]|\.(?!\w)|$)", r'<a href="mailto:\1">\1</a>', text)
    return text

def convert(md: str):
    lines = md.splitlines()
    title, meta = "", ""
    out, i, para = [], 0, []
    def flush():
        nonlocal para
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>"); para = []
    while i < len(lines):
        line = lines[i]
        if line.startswith("# ") and not title:
            title = line[2:].strip(); i += 1; continue
        if not meta and title and line.startswith("Effective "):
            meta = line.strip(); i += 1; continue
        if line.startswith("## "):
            flush(); out.append(f"<h2>{inline(line[3:].strip())}</h2>"); i += 1; continue
        if line.startswith("### "):
            flush(); out.append(f"<h3>{inline(line[4:].strip())}</h3>"); i += 1; continue
        if line.startswith("|"):
            flush(); rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells): rows.append(cells)
                i += 1
            head, body = rows[0], rows[1:]
            t = "<div class=\"table\"><table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
            for r in body: t += "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
            out.append(t + "</tbody></table></div>"); continue
        m = re.match(r"^(\d+)\.\s+(.*)", line)
        if re.match(r"^- ", line) or m:
            flush(); tag = "ol" if m else "ul"; items = []
            while i < len(lines) and (re.match(r"^- ", lines[i]) or re.match(r"^\d+\.\s+", lines[i])):
                items.append(re.sub(r"^(- |\d+\.\s+)", "", lines[i])); i += 1
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>"); continue
        if line.strip() == "":
            flush(); i += 1; continue
        para.append(line.strip()); i += 1
    flush()
    return title, meta, "\n".join(out)

def description(body_html: str) -> str:
    m = re.search(r"<p>(.*?)</p>", body_html, re.S)
    text = re.sub(r"<[^>]+>", "", m.group(1)) if m else ""
    return html.escape(text[:157] + ("…" if len(text) > 157 else ""), quote=True)

def page(title: str, meta: str, body: str, path: str, desc: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>{html.escape(title)} · FLAUNT</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/legal/{path}">
<style>{CSS}</style>
</head>
<body>
<header class="site"><div><a href="/legal/">FLAUNT · Legal</a></div></header>
<main>
<h1>{html.escape(title)}</h1>
{f'<p class="meta">{html.escape(meta)}</p>' if meta else ''}
{body}
</main>
<footer>{COMPANY} · <a href="mailto:{EMAIL}">{EMAIL}</a></footer>
</body>
</html>
"""

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    index = []
    for slug, path in PAGES:
        src = SRC / f"{slug}.md"
        if not src.exists(): sys.exit(f"missing {src}")
        title, meta, body = convert(src.read_text())
        if not meta.startswith("Effective "): sys.exit(f"{src.name}: no 'Effective … · Version …' line under the title")
        (OUT / f"{path}.html").write_text(page(title, meta, body, path, description(body)))
        index.append((path, title, meta))
        print(f"{src.name} → /legal/{path}  ({meta})")
    nav = "<nav class=\"index\">" + "".join(f'<a href="/legal/{p}">{html.escape(t)}<span>{html.escape(m)}</span></a>' for p, t, m in index) + "</nav>"
    (OUT / "index.html").write_text(page("Legal", "", nav, "", "FLAUNT's terms of service, privacy policy, community guidelines, takedown and appeals process, and Form Check notice."))
    robots = ROOT / "public" / "robots.txt"
    robots.write_text("User-agent: *\nAllow: /legal/\nAllow: /\nSitemap: https://flaunt.ae/legal/\n")
    print("index + robots.txt written")

if __name__ == "__main__":
    main()
