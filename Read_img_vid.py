import cv2 as cv

# cat=cv.imread("Photos/cat.jpg")

# cv.imshow("Cat",cat)

# cv.waitKey(0)

capture=cv.VideoCapture("Videos/kitten.mp4")

while True:
    isTrue,frame=capture.read()

    if isTrue:
        cv.imshow("Video",frame)
        if cv.waitKey(20) & 0xFF==ord("d"):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()