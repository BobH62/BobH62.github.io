import fitz  # PyMuPDF
from PIL import Image, ImageChops

src = r'e:\ADL\adl introduction(raw).pdf'
doc = fitz.open(src)

def autocrop(im, pad=10):
    bg = Image.new('RGB', im.size, (255, 255, 255))
    diff = ImageChops.difference(im.convert('RGB'), bg)
    bbox = diff.convert('L').point(lambda v: 255 if v > 12 else 0).getbbox()
    if bbox:
        l, t, r, b = bbox
        l = max(0, l - pad); t = max(0, t - pad)
        r = min(im.size[0], r + pad); b = min(im.size[1], b + pad)
        im = im.crop((l, t, r, b))
    return im

for p in range(1, 8):
    page = doc[p-1]
    pix = page.get_pixmap(dpi=150)
    raw = f'public/images/adl/_raw_p{p:02d}.jpg'
    pix.save(raw)
    im = Image.open(raw).convert('RGB')
    im = autocrop(im)
    out = f'public/images/adl/adl-page-{p:02d}.jpg'
    im.save(out, quality=88)
    print('wrote', out, im.size)

import os
for p in range(1, 8):
    f = f'public/images/adl/_raw_p{p:02d}.jpg'
    if os.path.exists(f): os.remove(f)
