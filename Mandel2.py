from PIL import Image
import math

imgx = 512
imgy = 512

image = Image.new ('RGB', (imgx, imgy))

x1, x2 = 0.2513, 0.2529
y1, y2 = -1.0633, -1.0616

max = 512

for y in range(imgy):
    z1 = y * (y2 - y1) / (imgy-1) + y1
    for x in range(imgx):
        z2 = x * (x2 - x1) / (imgx-1) + x1
        z = z1 + z2*1j
        c = z
        for i in range(max):
            if abs(z) >= 2.0: 
                break 
            z = z * z + c
        r = (i * 13) % 203
        g = i
        b = i
        if x < (imgx/2) and y < (imgy/2) :
            r = int ((r + i) / 2)
            g = (i * 13) % 203
            b = i

        image.putpixel((x, y), (r, g, b))

image.save ("Mandel2.png", "PNG")