from PIL import Image

imgx = 512
imgy = 512

image = Image.new ('RGB', (imgx, imgy))

x1, x2 = 0.26275, 0.27
y1, y2 = -0.9824, -0.9751

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
        r = (i % 4) * 64
        g = (i % 8) * 32
        b = (i % 16) * 16
        image.putpixel((x, y), (r, g, b))

image.save ("mandelbrot.png", "PNG")
