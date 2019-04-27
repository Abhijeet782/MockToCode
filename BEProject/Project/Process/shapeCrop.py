import cv2 as cv


class shapeCrop:
    def __init__(self):
        pass

    def cropImage(self, c, img):
        print(img)
#       shape = "unidentified"
        perimeter = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.04 * perimeter, True)

        if len(approx) == 3:
            pass

        elif len(approx) == 4:
            (x1, y1, x2, y2) = cv.boundingRect(approx)
            cropRect = img[y1:y2, x1:x2]
            cv.imwrite('cropImages/1.png', cropRect)

        elif len(approx) == 5:
            pass

        else:
            pass


