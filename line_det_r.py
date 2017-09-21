import cv2
import numpy as np

img = cv2.imread('unnamed.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

lines = cv2.HoughLines(edges,1,np.pi/180,600)
print lines.shape
#print lines[200][0][0],lines[200][0][1]
for k in range(lines.shape[0]):
    a = np.cos(lines[k][0][1])
    b = np.sin(lines[k][0][1])
    x0 = a*lines[k][0][0]
    y0 = b*lines[k][0][0]
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),8)

cv2.imwrite('houghlinesR.jpg',img)