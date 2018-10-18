#Kaki Su
#this will display a checkerboard of red and black sized 512 x 512

from PIL import Image

w = 512
h = 512

image = Image.new ('RGB', (w, h))

r = 0
for x in range (w):
	if x % 64 == 0:
		r = 255 - r
	for y in range (h) :
		if y % 64 == 0 :
			r = 255 - r
		image.putpixel((x, y), (r,0,0))

image.save ("checkerboard.png", "PNG")