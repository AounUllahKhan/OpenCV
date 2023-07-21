import cv2 as cv
import numpy as np

img=cv.imread("Photos/cats.jpg")
cv.imshow("Image",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

canny=cv.Canny(gray,200,250)
cv.imshow("Canny",canny)

blur=cv.GaussianBlur(img,(7,7),cv.BORDER_CONSTANT)
cv.imshow("Blur",blur)
contours,hierarchies=cv.findContours(gray,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

print(f"{len(contours)} contours Found")

blank=np.zeros(img.shape,dtype="uint8")
cv.imshow("Blank",blank)

cv.drawContours(blank,contours,-1,(0,255,0),1)
cv.imshow("Draw Contours",blank)

cv.waitKey(0)