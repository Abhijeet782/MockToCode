
import cv2 as cv
import imutils

class findContour:

    def contour(self,image):
        # Pre-Processing Image
        imageGray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        blurred = cv.GaussianBlur(imageGray, (5, 5), 0)
        threshold = cv.threshold(blurred, 250, 255, cv.THRESH_BINARY_INV)[1]

        # Finding Contours(ImageCopy,RetrievalWay,NoOfPoints)
        cont = cv.findContours(threshold.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        # Converting to readable contour
        cont = imutils.grab_contours(cont)

        return cont
