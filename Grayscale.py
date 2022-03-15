import cv2 as cv

img = cv.imread('Images\when-is-the-next-rick-and-morty-episode-out-3122098.jpg')
#GrayScale Image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Scale", gray)
cv.waitKey(0)
