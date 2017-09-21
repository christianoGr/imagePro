import cv2
import numpy as np
image = cv2.imread("unnamed2.jpg")
img = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)	
img = cv2.convertScaleAbs(img)

#cv2.imshow("Edges", edged)
#cv2.waitKey(0)
 
#applying closing function 
for x in range(3,18,2):
	for y in range(9,56,2):
		kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (x,x))
		opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel1)
		kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (y,y))
		closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel2)
		for x1 in range(450,501,50):
			for y1 in range(550,601,50):		
				if y1>x1:
					closed = cv2.Canny(closed, x1, y1)
					name_out='obj/'+'a'+'_'+str(x)+'_'+str(y)+'_'+str(x1)+'_'+str(y1)+'.jpg'
					cv2.imwrite(name_out,closed)
#finding_contours 
					modes=[cv2.RETR_EXTERNAL,cv2.RETR_LIST,cv2.RETR_CCOMP,cv2.RETR_TREE]
					methods=[cv2.CHAIN_APPROX_NONE,cv2.CHAIN_APPROX_SIMPLE,cv2.CHAIN_APPROX_TC89_L1,cv2.CHAIN_APPROX_TC89_KCOS ]
					for mode in modes:
						for method in methods:
							for e in np.arange(.01,.12,.05):
								image = cv2.imread("unnamed2.jpg")
								_,cnts,_ = cv2.findContours(closed.copy(), mode, method)
								for c in cnts:
									peri = cv2.arcLength(c, True)
									approx = cv2.approxPolyDP(c, e * peri, True)
									cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
								name_out='obj/'+'a'+str(mode)+'_'+str(method)+'_'+str(e)+'_'+str(x)+'_'+str(y)+'_'+str(x1)+'_'+str(y1)+'.jpg'
								cv2.imwrite(name_out,image)
								#cv2.imshow("Output", image)
								#cv2.waitKey(0)

