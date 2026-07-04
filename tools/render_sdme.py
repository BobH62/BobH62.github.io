import fitz, os

src = r"c:\Users\gybob\Documents\HKUST_application\portfolio(English version).pdf"
out = r"c:\Users\gybob\Documents\code\BobH62.github.io\public\images\sdme\raw"
os.makedirs(out, exist_ok=True)

doc = fitz.open(src)
zoom = 2.2
mat = fitz.Matrix(zoom, zoom)
for i in range(7, 18):  # pages 8..18 (0-indexed 7..17)
    page = doc[i]
    pix = page.get_pixmap(matrix=mat)
    fn = os.path.join(out, f"page-{i+1:02d}.png")
    pix.save(fn)
    print(fn, pix.width, pix.height)
print("done")
