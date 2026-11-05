#!/usr/bin/env python3
"""Generate Substack-ready versions of the blog posts.

Reads every post in _posts/, converts the Markdown body to HTML, and
writes one standalone page per post into this folder (substack/).

Usage:
    python3 substack/generate.py

Then open the generated .html file in a browser, click
"Copy article for Substack", and paste (Cmd+V) into the Substack
editor. Enter the title and description shown in the toolbar into
Substack's title/description fields.
"""

import html
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "_posts"
OUT_DIR = ROOT / "substack"

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Substack version</title>
<style>
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: #fff; color: #242424; font-family: Georgia, 'Times New Roman', serif; }}
  .toolbar {{
    position: sticky; top: 0; z-index: 10;
    display: flex; align-items: center; gap: 14px; flex-wrap: wrap;
    padding: 10px 20px; background: #f7f6f3; border-bottom: 1px solid #e3e1dc;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    font-size: 13px; color: #555;
  }}
  .toolbar button {{
    font: inherit; font-weight: 600; cursor: pointer;
    background: #242424; color: #fff; border: 0; border-radius: 6px; padding: 7px 14px;
  }}
  .toolbar button:hover {{ background: #000; }}
  .toolbar .ok {{ color: #1a7f37; font-weight: 600; }}
  .toolbar .err {{ color: #b42318; font-weight: 600; }}
  .article {{ max-width: 680px; margin: 0 auto; padding: 40px 24px 96px; font-size: 21px; line-height: 1.65; }}
  .article p {{ margin: 0 0 1.3em; }}
  .article h2 {{ font-size: 27px; line-height: 1.3; margin: 1.6em 0 0.6em; font-weight: 700; }}
  .article h3 {{ font-size: 22px; line-height: 1.3; margin: 1.4em 0 0.5em; font-weight: 700; }}
  .article a {{ color: #242424; text-decoration: underline; }}
  .article sup {{ font-size: 0.6em; }}
  .article blockquote {{ margin: 1.3em 0; padding-left: 1em; border-left: 3px solid #ddd; color: #444; }}
  .article .footnote {{ font-size: 15px; color: #555; line-height: 1.5; margin-top: 2.5em; }}
  .article .footnote hr {{ border: 0; border-top: 1px solid #ddd; margin: 0 0 1em; }}
  .article .footnote ol {{ margin: 0; padding-left: 1.2em; }}
  .article .footnote li {{ margin-bottom: 0.6em; }}
  .article .footnote a {{ text-decoration: none; color: #888; }}
</style>
</head>
<body>
<div class="toolbar">
  <button id="copyBtn" onclick="copyArticle()">Copy article for Substack</button>
  <span id="status"></span>
  <span class="hint">Title for Substack: <strong>{title}</strong> &nbsp;·&nbsp; Description: {description}</span>
</div>
<div class="article" id="article">
{body_html}
</div>
<script>
function setStatus(msg, cls) {{
  var el = document.getElementById('status');
  el.textContent = msg;
  el.className = cls;
}}
function buildCopyableArticle() {{
  var article = document.getElementById('article');
  var clone = article.cloneNode(true);
  // Substack does not support in-page anchor links, so footnote
  // markers become plain superscript numbers and the back-reference
  // arrows are removed. The notes section stays at the end of the
  // post, under a "Notes" heading.
  clone.querySelectorAll('a[href^="#fn:"]').forEach(function (a) {{
    a.replaceWith(document.createTextNode(a.textContent));
  }});
  clone.querySelectorAll('a.footnote-backref').forEach(function (a) {{
    a.remove();
  }});
  var notes = clone.querySelector('.footnote');
  if (notes) {{
    var h = document.createElement('h3');
    h.textContent = 'Notes';
    var hr = notes.querySelector('hr');
    if (hr) {{ hr.replaceWith(h); }} else {{ notes.insertBefore(h, notes.firstChild); }}
  }}
  return clone;
}}
function copyArticle() {{
  var clone = buildCopyableArticle();
  var html = clone.innerHTML;
  var text = clone.textContent;
  if (navigator.clipboard && window.ClipboardItem) {{
    navigator.clipboard.write([
      new ClipboardItem({{
        'text/html': new Blob([html], {{ type: 'text/html' }}),
        'text/plain': new Blob([text], {{ type: 'text/plain' }})
      }})
    ]).then(function () {{
      setStatus('Copied! Now paste (Cmd+V) into the Substack editor.', 'ok');
    }}).catch(function () {{
      fallbackCopy();
    }});
  }} else {{
    fallbackCopy();
  }}
}}
function fallbackCopy() {{
  var clone = buildCopyableArticle();
  var holder = document.createElement('div');
  holder.style.position = 'absolute';
  holder.style.left = '-9999px';
  holder.appendChild(clone);
  document.body.appendChild(holder);
  var range = document.createRange();
  range.selectNodeContents(clone);
  var sel = window.getSelection();
  sel.removeAllRanges();
  sel.addRange(range);
  document.execCommand('copy');
  sel.removeAllRanges();
  document.body.removeChild(holder);
  setStatus('Copied! Now paste (Cmd+V) into the Substack editor.', 'ok');
}}
</script>
</body>
</html>
"""


def parse_front_matter(text):
    """Split YAML front matter from the body. Returns (meta, body)."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    meta = {}
    if not m:
        return meta, text
    for line in m.group(1).splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            value = value.strip().strip('"').strip("'")
            if value.startswith("[") and value.endswith("]"):
                value = value[1:-1].strip()
            meta[key.strip()] = value
    return meta, text[m.end():]


def to_html(md_text):
    """Convert the post body to HTML suitable for pasting into Substack."""
    # Turn <https://...> autolinks into real Markdown links.
    md_text = re.sub(r"<(https?://[^>\s]+)>", r"[\1](\1)", md_text)
    return markdown.markdown(md_text, extensions=["extra"])


def main():
    OUT_DIR.mkdir(exist_ok=True)
    posts = sorted(POSTS_DIR.glob("*.md"))
    if not posts:
        raise SystemExit(f"No posts found in {POSTS_DIR}")

    for post in posts:
        meta, body = parse_front_matter(post.read_text(encoding="utf-8"))
        title = meta.get("title", post.stem)
        description = meta.get("description", "")
        body_html = to_html(body)

        slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", post.stem)
        out_path = OUT_DIR / f"{slug}.html"
        out_path.write_text(
            PAGE_TEMPLATE.format(
                title=html.escape(title, quote=False),
                description=html.escape(description, quote=False),
                body_html=body_html,
            ),
            encoding="utf-8",
        )
        print(f"  {out_path.relative_to(ROOT)}")

    print(f"\nDone. {len(posts)} post(s) written to substack/.")
    print("Open a file in your browser, click 'Copy article for Substack',")
    print("then paste into the Substack editor.")


if __name__ == "__main__":
    main()
