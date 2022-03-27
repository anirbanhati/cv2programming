import cv2 as cv
import os
import numpy as np
people=[]
dirs=r'E:\cv2programming\facerecog\train'
features=[]
labels=[]
hcv=cv.CascadeClassifier('haarface.xml')
for i in os.listdir(r'E:\cv2programming\facerecog\train'):
    people.append(i)
def training():
    for p in people:
        path=os.path.join(dirs,p)
        label=people.index(p)
        for i in os.listdir(path):
            img_path=os.path.join(path,i)
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            faces=hcv.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
            for (x,y,w,h) in faces:
                froi=gray[y:y+h,x:x+w]
                features.append(froi)
                labels.append(label)
training()
print(f'fearurelength={len(features)}')
print(f'labellength={len(labels)}')
featuresarray=np.array(features,dtype='object')
labelsarray=np.array(labels)
facerecognizer=cv.face.LBPHFaceRecognizer_create()
facerecognizer.train(featuresarray,labelsarray)
facerecognizer.save('trainedface.yml')
np.save('features.npy',featuresarray)
np.save('labels.npy',labelsarray)