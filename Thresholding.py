import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Threshold

threshold,thres=cv.threshold(gray,127,255,cv.THRESH_BINARY)
cv.imshow("Threshold",thres)


threshold_inv,thres_inv=cv.threshold(gray,127,255,cv.THRESH_BINARY_INV)
cv.imshow("Threshold Inverse",thres_inv)

# Adaptive Thresholding

adaptive_thres=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,9)
cv.imshow("Adaptive Threshold",adaptive_thres)

cv.waitKey(0)