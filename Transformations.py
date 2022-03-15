import cv2 as cv
import numpy as np

img = cv.imread('Images\when-is-the-next-rick-and-morty-episode-out-3122098.jpg')

# -X = Left
#  X = Up
# -Y = Right
#  Y = Down

def Translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

def Rotation(img, angle, rotationPoint=None):
    (height, width) = img.shape[:2]

    if rotationPoint is None:
        rotationPoint = (width//2, height//2)

    rotationMat = cv.getRotationMatrix2D(rotationPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotationMat, dimensions)

# 1 - Horizontal
# 0 - Vertical
# -1 - both

flip = cv.flip(img, 1)


Rotated = Rotation(img, -90)
Translated = Translate(img, 100, 100)
cv.imshow("flipped", flip)
cv.imshow("Translated", Translated)
cv.imshow("Rotated", Rotated)
cv.waitKey(0)
