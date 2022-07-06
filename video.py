import cv2
import numpy as np
import os
from detect import Detect
import xlwt
#from detect import Detect
from kalmanfilter import KalmanFilter


def dataSave(corner_pt, cnt):

    sheet.write(cnt, 0, str(corner_pt[0][0]))
    sheet.write(cnt, 1, str(corner_pt[0][1]))
    sheet.write(cnt, 2, str(corner_pt[1][0]))
    sheet.write(cnt, 3, str(corner_pt[1][1]))
    sheet.write(cnt, 4, str(corner_pt[2][0]))
    sheet.write(cnt, 5, str(corner_pt[2][1]))
    sheet.write(cnt, 6, str(corner_pt[3][0]))
    sheet.write(cnt, 7, str(corner_pt[3][1]))



if __name__ == '__main__':
    video = cv2.VideoCapture(".\\no.2.avi")

    cnt = 1
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('points')
    sheet.write(0, 0, 'p1_x')
    sheet.write(0, 1, 'p1_y')
    sheet.write(0, 2, 'p2_x')
    sheet.write(0, 3, 'p2_y')
    sheet.write(0, 4, 'p3_x')
    sheet.write(0, 5, 'p3_y')
    sheet.write(0, 6, 'p4_x')
    sheet.write(0, 7, 'p4_y')

    while True:
        ret, img = video.read()
        if not ret:
            print(ret)
            cv2.destroyAllWindows()
            book.save(".\\ptdata\\3.csv")
            break
        bd = Detect(img)
        try:
            corner_pts = bd.board_main()

            img_show = bd.getImg(img, corner_pts)
            dataSave(corner_pt=corner_pts, cnt=cnt)
            cnt+=1
        except:
            print("no")
            continue
        cv2.KalmanFilter()
        cv2.imshow("1", img_show)
        k = cv2.waitKey(1)


        if(k == 27):
            cv2.destroyAllWindows()
            book.save(".\\ptdata\\3.csv")
            break