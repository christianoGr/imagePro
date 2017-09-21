from PIL import Image
from pylab import *

# read image to array
im = array(Image.open('unnamed2.jpg').convert('L'))

# create a new figure
figure()

# show contours with origin upper left corner
y=contour(im,levels=[45],colors='black', origin='image')


show()
