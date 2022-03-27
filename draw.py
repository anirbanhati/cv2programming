import cv2 as cv
import numpy as np
blank=np.ones((500,500,3),dtype='uint8')
blank[0:250,250:500]=0,0,255
cv.imshow('blank',blank)
cv.rectangle(blank,(0,0),(250,250),(255,255,255),thickness=cv.FILLED)
cv.imshow('rectangle',blank)
cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),40,(0,255,0),thickness=-1)
cv.imshow('circle',blank)
cv.line(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(255,0,0),thickness=3)
cv.imshow('line',blank)
cv.line(blank,(blank.shape[0]//2,blank.shape[1]//2),(500,0),(255,0,0),thickness=3)
cv.imshow('2lines',blank)
cv.putText(blank,'HELLO',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,0),3)
cv.imshow('text',blank)
cv.waitKey(0)