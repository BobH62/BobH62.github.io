from PIL import Image
import os

raw = r"c:\Users\gybob\Documents\code\BobH62.github.io\public\images\sdme\raw"
out = r"c:\Users\gybob\Documents\code\BobH62.github.io\public\images\sdme"
os.makedirs(out, exist_ok=True)

# spread size: 3320 x 1392 ; left page ~ x[60..1600], right page ~ x[1720..3260]
def crop(src, box, dst, maxw=1600, quality=86):
    im = Image.open(os.path.join(raw, src)).convert("RGB")
    c = im.crop(box)
    w, h = c.size
    if w > maxw:
        nh = int(h * maxw / w)
        c = c.resize((maxw, nh), Image.LANCZOS)
    c.save(os.path.join(out, dst), "JPEG", quality=quality, optimize=True)
    print(dst, c.size)

# 1. Cover: X HOUSE facade (page-08 left page, full)
crop("page-08.png", (60, 40, 1600, 1352), "sdme-cover.jpg", maxw=1800)

# 2. On-site construction in Dubai (page-14 full spread collage)
crop("page-14.png", (60, 40, 3260, 1352), "sdme-construction.jpg", maxw=2000)

# 3. 9-step modular assembly (page-12 left page)
crop("page-12.png", (60, 40, 1600, 1352), "sdme-assembly.jpg", maxw=1600)

# 4. Flexible configurations PARTY/GYM/OFFICE/THEATER (page-09 left page)
crop("page-09.png", (60, 40, 1600, 1352), "sdme-flex-configs.jpg", maxw=1600)

# 5. Smart-home architectural section with tech overlay (page-10 top-left)
crop("page-10.png", (60, 40, 1600, 760), "sdme-smarthome-section.jpg", maxw=1600)

# 6. Smart-home UI dashboard (page-10 bottom-left)
crop("page-10.png", (60, 760, 1600, 1352), "sdme-smarthome-ui.jpg", maxw=1600)

# 7. Robotic fabrication of furniture molds + final pieces (page-11 left page)
crop("page-11.png", (60, 40, 1600, 1352), "sdme-fabrication.jpg", maxw=1600)

# 8. Finished living room interior (page-15 left page)
crop("page-15.png", (60, 40, 1600, 1352), "sdme-interior-living.jpg", maxw=1600)

# 9. Expo 2020 Dubai exhibition scene (page-18 left page)
crop("page-18.png", (60, 40, 1600, 1352), "sdme-expo.jpg", maxw=1600)

print("all done")
