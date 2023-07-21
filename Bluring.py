import cv2 as cv

img=cv.imread("Photos/group 1.jpg")
cv.imshow("Image",img)

# Average Bluring

avg_blur=cv.blur(img,(3,3))
cv.imshow("Average Blur",avg_blur)

# Gaussian Bluring

Gauss_Blur=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussain Bluring',Gauss_Blur)

# Median Bluring
median=cv.medianBlur(img,3)
cv.imshow("Median Bluring",median)

# Bilaterial 
Bilaterial=cv.bilateralFilter(img,10,30,15)
cv.imshow("Bilaterial",Bilaterial)
cv.waitKey(0)