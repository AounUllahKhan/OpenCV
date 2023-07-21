import cv2 as cv
import numpy as np

img=cv.imread("Photos/park.jpg")
cv.imshow("park",img)

# Translation
def translation(img,x,y):
    tran_mat=np.float32([[1,0,-100],[0,1,100]])
    dimansion=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,tran_mat,dimansion)
# -x --> Left
# -y --> Up
# x --> Right
# y --> Down
trans_img=translation(img,100,-100)
cv.imshow("Translated Image",trans_img)

# Rotate
def rotate(img,angle,rot_point=None):
    (width,height)=img.shape[:2]

    if rot_point==None:
        rot_point=(width//2,height//2)

    rot_mat=cv.getRotationMatrix2D(rot_point,angle,1.0)
    dimension=(width,height)
    return cv.warpAffine(img,rot_mat,dimension)

rotate_img=rotate(img,45)
cv.imshow("Rotate Image",rotate_img)

# Flip

flip_img=cv.flip(img,0)
cv.imshow("Flip Image",flip_img)


cv.waitKey(0)
