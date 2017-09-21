import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import probabilistic_hough_line
from skimage import draw
import cv2,os

def create_ker(n,k):
	return k*np.array([[-1]*n,[2]*n,[-1]*n])

def PMARAG(img,n,k,thr):
	kernel=create_ker(n,k)
	res=cv2.filter2D(img,-1,kernel)
	rows=res.shape[0]
	cols=res.shape[1]
	edges=np.ones((rows,cols),dtype=np.uint8)
	for i in range(rows):
		for j in range(cols):
			if res[i][j]<=thr:
				edges[i][j]=0
			else:	
				edges[i][j]=255
	return edges


def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray
count=0
for name in os.listdir('./PocketBizExportedImages/'):
	count=count+1
	print count
	distorted = plt.imread('./PocketBizExportedImages/'+name)
	dis=rgb2gray(distorted)
	dis = np.uint8(dis)
	dis=PMARAG(dis,5,3,150)
	for thresholdi in range(350,471,50):
		for line_lengthi in range(50,400,150):
			for line_gapi in range(30,31):
				print str(line_gapi)+' '+str(line_lengthi)+' '+str(thresholdi)
				lines = probabilistic_hough_line(dis,
					                         thresholdi,
					                         line_lengthi,
					                         line_gapi)
				print 'Lines: '+str(len(lines))
				if len(lines)>100:
					continue
				for k in range(len(lines)):
					length=((lines[k][0][0] - lines[k][0][1])**2 + ( lines[k][1][0] - lines[k][1][1])**2 )**.5
					if length > 350:
						continue
					cv2.line(distorted,
						(lines[k][0][0],
						lines[k][0][1]),
						(lines[k][1][0],
						lines[k][1][1]),
						(0,0,255),5)
				namee='hhh/out'+str(count)+'__'+'_'+str(thresholdi)+'_'+str(line_lengthi)+'_'+str(line_gapi)+'.jpg'
				cv2.imwrite(namee,distorted)




