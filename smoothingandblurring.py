import cv2 as cv
img=cv.imread('pics/dots2.jpg')
cv.imshow('gnr',img)
ab=cv.blur(img,(7,7))
cv.imshow('avgblut',ab)
gb=cv.GaussianBlur(img,(7,7),0)
cv.imshow('gaussblur',gb)
mb=cv.medianBlur(img,7,0)
cv.imshow('medianblur',mb)
blb=cv.bilateralFilter(img,10,15,15)
cv.imshow('bilateralblur',blb)
cv.waitKey(0)