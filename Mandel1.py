from PIL import Image

imgx = 512
imgy = 512

image = Image.new ('RGB', (imgx, imgy))

x1, x2 = 0.2625, 0.2698
y1, y2 = -0.983, -0.976

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
        r = i % 1024
        g = r % 512 + 32
        b = g % 256
        if x + y >= imgx :
            b = b +64
        if y - x >= 0 :
            r = r + 64


        image.putpixel((x, y), (r, g, b))

image.save ("mandel1.png", "PNG")