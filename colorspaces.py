import cv2 as cv
img=cv.imread('pics/gnr.jpg')
cv.imshow('img',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)
fir=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('fir',fir)
cv.waitKey(0)