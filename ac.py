import numpy as np
import argparse
import glob
import cv2
 
def auto_canny(image, sigma):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
 
	# return the edged image
	return edged


name = 'unnamed2.jpg'
img = cv2.imread(name)
img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)	
for s in np.arange(9,20,.2):
	edged =	auto_canny(img,s)
	name_out='edges_with_sigma_'+str(s)+'.jpg'
	cv2.imwrite(name_out,edged)



