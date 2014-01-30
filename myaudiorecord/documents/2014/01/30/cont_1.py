import cv2
import numpy as np

img = cv2.imread('trial.jpg',0)
ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
x,y,w,h = cv2.boundingRect(cnt)
print(type(img))
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
M = cv2.moments(cnt)
print(type(img))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('img_gray',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print M
