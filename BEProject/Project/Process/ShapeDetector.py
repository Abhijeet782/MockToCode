import cv2 as cv
class ShapeDetector:
    def __init__(self):
        pass

    def detect(self, c):
        shape = "unidentified"
        perimeter = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.04 * perimeter, True)

        if len(approx) == 2:
            shape = "Line"

        elif len(approx) == 3:
            shape = "Triangle"

        elif len(approx) == 4:
            # find aspect ratio
            (x1, y1, w, h) = cv.boundingRect(approx)
            #print(x1, y1, x2, y2)
            ar = w / float(h)
            shape = "Square" if ar >= 0.95 and ar <= 1.05 else "Rectangle"

        elif len(approx) == 5:
            shape = "Pentagon"

        else:
            shape = "Circle"

        return shape
