import cv2 as cv

img = cv.imread(
    'D:\Python\Py\Images\when-is-the-next-rick-and-morty-episode-out-3122098.jpg')
cv.imshow('Image', img)


def ResizeFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resized_img = ResizeFrame(img)
cv.imshow('resized', resized_img)

cv.waitKey(0)
