import numpy
import cv2

Fra = numpy.zeros((800, 1400, 4), numpy.uint8)
i = 2

while i < 255:
    for x in range(0, 1800, 200):
        for y in range (0, 1400, 200):
            cv2.circle(Fra, (x,y), i + 2, (i, i, i))
            cv2.circle(Fra, (x,y), 254 - i, (255 - i, 255 - i, i))
            cv2.imshow('Artwork', Fra)
    i += 2
    k = cv2.waitKey(10)
    if k == 27:
       break
    if i > 254:
       i = 2

cv2.destroyAllWindows()