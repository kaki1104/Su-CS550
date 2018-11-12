#blur.py

from PIL import Image
from PIL import ImageFilter

# Create an Image Object

img = Image.open("IMG_0701.jpg")

 # Apply SMOOTH filters

smoothenedImage = img.filter(ImageFilter.SMOOTH)

moreSmoothenedImage = img.filter(ImageFilter.SMOOTH_MORE)

# Display the original image and the smoothened Images

img.show()

smoothenedImage.show()

moreSmoothenedImage.show()

img.save ("blurred.png", "PNG")