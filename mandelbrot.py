#mandelbrot
from PIL import Image

imgx = 512
imgy = 512

image = Image.new ('RGB', (imgx, imgy))

max = 255

x1 = -0.5
x2 = 1
y1 = -2
y2 = 0.5

for y in range(imgy):
    z1 = y * (y1 - y2) / imgy 
    for x in range(imgx):
        z2 = x * (x1 - x2) / imgx 
        z = z1 + z2*1j
        c = z
        for i in range(max):
            if abs(z) > 2.0: 
            	break 
            z = z * z + c
        image.putpixel((x, y), (i*20+50, i*40+20, i*20+30))

image.save ("mandelbrot.png", "PNG")
