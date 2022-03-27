import cv2 as cv
import numpy as np
img=cv.imread('pics/lotus.jpg')
cv.imshow('gnr',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
thresh,thrsimg=cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('simplethreshold',thrsimg)
adapthrsimg=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
adapthrsimg2=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('adaptivethreshold',adapthrsimg)
cv.imshow('adaptivethreshold2',adapthrsimg2)
cv.waitKey(0)