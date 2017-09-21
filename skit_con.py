import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from skimage import data
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square,rectangle,disk,opening
from skimage.color import label2rgb
from skimage import img_as_ubyte


import cv2
image=cv2.imread('unnamed2.jpg')
image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
# apply threshold
thresh = threshold_otsu(image)
print thresh
cs=np.arange(.5,1.5,.2)
ys=range(2,15)
for c in cs:
	for y in ys: 
		bw = opening(closing(image > c*thresh, rectangle(y,int(y/3))),rectangle(int(y/3),y))
		cv_image = img_as_ubyte(bw)
		cv2.imwrite('./fakelos/nadwpwseisai'+str(y)+str(c)+'.jpg',cv_image)

		print c
		print y
		# remove artifacts connected to image border
		cleared = clear_border(bw)

		# label image regions
		label_image = label(cleared)
		image_label_overlay = label2rgb(label_image, image=image)

		fig, ax = plt.subplots(figsize=(10, 6))
		ax.imshow(image_label_overlay)

		for region in regionprops(label_image):
				# take regions with large enough areas
				if region.area >= 100:
				    # draw rectangle around segmented coins
				    minr, minc, maxr, maxc = region.bbox
				    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
				                              fill=False, edgecolor='red', linewidth=2)
				    ax.add_patch(rect)

		ax.set_axis_off()
		plt.tight_layout()
		plt.show()
