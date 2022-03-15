import cv2 as cv

img = cv.imread('Images\when-is-the-next-rick-and-morty-episode-out-3122098.jpg')
#Blur
Blur = cv.GaussianBlur(img, (1, 1), cv.BORDER_DEFAULT)

#Edge Detection * Canny
Edges = cv.Canny(Blur, 125, 175)

#Edge Detection * Dilated
Dilated = cv.dilate(img, (5, 5), iterations= 4)

#Edge Detection * Eroded
Eroded = cv.erode(img, (7, 7), iterations=4)


cv.imshow("Canny Detection", Edges)
cv.imshow("Dilated Detection", Dilated)
cv.imshow("Eroded Detection", Eroded)
cv.waitKey(0)
