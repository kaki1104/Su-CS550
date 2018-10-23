from PIL import Image

imgx = 512
imgy = 512

image = Image.new ('RGB', (imgx, imgy))

x1, x2 = -1, 0
y1, y2 = -1, 0

max = 512

for y in range(imgy):
    z1 = y * (y2 - y1) / (imgy-1) + y1
    for x in range(imgx):
        z2 = x * (x2 - x1) / (imgx-1) + x1
        z = z1 + z2*1j
        c = -0.5+0.55j
        for i in range(max):
            if abs(z) >= 2.0: 
                break 
            z = z ** 3 + c
        r = i % 256
        g = (y/imgy) * 255
        b = (x/imgy) * 255
        image.putpixel((x, y), (r, int(g), int(b)))

image.save ("cosfractal.png", "PNG")