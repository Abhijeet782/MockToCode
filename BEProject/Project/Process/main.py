import os

import cv2 as cv

from Project.Process import ShapeDetector,findContour,windowCoordinates,temp,generateHtml

def main():
    images = os.listdir("Media")
    if len(images)>0:
        for file in images:
            os.remove("Media/" + file)
    for image_file in images:
        d = {}

        image = cv.imread("Media/" + image_file)
        print(image_file)

        #cv.imshow("image", image)
        #cv.waitKey(0)


        # Creating findContour Class Object
        findContourObject = findContour.findContour()

        cont = findContourObject.contour(image)

        # Creating ShapeDetector Class Object
        sd = ShapeDetector.ShapeDetector()

        # Looping for Every Contour found
        for c in cont:
            area = cv.contourArea(c)

            # Calling detect function and return Shape
            shape = sd.detect(c)

            d[area] = shape

        # finding max area
        maxArea = max(d)

        # finding shape of the max area
        shapeOfMaxArea = d[maxArea]

        print("shape is", shapeOfMaxArea)

        # checking if rectangle or not
        if shapeOfMaxArea == 'Rectangle' or shapeOfMaxArea == 'Square':
            x1, y1, w, h = windowCoordinates.coordinates(cont, maxArea)
            print(x1, y1, w, h)

            list_of_img = [x1, y1, x1 + w, y1 + h]
            print(list_of_img)

            img = image[y1 + 7:h + y1 - 7, x1 + 7:w + x1 - 7]

            cv.imwrite("Project/Process/IntermediateOutput/mynewimage.jpg", img)
            tempObject=temp.newImageCrop()

            list_of_box=tempObject.crop()
            print(list_of_box)

            list_of_box.reverse()
            t2=generateHtml.sampleproj()
            t2.template(list_of_box, list_of_img)
            return 'Success'

        else:
            # Not Square
            print("Your content should be inside square")
            return 'Failure'

