import numpy as np
import cv2

img = cv2.imread("placeholder.jpg")
kernel = np.ones((5,5),np.uint8)
img = cv2.resize(img,(400,400))
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgray = cv2.GaussianBlur(imgray,(5,5),0)
imgray = cv2.dilate(imgray,kernel,iterations=1)
edge = cv2.Canny(imgray,100,200)
ret,thresh = cv2.threshold(imgray,127,255,0)
(_,cnts,_)  = cv2.findContours(edge.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
screenCnt = None
for c in cnts:
    peri = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.02*peri, True)
    if len(approx)==4:
        screenCnt = approx
        break

#criar mascara
cv2.drawContours(img,[screenCnt],-1,(255,150,0),3)
cv2.imshow("Contorno",img)



cv2.imshow('canny',edge)
cv2.imshow("blur+erode", imgray)
cv2.imshow("thrseh", thresh)
cv2.waitKey(0)