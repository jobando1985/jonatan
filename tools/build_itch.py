"""Genera dist/galaxy-rush-itch.zip: el juego sin el SDK de CrazyGames, listo para itch.io (index.html en la raíz)."""
import zipfile, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
html = (root / 'index.html').read_text(encoding='utf-8')
tag = '<script src="https://sdk.crazygames.com/crazygames-sdk-v3.js"></script>\n'
assert tag in html
out = root / 'dist'; out.mkdir(exist_ok=True)
with zipfile.ZipFile(out / 'galaxy-rush-itch.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr('index.html', html.replace(tag, ''))
print('ok', (out / 'galaxy-rush-itch.zip').stat().st_size, 'bytes')
