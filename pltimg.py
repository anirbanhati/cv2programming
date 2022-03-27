import matplotlib.pyplot as plt
import cv2 as cv
img=cv.imread('pics/gnr.jpg')
img2=plt.imread('pics/gnr.jpg')
plt.imshow(img2)
plt.show()
plt.imshow(img)
plt.show()