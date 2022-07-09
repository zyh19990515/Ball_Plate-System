import numpy as np
import matplotlib.pyplot as plt
import random
import cv2
import xlrd
from kalmanfilter import KalmanFilter

if __name__ == '__main__':
    book = xlrd.open_workbook(".\\ptdata\\ptdata4.xls")
    sheet = book.sheets()[0]
    nrows = sheet.nrows
    pt1_x = sheet.col_values(0)
    pt1_y = sheet.col_values(5)
    del pt1_x[0]
    del pt1_y[0]
    pt1_x_0_100 = np.array(pt1_x[0:500], dtype=np.float)
    pt1_y_0_100 = np.array(pt1_y[0:500], dtype=np.float)
    pt1_x_100_110 = np.array(pt1_x[500:505])
    pt=[]
    K = KalmanFilter()
    pt_pre_x = []
    pt_pre_y = []
    for i in range(0, len(pt1_y_0_100)):
        pt.append((pt1_x_0_100[i], pt1_y_0_100[i]))
    for p in pt:
        predicted = K.predict(p[0], p[1])
        print()
        pt_pre_x.append(predicted[0])
        pt_pre_y.append(predicted[1])
    ptPre_x = []
    ptPre_y = []
    for i in range(5):
        predicted = K.predict(predicted[0], predicted[1])
        ptPre_x.append(predicted[0])
        ptPre_y.append(predicted[1])
    plt.figure(1)
    #plt.scatter(pt_pre_x, pt_pre_y, c='r')
    x = range(500)
    plt.plot(x, pt1_x_0_100, 'r')
    plt.plot(x, pt_pre_x, 'b')
    plt.figure(2)
    x_1 = range(500, 505)
    plt.plot(x_1, ptPre_x, 'g')
    plt.plot(x_1, pt1_x_100_110, 'y')

    plt.show()
