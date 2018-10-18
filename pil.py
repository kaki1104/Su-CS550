#Kaki Su
#this will display a gradient image from red to black sized 512 x 512

from PIL import Image

imgx = 512
imgy = 512

image = Image.new ('RGB', (imgx, imgy))

for y in range (imgy) :
	for x in range (imgx) :
		
		r = (x/512) * 255 #dividing the x axis by 255, thus converting x position to 255 scale so that each pixel (s) correspond to a R value. 
		image.putpixel((x, y), (int(r), 0, 0))

image.save ("demo_image.png", "PNG")
