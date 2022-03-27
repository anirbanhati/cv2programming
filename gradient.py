import cv2 as cv
import numpy as np
img=cv.imread('faces/face1.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('lap',lap)
sbx=cv.Sobel(gray,cv.CV_64F,1,0)
sby=cv.Sobel(gray,cv.CV_64F,0,1)
sbxy=cv.bitwise_or(sbx,sby)
cv.imshow('xsobel',sbx)
cv.imshow('ysobel',sby)
cv.imshow('xysobel',sbxy)
can=cv.Canny(gray,157,175)
cv.imshow('canny',can)

cv.waitKey(0)