import cv2 as cv

video = cv.VideoCapture('Videos\Rick and Morty - Best scene ever.mp4')


def ResizeFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


while True:
    isTrue, frame = video.read()
    frame_resized = ResizeFrame(frame)
    cv.imshow('video Player', frame)
    cv.imshow('Resized video Player', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('x'):
        break

video.release()
cv.destroyAllWindows()