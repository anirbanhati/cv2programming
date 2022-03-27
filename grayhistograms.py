import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('pics/gnr.jpg')
blank=np.zeros(img.shape[:2],dtype='uint8')
mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),150,255,-1)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
masked=cv.bitwise_and(gray,gray,mask=mask)
gh=cv.calcHist([gray],[0],masked,[256],[0,256])
plt.figure()
plt.xlabel('Bins')
plt.ylabel('pixels')
plt.plot(gh)
plt.show()
cv.waitKey(0)