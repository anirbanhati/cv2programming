import cv2 as cv
import numpy as np
people=['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Kaling Mindy', 'Madonna']
hcv=cv.CascadeClassifier('haarface.xml')
#features=np.load('features.npy')
#labels=np.load('labels.npy')
facerecognizer=cv.face.LBPHFaceRecognizer_create()
facerecognizer.read('trainedface.yml')
img=cv.imread(r'E:\cv2programming\facerecog\val\ben_afflek\vb1.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('person',gray)
faces=hcv.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
for (x,y,w,h) in faces:
    froi=gray[y:y+h,x:x+w]
    label,confidence=facerecognizer.predict(froi)
    print(f'label={people[label]}--confidence={confidence}')
    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('detec',img)
cv.waitKey(0)