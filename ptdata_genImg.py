import cv2
import numpy as np
import xlrd
import time

if __name__ == '__main__':

    book = xlrd.open_workbook(".\\ptdata\\ptdata3.xls")
    sheet = book.sheets()[0]
    nrows = sheet.nrows
    pt1_x = sheet.col_values(6)
    pt1_y = sheet.col_values(7)
    del pt1_x[0]
    del pt1_y[0]
    #img = np.zeros((640, 480), dtype=np.uint8)
    for i in range(0, len(pt1_x)):
        img = np.zeros((480, 640), dtype=np.uint8)
        cv2.circle(img, np.array((int(pt1_x[i]), int(pt1_y[i]))), 3, (255, 255, 255), thickness=2)
        cv2.imshow("1", img)
        cv2.waitKey(1)
        time.sleep(0.03)



