from PIL import Image

src = r'C:\Users\gybob\.cursor\projects\c-Users-gybob-Documents-code-BobH62-github-io\assets\c__Users_gybob_AppData_Roaming_Cursor_User_workspaceStorage_3d9e60ae13885b58b52632a21ae0d275_images_image-2cd64dfc-3447-4fb8-b1ea-b91b4c5d804f.png'
im = Image.open(src).convert('RGB')
W, H = im.size

g = im.getchannel('G')
# stampness: red ink -> 1, white -> 0
s = g.point(lambda v: 255 - v)
s = s.point(lambda v: int(round((v / 255.0) ** 0.8 * 255)))  # gamma boost

bbox = s.point(lambda v: 255 if v > 10 else 0).getbbox()
m = 10
x0, y0 = max(0, bbox[0] - m), max(0, bbox[1] - m)
x1, y1 = min(W, bbox[2] + m), min(H, bbox[3] + m)

# blend: body dark #161616, characters white #ffffff
DARK = (0x16, 0x16, 0x16)
WHITE = (0xff, 0xff, 0xff)
sv = list(s.getdata())
out = Image.new('RGB', (W, H))
px = out.load()
for i, svv in enumerate(sv):
    x = i % W
    y = i // W
    t = svv / 255.0
    px[x, y] = (int(DARK[0]*t + WHITE[0]*(1-t)),
                int(DARK[1]*t + WHITE[1]*(1-t)),
                int(DARK[2]*t + WHITE[2]*(1-t)))
out = out.crop((x0, y0, x1, y1))
out.save('public/images/seal.png')
print('wrote public/images/seal.png', out.size)

# preview on white for verification
prev = Image.new('RGB', (out.size[0]+40, out.size[1]+40), (255, 255, 255))
prev.paste(out, (20, 20))
prev.save('tools/seal-preview.png')
print('wrote tools/seal-preview.png')
