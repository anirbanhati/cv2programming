import cv2 as cv
img=cv.imread('faces/humans.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
hcv=cv.CascadeClassifier('haarface.xml')
faces=hcv.detectMultiScale(gray,scaleFactor=1.175,minNeighbors=3)
print(f'faces={len(faces)}')
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('dected',img)
cv.waitKey(0)