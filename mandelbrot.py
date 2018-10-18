#mandelbrot
from PIL import Image

imgx = 512
imgy = 512

image = Image.new ('RGB', (imgx, imgy))

max = 255

ax = -0.5
ay = 1
bx = -2
by = 0.5

for y in range(imgy):
    zy = y * (ax - ay) / imgy 
    for x in range(imgx):
        zx = x * (bx - by) / imgx 
        z = zx + zy * 1j
        c = z
        for i in range(max):
            if abs(z) > 2.0: 
            	break 
            z = z * z + c
        image.putpixel((x, y), (i*20+50, i*40+20, i*20+30))

image.save ("mandelbrot.png", "PNG")
