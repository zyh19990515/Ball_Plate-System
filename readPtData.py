import xlrd
import xlwt
import matplotlib.pyplot as plt
from kalmanClass_demo import Kalman
import numpy as np

if __name__ == '__main__':

    book = xlrd.open_workbook(".\\position_data\\position_20221119_1.xls")
    sheet = book.sheets()[0]
    nrows = sheet.nrows
    pt1_x = sheet.col_values(0)
    pt1_y = sheet.col_values(1)
    del pt1_x[0]
    del pt1_y[0]
    ptx = []
    distant = []
    # for i in range(0, len(pt1_x)):
    for i in range(0, 500):
        #distant.append(int(pt1_x[i]))
        # ptx.append(int(pt1_x[i]))
        dis = np.sqrt(pow((float(pt1_x[i])-164), 2) + pow((float(pt1_y[i])-142), 2))#164,142   138,94
        distant.append(dis)
    # print(max(distant))
    plt.figure()
    plt.ylabel("distant")
    plt.xlabel("time")
    # plt.plot(ptx)
    plt.plot(distant)
    #plt.plot(pt_x, pt_y)
    # plt.plot(pt1_pre, '-r')
    plt.show()
