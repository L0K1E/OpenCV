import cv2 as cv

img = cv.imread('Images\when-is-the-next-rick-and-morty-episode-out-3122098.jpg')

resized_small = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
resized_large = cv.resize(img, (800, 800), interpolation=cv.INTER_CUBIC)

cv.imshow("Large", resized_large)
cv.imshow("Small", resized_small)

cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
