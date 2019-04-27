import cv2 as cv
import imutils

def coordinates(cont, maxArea):
    for c in cont:

        area = cv.contourArea(c)
        if area == maxArea:
            perimeter = cv.arcLength(c, True)
            approx = cv.approxPolyDP(c, 0.04 * perimeter, True)
            (x1, y1, w, h) = cv.boundingRect(approx)
            return x1, y1, w, h