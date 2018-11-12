#ilter.py
#https://medium.com/@enzoftware/how-to-build-amazing-images-filters-with-python-median-filter-sobel-filter-%EF%B8%8F-%EF%B8%8F-22aeb8e2f540

from PIL import Image
import math

img = Image.open("IMG_0701.jpg")
width, height = img.size
fil = Image.new("RGB", (width, height), "white")

for x in range (1, width - 1):
	for y in range(1, height -1):

		Gx = 0
		Gy = 0

		# top left pixel
		p = img.getpixel((x-1, y-1))
		r = p[0]
		g = p[1]
		b = p[2]

		# intensity ranges from 0 to 765 (255 * 3)
		intensity = r + g + b

		# accumulate the value into Gx, and Gy
		Gx += -intensity
		Gy += -intensity

		# remaining left column
		p = img.getpixel((x-1, y))
		r = p[0]
		g = p[1]
		b = p[2]

		Gx += -2 * (r + g + b)

		p = img.getpixel((x-1, y+1))
		r = p[0]
		g = p[1]
		b = p[2]

		Gx += -(r + g + b)
		Gy += (r + g + b)

		# middle pixels
		p = img.getpixel((x, y-1))
		r = p[0]
		g = p[1]
		b = p[2]

		Gy += -2 * (r + g + b)

		p = img.getpixel((x, y+1))
		r = p[0]
		g = p[1]
		b = p[2]

		Gy += 2 * (r + g + b)

		# right column
		p = img.getpixel((x+1, y-1))
		r = p[0]
		g = p[1]
		b = p[2]

		Gx += (r + g + b)
		Gy += -(r + g + b)

		p = img.getpixel((x+1, y))
		r = p[0]
		g = p[1]
		b = p[2]

		Gx += 2 * (r + g + b)

		p = img.getpixel((x+1, y+1))
		r = p[0]
		g = p[1]
		b = p[2]

		Gx += (r + g + b)
		Gy += (r + g + b)

		# calculate the length of the gradient (Pythagorean theorem)
		length = math.sqrt((Gx * Gx) + (Gy * Gy))

		# normalise the length of gradient to the range 0 to 255
		length = length / 4328 * 255

		length = int(length) * 10

		# draw the length in the edge image
		#newpixel = img.putpixel((length,length,length))
		fil.putpixel((x,y), ( 255-length, 255-length, 255-length))
		if (255-length) >= 100 :
			p = img.getpixel((x, y))
			r = p[0]
			g = p[1]
			b = p[2]
			fil.putpixel ((x,y), (r,g,b))
		else :
			fil.putpixel ((x,y), (0,0,0))


fil.save ("filtered.png", "PNG")
