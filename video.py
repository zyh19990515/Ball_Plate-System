import cv2
import numpy as np
import os
from detect import Detect
from solvePerspective import perspectiveMatrix
import xlwt
from kalmanfilter import KalmanFilter
import matplotlib.pyplot as plt
from kalmanfilter import KalmanFilter
import time


def dataSave(corner_pt, ball_pt, cnt):
    sheet.write(cnt, 0, str(corner_pt[0][0]))
    sheet.write(cnt, 1, str(corner_pt[0][1]))
    sheet.write(cnt, 2, str(corner_pt[1][0]))
    sheet.write(cnt, 3, str(corner_pt[1][1]))
    sheet.write(cnt, 4, str(corner_pt[2][0]))
    sheet.write(cnt, 5, str(corner_pt[2][1]))
    sheet.write(cnt, 6, str(corner_pt[3][0]))
    sheet.write(cnt, 7, str(corner_pt[3][1]))
    sheet.write(cnt, 8, str(ball_pt[0]))
    sheet.write(cnt, 9, str(ball_pt[1]))

if __name__ == '__main__':
    video = cv2.VideoCapture(".\\video\\ball6(15f).avi")
    kf = KalmanFilter()
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
    sheet.write(0, 8, 'ball_x')
    sheet.write(0, 9, 'ball_y')


    ball=[]
    while True:
        ret, img = video.read()
        if not ret:
            print(ret)
            cv2.destroyAllWindows()
            book.save(".\\ptdata\\a.csv")
            break
        bd = Detect(img)
        #cv2.imwrite(".\\frame\\" + str(cnt) + ".jpg", img)
        try:
            corner_pts = bd.board_main()
            ball_pt = bd.ball_main()

            #print(ball_pt)
            # try:
            #     predicted = kf.predict(ball_pt[0], ball_pt[1])
            #     ball_pt[0] = predicted[0]
            #     ball_pt[1] = predicted[1]
            # except:
            #     print(1)
            #Matrix = M.getperspectiveMatrix(pt1, corner_pts)

            #print(Matrix)
            #ballP = M.calculateBallPosition(ball_pt, Matrix)
            #print("ball_pt: ", ball_pt)
            #print("ballP: ", ballP)

            img_show = bd.getImg(img, corner_pts, ballPt=ball_pt)

            ball.append(ball_pt)
            #dataSave(corner_pt=corner_pts, ball_pt=ball_pt, cnt=cnt)
            print("save done")
        except:
            print("no")
            continue

        cv2.imshow("1", img_show)
        time.sleep(0.1)
        k = cv2.waitKey(1)


        if(k == 27):
            cv2.destroyAllWindows()
            #book.save(".\\ptdata\\a.csv")
            break
    for i in ball:
        sheet.write(cnt, 8, str(i[0]))
        sheet.write(cnt, 9, str(i[1]))
        cnt += 1
    book.save(".\\ptdata\\ballpt_6.csv")

