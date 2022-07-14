import numpy as np
import cv2
import xlrd
import time

if __name__ == '__main__':
    book = xlrd.open_workbook(".\\ptdata\\ballpt_4.csv")
    sheet = book.sheets()[0]
    nrows = sheet.nrows
    pt1_x = sheet.col_values(8)


    pt1_y = sheet.col_values(9)

    del pt1_x[0]
    del pt1_y[0]
    pt1_x = np.array(pt1_x, dtype=np.int)
    pt1_y = np.array(pt1_y, dtype=np.int)
    ballpt = []
    im = np.zeros((480, 640), dtype=np.uint8)
    for i in range(0, len(pt1_x)):

        ballpt.append((pt1_x[i], pt1_y[i]))

    for i in ballpt:
        cv2.circle(im, center=i, radius=3, color=255, thickness=3)
        cv2.imshow("guiji", im)
        time.sleep(0.05)
        k = cv2.waitKey(1)
        if (k == 27):
            cv2.destroyAllWindows()
            # book.save(".\\ptdata\\a.csv")
            break