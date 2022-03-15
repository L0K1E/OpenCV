import cv2 as cv

img = cv.imread('Images\when-is-the-next-rick-and-morty-episode-out-3122098.jpg')
#Blur Image
Blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Gray Scale", Blur)
cv.waitKey(0)
