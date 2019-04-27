import os

import cv2 as cv

from Project.Process import ShapeDetector,findContour,windowCoordinates,shapeCrop

class newImageCrop:
    
    def __init__(self):
        pass
    
    def crop(self):
        image = cv.imread("Project/Process/IntermediateOutput/mynewimage.jpg")
        #print(image)
        # Creating findContour Class Object
        findContourObject = findContour.findContour()

        cont = findContourObject.contour(image)

        # Creating ShapeDetector Class Object
        sd = ShapeDetector.ShapeDetector()
        count = 1

        list_of_coord=[]
        for c in cont:
            # area = cv.contourArea(c)

            # Calling detect function and return Shape
            shape = sd.detect(c)
            print(shape)
            perimeter = cv.arcLength(c, True)
            approx = cv.approxPolyDP(c, 0.04 * perimeter, True)
            if shape == 'Rectangle' or shape == 'Square':
                #cv.drawContours(image, [c], -1, (255, 0, 255), 2)
                #perimeter = cv.arcLength(c, True)
                #approx = cv.approxPolyDP(c, 0.04 * perimeter, True)

                (x1, y1, w, h) = cv.boundingRect(approx)

                #create list of box coordinates
                list_of_coord.append([x1, y1, w, h])
                print(x1, y1, w, h)
                
                #cv.line(image, (x1,y1),(y2,w), (255, 0, 0), 5)
                cropped = image[y1:h+y1, x1:w+x1]
                #print (cropped)
                
                cv.imwrite("Project/Process/cropImages/"+str(count)+".jpg", cropped)
                #cv.imshow("img", cropped)
                #cv.waitKey(0)
                count = count+1
            #line
            elif shape == "Line":
                print("Line")

            else:
                print("No rectangle")

        #printing coordinates of all the boxes in img
        print(list_of_coord)
        return list_of_coord
    
    
    
