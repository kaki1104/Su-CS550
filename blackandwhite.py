#Kak Su
#november 15, 2018
#This will add a filter to an original photo. It gives a nostalgic feel to the original photo.
#I have neither given nor received unauthorized aid.
#how to convert pictures into black and white : https://www.blog.pythonlibrary.org/2017/10/11/convert-a-photo-to-black-and-white-in-python/

from PIL import Image
 
pic = 'doggo.jpg'

img = Image.open(pic) #opens the image 
bw = img.convert('L') #converts picture to black and white first

width, height = img.size #sets width and height as the values for the size of the image

fil = Image.new("RGB", (width, height), "white") #create new image

for x in range (width):
	for y in range (height):

		hm = width/3 #this is the horizontal margin, 1/3 of the width
		vm = height/3 #this is the vertical margin, 1/3 of the length

		p = bw.getpixel((x, y))
		r = p
		g = p
		b = p

		#the initial values for the color. Will give a yellow-ish tone.
		r += 55
		g += 40
		b += 10 

		i = 100 #the max difference of intensity 

		if x < hm : #gradation for the left margin
			r -= int (((hm-x)*i)/(hm))
			g -= int (((hm-x)*i)/(hm))
			b -= int (((hm-x)*i)/(hm))

		if x > hm * 2 : #gradation for the right margin
			r -= int (((x -hm*2)*i)/(hm))
			g -= int (((x-hm*2)*i)/(hm))
			b -= int (((x-hm*2)*i)/(hm))

		if y < vm : #gradation for the top margin
			r -= int (((vm-y)*i)/(vm))
			g -= int (((vm-y)*i)/(vm))
			b -= int (((vm-y)*i)/(vm))

		if y > vm * 2 : #gradation for the bottom margin
			r -= int (((y-vm*2)*i)/(vm))
			g -= int (((y-vm*2)*i)/(vm))
			b -= int (((y-vm*2)*i)/(vm))

		fil.putpixel ((x,y), (r,g,b))

fil.save("faded.png", "PNG")
