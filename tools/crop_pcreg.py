from PIL import Image
import os

raw = r"c:\Users\gybob\Documents\code\BobH62.github.io\public\images\pc-reg\raw"
out = r"c:\Users\gybob\Documents\code\BobH62.github.io\public\images\pc-reg"
os.makedirs(out, exist_ok=True)

def crop(src, box, dst, maxw=1600, quality=86):
    im = Image.open(os.path.join(raw, src)).convert("RGB")
    c = im.crop(box)
    w, h = c.size
    if w > maxw:
        nh = int(h * maxw / w)
        c = c.resize((maxw, nh), Image.LANCZOS)
    c.save(os.path.join(out, dst), "JPEG", quality=quality, optimize=True)
    print(dst, c.size)

# 1. Cover: robotic welding action shot (page-04 left page)
crop("page-04.png", (60, 40, 1600, 1352), "pcreg-cover.jpg", maxw=1700)

# 2. Pipeline / concept diagrams (page-04 right page, lower diagram area)
crop("page-04.png", (1720, 480, 3260, 1352), "pcreg-pipeline.jpg", maxw=1500)

# 3. Iterative registration sequence (page-05 left page: figures a/b/c)
crop("page-05.png", (60, 40, 1600, 1352), "pcreg-iterations.jpg", maxw=1600)

# 4. Orange component aligned into blue point cloud (page-06 left page)
crop("page-06.png", (60, 40, 1600, 1352), "pcreg-visualization.jpg", maxw=1600)

# 5. FPFH back-point discarding for thin steel plates (page-07 left top)
crop("page-07.png", (60, 40, 1600, 720), "pcreg-fpfh.jpg", maxw=1600)

# 6. 47 groups results: success/deviation/failure (page-07 left bottom)
crop("page-07.png", (60, 700, 1600, 1352), "pcreg-results.jpg", maxw=1600)

print("all done")
