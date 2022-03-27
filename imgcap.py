import cv2 as cv
img=cv.imread('pics/robo.jpg')
sky=cv.imread('pics/stars.jpg')
cv.imshow('robo',img)
#cv.waitKey(0)
def rescale(frame,scale=0.15):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
img1=rescale(sky)
cv.imshow('stars',img1)
cv.waitKey(0)