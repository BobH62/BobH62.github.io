from PIL import Image, ImageChops

def autocrop(src, out, pad=12):
    im = Image.open(src).convert('RGB')
    bg = Image.new('RGB', im.size, (255, 255, 255))
    diff = ImageChops.difference(im, bg)
    bbox = diff.convert('L').point(lambda v: 255 if v > 12 else 0).getbbox()
    if bbox:
        l, t, r, b = bbox
        l = max(0, l - pad); t = max(0, t - pad)
        r = min(im.size[0], r + pad); b = min(im.size[1], b + pad)
        im = im.crop((l, t, r, b))
    im.save(out, quality=88)
    print('wrote', out, im.size)

autocrop('public/images/adl/adl-p14.jpg', 'public/images/adl/adl-gridshell.jpg')
autocrop('public/images/adl/adl-p16.jpg', 'public/images/adl/adl-team.jpg')
