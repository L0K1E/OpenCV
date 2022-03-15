import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype=np.uint8)
# cv.imshow('blank', blank)

# Square
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('green', blank)

# Rectangle
# thickness -1 means fill
cv.rectangle(blank, (0, 0), (250, 500), (255, 255, 255), thickness=1)
# cv.imshow('draw', blank)

cv.rectangle(blank, (0, 0),
             (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=1)
# cv.imshow('rectangle', blank)

# Cricle
cv.circle(blank, (250, 250), 100, (255, 255, 255), thickness=3)
# cv.imshow('Cricle', blank)

# StraightLine
cv.line(blank, (0, 0), (500, 500), (255, 255, 255), thickness=3)
cv.imshow("Shapes", blank)

# Text
cv.putText(blank, 'hello', (255, 255),
           cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
cv.imshow("Text", blank)
cv.waitKey(0)
