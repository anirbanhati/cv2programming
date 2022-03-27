import cv2 as cv
import numpy as np
img=cv.imread('pics/gnr.jpg')
cv.imshow('gnr',img)
blank=np.zeros(img.shape[:2],dtype='uint8')
mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),150,255,-1)
cv.imshow('mask',mask)
masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('masked',masked)
rec=cv.rectangle(blank.copy(),(100,100),(400,200),255,-1)
cir=cv.circle(blank.copy(),(200,100),100,255,-1)
cxmask=cv.bitwise_or(rec,cir)
cxmasked=cv.bitwise_and(img,img,mask=cxmask)
cv.imshow('cxmasked',cxmasked)
cv.waitKey(0)
