import cv2 as cv

def rescale(frame,scale=0.25):

    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimension=(width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

# cat=cv.imread("Photos/cat_large.jpg")
# rescale_img=rescale(cat)
# cv.imshow("Cat",rescale_img)

video=cv.VideoCapture("Videos/dog.mp4")

while True:
    isTrue,frame=video.read()

    resize_frame=rescale(frame)
    cv.imshow("resize Video",resize_frame)

    if cv.waitKey(20) & 0xFF==ord("d"):
        break

video.release()
cv.destroyAllWindows()



cv.waitKey(0)