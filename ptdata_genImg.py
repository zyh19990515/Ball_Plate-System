import cv2
import numpy as np
import xlrd
import time
from interpolation import interpro
if __name__ == '__main__':

    # book = xlrd.open_workbook(".\\ptdata\\chazhi.xls")
    # sheet = book.sheets()[0]
    # nrows = sheet.nrows
    # pt1_x = sheet.col_values(0)
    # pt1_y = sheet.col_values(1)
    # del pt1_x[0]
    # del pt1_y[0]
    # del pt1_x[0]
    # del pt1_y[0]
    book = xlrd.open_workbook(".\\ptdata\\ballpt.xls")
    # book = xlrd.open_workbook(".\\ptdata\\ptdata4.xls")
    sheet = book.sheets()[0]
    nrows = sheet.nrows
    pt1_x = sheet.col_values(0)
    pt1_y = sheet.col_values(1)
    del pt1_x[0:2]

    del pt1_y[0:2]

    pt1_x = np.array(pt1_x, dtype=np.float32)
    pt1_y = np.array(pt1_y, dtype=np.float32)

    eprch = 2
    for i in range(eprch):
        pt1_x, pt1_y = interpro(pt1_x, pt1_y)
    #img = np.zeros((640, 480), dtype=np.uint8)
    for i in range(0, len(pt1_x)):
        img = np.zeros((480, 640), dtype=np.uint8)
        cv2.circle(img, np.array((int(pt1_x[i]), int(pt1_y[i]))), 3, (255, 255, 255), thickness=2)
        cv2.imshow("1", img)
        cv2.waitKey(1)
        time.sleep(0.1)



