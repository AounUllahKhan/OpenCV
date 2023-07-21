import cv2 as cv

img=cv.imread("Photos/park.jpg")

cv.imshow("Park",img)

gry_scale=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gry_Scale",gry_scale)

blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

canny=cv.Canny(img,125,150)
cv.imshow("Canny",canny)



cv.waitKey(0)
