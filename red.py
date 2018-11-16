
from PIL import Image
 

img = Image.open('IMG_0701.jpg')

width, height = img.size

fil = Image.new("RGB", (width, height), "white")

for x in range (width):
	for y in range (height):

		p = img.getpixel((x, y))
		r = p[0]
		g = p[1]
		b = p[2]

		if (g + 50 >= b or g - 50 <= b) and r-30 < g and r-30 < b :
			r = int(r*1.5)
			g = r
			b = r
		"""else :
			g =r
			b = r"""

		fil.putpixel ((x,y), (r,g,b))

fil.save("red.png", "PNG")