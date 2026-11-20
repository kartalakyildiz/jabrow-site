# Builds the static pages from the bodies below: python3 _src/build.py (from the repo root).
# Plain HTML, no JavaScript: Apple's review fetches these URLs. The _src folder is not published (GitHub Pages skips
# folders that start with an underscore).
from pathlib import Path

UPDATED = 'November 19, 2026'
# A page changed after that carries its own date.
PAGE_UPDATED = {'privacy': 'November 20, 2026'}
EMAIL = 'jabrow@bkverse.com'
APP = 'Jabrow: Muay Thai &amp; Boxing'
ROOT = Path(__file__).resolve().parent.parent
BODIES = Path(__file__).resolve().parent / 'pages'

PAGES = {
    'index': ('Jabrow', 'Jabrow is an audio-guided Muay Thai and boxing training app for iPhone.'),
    'privacy': ('Privacy Policy', f'Privacy Policy for {APP}. No account, no ads, no tracking.'),
    'terms': ('Terms of Use', f'Terms of Use for {APP}.'),
    'support': ('Support', f'Help and contact for {APP}.'),
}
NAV = [('privacy', 'Privacy'), ('terms', 'Terms'), ('support', 'Support')]


def page(name: str, title: str, description: str, body: str) -> str:
    nav = '\n'.join(
        f'    <a href="{key}.html"{" aria-current=\"page\"" if key == name else ""}>{label}</a>' for key, label in NAV
    )
    full_title = 'Jabrow' if name == 'index' else f'{title} - Jabrow'
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#ECEEEC">
<link rel="icon" href="icon.png">
<link rel="stylesheet" href="style.css">
</head>
<body{' class="home"' if name == 'index' else ''}>
<header class="site"><div class="wrap{' wide' if name == 'index' else ''}">
  <a class="brand" href="index.html"><img src="icon.png" alt="">Jabrow</a>
  <nav aria-label="Main">
{nav}
  </nav>
</div></header>
<main><div class="wrap{' wide' if name == 'index' else ''}">
{body.strip()}
</div></main>
<footer><div class="wrap{' wide' if name == 'index' else ''}">
  <a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Use</a><a href="support.html">Support</a>
  <p>&copy; 2026 Batuhan Soyarslan &middot; Developed by Kartal Akyildiz &middot; Apple, iPhone and App Store are trademarks of Apple Inc.</p>
</div></footer>
</body>
</html>
'''


for name, (title, description) in PAGES.items():
    body = (BODIES / f'{name}.html').read_text(encoding='utf-8')
    body = body.replace('{{UPDATED}}', PAGE_UPDATED.get(name, UPDATED)).replace('{{EMAIL}}', EMAIL).replace('{{APP}}', APP)
    (ROOT / f'{name}.html').write_text(page(name, title, description, body), encoding='utf-8')
    print('wrote', name + '.html')
