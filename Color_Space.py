import cv2 as cv

img=cv.imread("Photos/park.jpg")
cv.imshow("Image",img)

# BGR to Gray

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)


# BGR to HSV

hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

# BGR to LAB 

lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)

cv.waitKey(0)
