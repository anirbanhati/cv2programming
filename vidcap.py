import cv2 as cv
vid=cv.VideoCapture('pics/bubble.mp4')
def rescale(frame,scale=0.15):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
while True:
    isTrue,frame=vid.read()
    cv.imshow('video',frame)
    fr=rescale(frame,scale=1.5)
    cv.imshow('rsv',fr)
    if cv.waitKey(20) and 0xFF==ord('d'):
        break
vid.release()
cv.destroyAllWindows()