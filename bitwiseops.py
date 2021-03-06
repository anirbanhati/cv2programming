import cv2 as cv
import numpy as np
blank=np.zeros((500,500),dtype='uint8')
rec=cv.rectangle(blank.copy(),(100,100),(400,200),255,-1)
cir=cv.circle(blank.copy(),(200,100),100,255,-1)
cv.imshow('rectangle',rec)
cv.imshow('circle',cir)
btxnor=cv.bitwise_not(cv.bitwise_xor(rec,cir))
cv.imshow('btxnor',btxnor)
btand=cv.bitwise_and(rec,cir)
cv.imshow('btand',btand)
btor=cv.bitwise_or(rec,cir)
cv.imshow('btor',btor)
btxor=cv.bitwise_xor(rec,cir)
cv.imshow('btxor',btxor)
cv.waitKey(0)