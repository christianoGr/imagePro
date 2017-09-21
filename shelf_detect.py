import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pylab import savefig
import math ,os

def create_ker(n,k):
	return k*np.array([[-1]*n,[2]*n,[-1]*n])

def PMARAG(img,n,k,thr):
	res = cv2.bilateralFilter(img,5,200,200)
#	sharp=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
#	res=cv2.filter2D(img,-1,sharp)
	#kernel=np.array([[0,0,0,1,0,0,0],[0,0,1,1,1,0,0],[0,1,1,1,1,1,0],[1,1,1,1,1,1,1],[0,1,1,1,1,1,0],[0,0,1,1,1,0,0],[0,0,0,1,0,0,0]])
	kernel=np.array([[0,0,0],[0,1,0],[0,1,0],[1,1,1],[0,1,0],[0,1,0],[0,0,0]])
	img_d=cv2.dilate(res,kernel)
	img_e=cv2.erode(res,kernel)
	res = img_d-img_e
	#ker_rot=k*np.array([[-1,-1,-1,-1,2],[-1,-1,2,-1,-1],[2,-1,-1,-1,-1]])
	kernel=create_ker(n,k)
	res1=cv2.filter2D(res,-1,kernel)
	#res2=cv2.filter2D(res,-1,ker_rot)
	rows=res.shape[0]
	cols=res.shape[1]
	edges1=np.ones((rows,cols),dtype=np.uint8)
	for i in range(rows):
		for j in range(cols):
			if res1[i][j]<=thr:
				edges1[i][j]=0
			else:	
				edges1[i][j]=255
	#edges2=np.ones((rows,cols),dtype=np.uint8)
	#for i in range(rows):
	#	for j in range(cols):
	#		if res2[i][j]<=thr:
	#			edges2[i][j]=0
	#		else:	
	#			edges2[i][j]=255
	#edges=np.ones((rows,cols),dtype=np.uint8)
	#for i in range(rows):
	#	for j in range(cols):
			#edges[i][j]=min(255,255*int(edges1[i][j]/255.0+edges2[i][j]/255.0))
	#		edges[i][j]=max(edges1[i][j],edges2[i][j])
	#ker = np.ones((3,7),np.uint8)
	#edges1 = cv2.erode(edges1,ker,iterations = 2)
	#edges1=cv2.morphologyEx(edges1,cv2.MORPH_CLOSE,np.ones((3,3)))
	#ker = np.ones((3,3),np.uint8)
	#edges1 = cv2.erode(edges1,ker,iterations = 1)
	return edges1

#num_of_pics=5
count=0
for name in os.listdir('./PocketBizExportedImages/'):
	count=count+1
	print count
	img = cv2.imread('./PocketBizExportedImages/'+name)
	gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)	
	for n in range(5,6):
		for kk in range(5,6):
			for thr1 in range(210,231,20):
				edges = PMARAG(gray,n,kk,thr1)
				cv2.imwrite('./hh/edges'+str(count)+'_'+str(thr1)+'.jpg',edges)
				minLineLength = 50
				maxLineGap=30
				thr=100
				lines = cv2.HoughLinesP(edges,1,np.pi/180,thr,minLineLength,maxLineGap)
				#print lines.shape
				try:
					lines.shape[0]
				except AttributeError:
					continue						
				for k in range(lines.shape[0]):
						length=((lines[k][0][0] - lines[k][0][2])**2 + ( lines[k][0][1] - lines[k][0][3])**2 )**.5
						#print length
						if length<100:
							continue
						cv2.line(img,(lines[k][0][0],lines[k][0][1]),(lines[k][0][2],lines[k][0][3]),(0,255,0),10)
				print str(minLineLength)+'  '+str(maxLineGap)+'  '+str(thr)
				name_fig='./thresh100/output_105'+str(count)+'___'+str(minLineLength)+'_'+str(maxLineGap)+'_'+str(thr)+'___'+str(n)+'_'+str(kk)+'_'+str(thr1)+'1.jpg'
				#savefig(name_fig)
				cv2.imwrite(name_fig,img)
