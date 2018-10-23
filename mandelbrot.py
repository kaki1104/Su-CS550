#Kaki Su
#October 23rd, 2018
#This program will generate three png pictures of uniquely zoomed and colored fractals. The first two are mandelbrot sets, and the last one is julia set.
#References: 
#about julia set: https://www.dropbox.com/s/tie5910sltnkxq3/mandelbrot_reading.pdf?dl=0


from PIL import Image

imgx = 512
imgy = 512
max = 512

def mandel1 () : #the first Mandelbrot Set

    image = Image.new ('RGB', (imgx, imgy)) #Create a new blank image of size imgx x imgy

    x1, x2 = 0.2625, 0.2698 #the zoomed x axis
    y1, y2 = -0.983, -0.976 #the zoomed y axis
    #these coordinates combined generates a swirling figure with its center point roughly positioned at the middle of the picture
        
    for y in range(imgy):
        z1 = y * (y2 - y1) / (imgy-1) + y1
        for x in range(imgx):
            z2 = x * (x2 - x1) / (imgx-1) + x1
            z = z1 + z2*1j #z is a complex number of z1 + (z2)i
            c = z #for mandelbrot set, c = z
            for i in range(max): # the mandelbrot set function z = z*z+c will continue until its absolute value reaches 2.0 for every number up till the max iteration stated above
                if abs(z) >= 2.0: 
                    break 
                z = z * z + c
            r = i
            g = i + 32
            b = g % 256
            if x + y >= imgx : # puts on a blue filter on the bottom-right right triangle
                b = b +64
            if y - x >= 0 : # puts on a red filter on the bottom-left right triangle
                r = r + 64
            #the overlap of these two triangles at the bottom will become a purple filter

            image.putpixel((x, y), (r, g, b))

    image.save ("mandel1.png", "PNG") #saves generated image as pnadel1.png

def mandel2 () : #the second Mandelbrot Set 

    image = Image.new ('RGB', (imgx, imgy))

    x1, x2 = 0.2513, 0.2529
    y1, y2 = -1.0633, -1.0616
    #these coordinates creates an image that looks like four different sized swirls partially overlapped

    for y in range(imgy):
        z1 = y * (y2 - y1) / (imgy-1) + y1
        for x in range(imgx):
            z2 = x * (x2 - x1) / (imgx-1) + x1
            z = z1 + z2*1j
            c = z
            for i in range(max): # the mandelbrot set function z = z*z+c will continue until its absolute value reaches 2.0 for every number up till the max iteration stated above
                if abs(z) >= 2.0: 
                    break 
                z = z * z + c
            r = (i * 13) % 203 + int((x/imgx) * 128) #Because the number i * 13 is big and 203 is a prime number, the color generates an interesting pattern. There is also a slight gradation of colors along the x axis; the intensity of red increases from left to right, and the turquise background becomes lighter as it goes towars the right
            g = i
            b = g #the color of g and b is kept the same so that we can enphasize the effect of red. Also it's pretty this way.

            image.putpixel((x, y), (r, g, b))

    image.save ("mandel2.png", "PNG") #saves the generated image as mandel2.png

def julia() :

    image = Image.new ('RGB', (imgx, imgy))

    x1, x2 = -1, 0
    y1, y2 = -1, 0

    for y in range(imgy):
        z1 = y * (y2 - y1) / (imgy-1) + y1
        for x in range(imgx):
            z2 = x * (x2 - x1) / (imgx-1) + x1
            z = z1 + z2*1j
            c = -0.5+0.55j # a pre-set initial value of c
            for i in range(max):# the third degree julia set function z = z**3+c will continue until its absolute value reaches 2.0 for every number up till the max iteration stated above
                if abs(z) >= 2.0:  
                    break 
                z = z ** 3 + c #third power julia set
            r = i % 256 #the red is the defult color fr the swirling shape itself.
            g = (y/imgy) * 255 #the intensity of g increases as it goes from top to bottom
            b = (x/imgy) * 255 #the intensity of b increases as it goes from left to right
            image.putpixel((x, y), (r, int(g), int(b)))

    image.save ("julia.png", "PNG") # saves the generated image as julia.png

mandel1 ()
mandel2 ()
julia ()

