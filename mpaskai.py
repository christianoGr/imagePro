import cv2,os
import numpy as np
data_dir='./PocketBizExportedImages/'
counter=0
for name in os.listdir(data_dir):
	counter+=1
	print counter
	img=cv2.imread(data_dir+name)
	img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	#img=cv2.blur(img,(3,3))	
	#img = cv2.convertScaleAbs(img)
	#img=cv2.blur(img,(7,7))
	#canny_edge=cv2.Canny(img,0,0)
	#cv2.createTrackbar('min_value','canny_edge',0,500,nothing)
	#cv2.createTrackbar('max_value','canny_edge',0,500,nothing)
	#min_value = cv2.getTrackbarPos('min_value', 'canny_edge')
	#max_value = cv2.getTrackbarPos('max_value', 'canny_edge')
	kernel=np.array([[0,0,0,1,0,0,0],[0,0,1,1,1,0,0],[0,1,1,1,1,1,0],[1,1,1,1,1,1,1],[0,1,1,1,1,1,0],[0,0,1,1,1,0,0],[0,0,0,1,0,0,0]])
	#kernel=np.array([[0,0,0],[0,1,0],[0,1,0],[1,1,1],[0,1,0],[0,1,0],[0,0,0]])
	img_d=cv2.dilate(img,kernel)
	img_e=cv2.erode(img,kernel)
	img = img_d-img_e
	rows=img.shape[0]
	cols=img.shape[1]
	edges=np.ones((rows,cols))
	for thr in np.arange(150,161,10):
		for i in range(rows):
			for j in range(cols):
				if img[i][j]<=thr:
					edges[i][j]=0
				else:	
					edges[i][j]=255
			#opened=cv2.morphologyEx(edges,cv2.MORPH_OPEN,np.ones((3,3)))	
		for x in range(3,25,2):
			closed=cv2.morphologyEx(edges,cv2.MORPH_CLOSE,np.ones((x,x)))
			closed=cv2.erode(closed,np.ones((x,2*x)))
			#closed=cv2.morphologyEx(closed,cv2.MORPH_CLOSE,np.ones((2*x,2*x)))
			cv2.imwrite('./h/output'+str(counter)+'_'+str(thr)+'_'+str(x)+'_'+'_'+'.jpg',closed)
			'''
			#for x in range(10,111,10):
			#img=cv2.imread('./marag_method/giaelaedw_closed'+str(x)+'.jpg')
			img=cv2.imread('aaa.jpg')
			img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
			modes=[cv2.RETR_EXTERNAL,cv2.RETR_LIST,cv2.RETR_CCOMP,cv2.RETR_TREE]
			methods=[cv2.CHAIN_APPROX_NONE,cv2.CHAIN_APPROX_SIMPLE,cv2.CHAIN_APPROX_TC89_L1,cv2.CHAIN_APPROX_TC89_KCOS]
			for mode in modes:
				for method in methods:
					for e in np.arange(.01,.12,.05):
						image = cv2.imread("aaa.jpg")
						_,cnts,_ = cv2.findContours(img, mode, method)
						for c in cnts:
							peri = cv2.arcLength(c, True)
							approx = cv2.approxPolyDP(c, e * peri, True)
							cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
						name_out='aaa'+str(mode)+'_'+str(method)+'_'+str(e)+'.jpg'
						cv2.imwrite(name_out,image)
			'''
