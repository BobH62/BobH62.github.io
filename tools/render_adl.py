import fitz  # PyMuPDF

src = r'e:\ADL\adl introduction(raw).pdf'
doc = fitz.open(src)
print('pages', doc.page_count)
pages = [3, 4, 14, 15, 16, 17, 18, 19]
for p in pages:
    page = doc[p-1]
    pix = page.get_pixmap(dpi=150)
    out = f'public/images/adl/adl-p{p:02d}.jpg'
    pix.save(out)
    print('wrote', out, pix.width, 'x', pix.height)
