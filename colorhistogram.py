import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('pics/madara.jpg')
blank=np.zeros(img.shape[:2],dtype='uint8')
mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),150,255,-1)
masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('masked',masked)
plt.figure()
plt.xlabel('Bins')
plt.ylabel('pixels')
colors=('b','g','r')
for i,col in enumerate(colors):
    ch=cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(ch,color=col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0)