import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pylab import savefig
import math 
'''def auto_canny(image, sigma):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper,L2gradient=True)
 
	# return the edged image
	return edged
'''
num_of_pics=5
for num in range(num_of_pics):
	name='unnamed'+str(num)+'.jpg'
	img = cv2.imread(name)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)	
	for x1 in range(50,51):
			for x2 in range(100,101):
				if x2>=x1:
					for L2gr in [True]:
						edges = cv2.Canny(gray,x1,x2,L2gradient=L2gr)
						name_out_e='edges'+str(num)+'.jpg'
						cv2.imwrite(name_out_e,edges)
						for minLineLength in range(130,131):
							for maxLineGap in range(30,31):
								for thr in range(260,261):
									print type(edges)
									print type(edges[0][0])
									lines = cv2.HoughLinesP(edges,1,np.pi/180,thr,minLineLength,maxLineGap)
									#print lines.shape
									try:
										lines.shape[0]
									except AttributeError:
										continue
									for k in range(lines.shape[0]):
											#length=((lines[k][0][0] - lines[k][0][2])**2 + ( lines[k][0][1] - lines[k][0][3])**2 )**.5
											#print length
											#if length<20:
												#continue
											cv2.line(img,(lines[k][0][0],lines[k][0][1]),(lines[k][0][2],lines[k][0][3]),(0,255,0),5)
									name_out='output'+str(num)+'.jpg'
									#cv2.imshow('image',img)
									#cv2.waitKey(0)
									#cv2.destroyAllWindows()
									print str(x1)+'  '+str(x2)+'  '+str(minLineLength)+'  '+str(maxLineGap)+'  '+str(thr)
									image = mpimg.imread(name_out)
									imgplot = plt.imshow(image)
									#plt.show()
									name_fig='./final/output_'+str(num)+'___'+str(x1)+'_'+str(x2)+'_'+str(minLineLength)+'_'+str(maxLineGap)+'_'+str(thr)+'.jpg'
									savefig(name_fig)
									cv2.imwrite(name_out,img)
