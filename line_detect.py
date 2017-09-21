import cv2,os
import numpy as np
data_dir='./PocketBizExportedImages/'
count=0
for name in os.listdir(data_dir):
	count+=1
	img=cv2.imread(data_dir+name)
	img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	kernel=np.array([[-2,-2,-2,-2,-2],[4,4,4,4,4],[-2,-2,-2,-2,-2]])
	res=cv2.filter2D(img,-1,kernel)
	rows=res.shape[0]
	cols=res.shape[1]
	edges=np.ones((rows,cols))
	thr=150
	for i in range(rows):
		for j in range(cols):
			if res[i][j]<=thr:
				edges[i][j]=0
			else:	
				edges[i][j]=255
	closed=cv2.morphologyEx(edges,cv2.MORPH_CLOSE,np.ones((3,3)))
	cv2.imwrite('./h/out'+str(count)+'.jpg',closed)



