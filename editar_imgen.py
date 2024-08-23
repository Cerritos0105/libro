import cv2
import cv
import numpy as nu
img = cv2.imread("pai.jpg")
cv2.imshow("Original", img)
cv2.waitKey(0)
#imgGris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgGris =img
h,w,a=img.shape             
mean = 0
cont =0
for i in range(h):
    for j in range(w):
        for z in range (a):
           k=img[i,j,z]
           imgGris[i,j]=k
           mean+=k
           cont+=1
cv2.imshow("Gris", imgGris)
cv2.waitKey(0)
imgNegativo = img
mean/=cont
for i in range(h):
    for j in range(w):
        for z in range (a):
            if imgGris[i,j,z]<mean:
                imgNegativo[i,j,z]=0
            else:
                imgNegativo[i,j,z]=255

cv2.imshow("separacion de claro y obscuro", imgNegativo)
cv2.waitKey(0)