import pytesseract
import os
import cv2 as cv
from pytesseract import Output
import cv2
from PIL import Image
import pyautogui
width, height= pyautogui.size()
width=1.75*width
print (width,height)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#f = open("Project/Process/OutputHTML/output.html","r+")
HTML_TEMP = '<!DOCTYPE html>\n<html>\n<body>\n'
BODY_CLOSE = '</body>\n</html>'

f = open("Project/templates/Project/OutputHTML/output.html", "w")
mainFile = open("Project/Process/OutputHTML/output.html", "w")


class sampleproj:

    def template(self, list_cord, list_img):
        f.write(HTML_TEMP)
        mainFile.write(HTML_TEMP)
        self.check_photo()
        self.select_img(list_cord, list_img)

    def check_photo(self):
        c = 1
        crop_pic = os.listdir("Project/Process/cropImages")
        crop_pic.reverse()
        for img in crop_pic:
            im = cv.imread("Project/Process/cropImages/"+img)
            if not self.checkColor(im, 10, 10):
                cv.imwrite("Project/static/Project/images/cropPhoto/"+str(c)+".jpg", im)
                #cv.imwrite("search/images/cropPhoto/" + str(c) + ".jpg", im)
                c = c+1

    def select_img(self, list_of_box, list_img):
        crop_images = os.listdir("Project/Process/cropImages")
        crop_images.reverse()
        i = 0
        img_no = 1
        for crop_img in crop_images:
            img = cv.imread("Project/Process/cropImages/"+crop_img)
            print(crop_img)
            #cv.imshow("image", img)
            #cv.waitKey(0)

            if self.checkColor(img, 10, 10):
                result = pytesseract.image_to_string(Image.open("Project/Process/cropImages/"+crop_img))
                print(result)

                height = width/(list_img[2]/list_img[3])

                x1 = list_of_box[i][0]
                y1 = list_of_box[i][1]
                w = list_of_box[i][2]
                h = list_of_box[i][3]
                x2 = x1 + w
                y2 = y1 + h

                xx1 = list_img[2]
                yy1 = list_img[3]
                xx2 = list_img[2]
                yy2 = list_img[3]

                ratio_x1 = x1 / xx1
                ratio_y1 = y1 / yy1
                ratio_x2 = x2 / xx2
                ratio_y2 = y2 / yy2

                window_x1 = ratio_x1 * width
                window_y1 = ratio_y1 * height
                window_x2 = ratio_x2 * width
                window_y2 = ratio_y2 * height

                print("im in checkcolor")
                self.text_tag(result, window_x1, window_y1, window_x2, window_y2)
            else:
                height = width / (list_img[2] / list_img[3])

                x1 = list_of_box[i][0]
                y1 = list_of_box[i][1]
                w = list_of_box[i][2]
                h = list_of_box[i][3]
                x2 = x1 + w
                y2 = y1 + h

                xx1 = list_img[2]
                yy1 = list_img[3]
                xx2 = list_img[2]
                yy2 = list_img[3]

                ratio_x1 = x1 / xx1
                ratio_y1 = y1 / yy1
                ratio_x2 = x2 / xx2
                ratio_y2 = y2 / yy2

                window_x1 = ratio_x1 * width
                window_y1 = ratio_y1 * height
                window_x2 = ratio_x2 * width
                window_y2 = ratio_y2 * height

                print("else part")
                print("checking image no------------")
                print(img_no)
                self.img_tag(window_x1, window_y1, window_x2, window_y2, img_no)
                img_no = img_no+1
                print("checking image no------------")
                print (img_no)
            i = i+1
        f.write(BODY_CLOSE)
        mainFile.write(BODY_CLOSE)
        #print(f.read(),"I m here")
        f.close()

        mainFile.close()




    def checkColor(self, im, x, y):
        #im = Image.open('test3.jpg')
        im = cv.cvtColor(im, cv.COLOR_BGR2RGB)
        #im=im.convert('RGB')
        #RGB=im.getpixel((x,y))
        #R,G,B=RGB

        pixel = im[5, 5]
        B, G, R = pixel[2], pixel[1], pixel[0]

        print(R, G, B)
        if (128 <= R <= 255) and (0 <= G <= 128) and (0 <= B <= 128):
            return True
        else:
            return False

    def text_tag(self, result, x1, y1, x2, y2):
        c = 1
        for letters in result:
            if letters == '\n':
                c = c+1
        img_size = y2-y1
        img_size = img_size*0.8
        font_size = img_size / c
        self.box1(x1, y1, x2, y2, font_size)
        for letters in result:
            if letters != '\n':
                f.write(letters)
                mainFile.write(letters)
            else:
                f.write("<br>")
                mainFile.write("<br>")
        f.write("</a>\n")
        mainFile.write("</a>\n")

    def img_tag(self, x1, y1, x2, y2, img_no):
        self.box2(x1, y1, x2, y2, img_no)

    def box2(self, x1, y1, x2, y2, img_no):
        img_tag = '<img src="../../static/Project/images/cropPhoto/' + str(img_no)+'.jpg"' + ' style="position:absolute; TOP:'+str(y1)+'px; LEFT:'+str(x1)+'px; WIDTH:'+str(x2-x1)+'px; HEIGHT:'+str(y2-y1)+'px">\n'
        f.write(img_tag)
        img_tag = '<img src="../../static/Project/images/cropPhoto/' + str(img_no) + '.jpg"' + ' style="position:absolute; TOP:' + str(y1/1.5) + 'px; LEFT:' + str(x1/1.5) + 'px; WIDTH:' + str((x2 - x1)/1.5) + 'px; HEIGHT:' + str((y2 - y1)/1.5) + 'px">\n'
        mainFile.write(img_tag)

    def box1(self, x1, y1, x2, y2, font_size):
        align = '<a style="position:absolute; TOP:'+str(y1)+'px; LEFT:'+str(x1)+'px; WIDTH:'+str(x2-x1)+'px; HEIGHT:'+str(y2-y1)+'px;font-size:'+str(font_size)+'px">\n'
        f.write(align)
        align = '<a style="position:absolute; TOP:' + str(y1/1.5) + 'px; LEFT:' + str(x1/1.5) + 'px; WIDTH:' + str((x2 - x1)/1.5) + 'px; HEIGHT:' + str((y2 - y1)/1.5) + 'px;font-size:' + str(font_size/1.5) + 'px">\n'
        mainFile.write(align)
