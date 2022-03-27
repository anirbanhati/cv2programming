import cv2 as cv
import numpy as np
img=cv.imread('pics/lotus.jpg')
cv.imshow('lotus',img)
def translate(img,x,y):
    trnsmat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[0],img.shape[1])
    return cv.warpAffine(img,trnsmat,dimensions)
ti=translate(img,100,100)
cv.imshow('tri',ti)
def rotate(img,angle,c=None):
    (height,width)=(img.shape[1],img.shape[0])
    if(c is None):
        c=(width/2,height/2)
    rotmat=cv.getRotationMatrix2D(c,angle,2.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotmat,dimensions)
ri=rotate(img,135)
cv.imshow('ri',ri)
f0=cv.flip(img,0)
f1=cv.flip(img,1)
fn1=cv.flip(img,-1)
cv.imshow('f0',f0)
cv.imshow('f1',f1)
cv.imshow('f-1',fn1)
cv.waitKey(0)