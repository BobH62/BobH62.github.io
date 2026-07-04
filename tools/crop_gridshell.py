from PIL import Image, ImageChops
import os

raw = r"c:\Users\gybob\Documents\code\BobH62.github.io\public\images\gridshell\raw"
out = r"c:\Users\gybob\Documents\code\BobH62.github.io\public\images\gridshell"
os.makedirs(out, exist_ok=True)

def crop(src, box, dst, maxw=1700, quality=88):
    im = Image.open(os.path.join(raw, src)).convert("RGB")
    c = im.crop(box)
    w, h = c.size
    if w > maxw:
        nh = int(h * maxw / w)
        c = c.resize((maxw, nh), Image.LANCZOS)
    c.save(os.path.join(out, dst), "JPEG", quality=quality, optimize=True)
    print(dst, c.size)

# Cover: night gridshell prototype photo (page-19 left page, text-free)
crop("page-19.png", (60, 40, 1600, 1352), "gridshell-cover.jpg", maxw=1800)

# Cable-driven 3D scan comparison (page-20 right page bottom: built model + 3D scan + design/scan/sim overlay)
crop("page-20.png", (1720, 1000, 3260, 1352), "gridshell-scan.jpg", maxw=1700)

# Cable-driven erection phases + physical model (page-20 right page upper-mid: 3c phases + 3d photos)
crop("page-20.png", (1720, 380, 3260, 1010), "gridshell-cable.jpg", maxw=1700)

# Arctic multistable hero (page-21 left page, poster with title)
crop("page-21.png", (60, 40, 1600, 1352), "gridshell-arctic.jpg", maxw=1800)

# Multistable 3x3 grid surface states (page-21 right page middle column)
crop("page-21.png", (2120, 600, 2880, 1352), "gridshell-multistable.jpg", maxw=1500)

# Woven Morning Glory full-page photo (page-22 left page)
crop("page-22.png", (60, 40, 1600, 1352), "gridshell-woven.jpg", maxw=1800)

print("done")
