import cv2 as cv
import numpy as np

img = cv.imread(
    'Images\when-is-the-next-rick-and-morty-episode-out-3122098.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blank = np.zeros(img.shape, dtype='uint8')

#Blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
#canny = cv.Canny(Blur, 125, 175)

Ret, Thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", Thresh)

contours, hierarchies = cv.findContours(
    Thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(len(contours))

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("blank", blank)

cv.imshow("Gray Scale", gray)
#cv.imshow(" Canny", canny)
cv.waitKey(0)
