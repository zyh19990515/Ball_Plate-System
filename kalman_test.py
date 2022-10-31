import numpy as np
import matplotlib.pyplot as plt
import random
import xlrd
import time

class KF:
    def __init__(self, my_A, my_C, my_P_, my_P, my_Q, my_R, my_x_):
        self.A = my_A
        self.C = my_C
        self.P_ = my_P_
        self.P = my_P
        self.Q = my_Q
        self.R = my_R
        self.x_ = my_x_
    def estimate(self, zk):
        self.P_ = self.A * self.P * self.A + self.Q
        self.K = (self.P_ * self.C) / ((self.C * self.P_ * self.C) + self.R)
        x = self.x_ + self.K * (zk - self.C * self.x_)
        self.P = (1 - self.K * self.C) * self.P_
        self.x_ = x
        return x


if __name__ == '__main__':
    workbook = xlrd.open_workbook(".\\ptdata\\ptdata4.xls")
    sheet = workbook.sheet_by_index(0)
    data = [int(sheet.cell_value(i, 1)) for i in range(1, sheet.nrows)]
    kf1 = KF(1, 1, 1, 1, 0.2, 1, 0)
    kf2 = KF(1, 1, 1, 1, 0.5, 1, 0)
    kf3 = KF(1, 1, 1, 1, 0.9, 1, 0)
    # print(data)
    # x = np.array([[0], [0]])
    # p = np.array([[1, 0], [0, 1]])
    # f = np.array([[1, 1], [0, 1]])
    # q = np.array([[0.5, 0], [0, 0.5]])
    # h = np.array([1, 0])
    # r = 1
    '''
    x=0
    p=1
    f=1
    q=1
    h=1
    r=1
    data = data[0:50]
    x1 = []
    x2 = []
    print(len(data))
    for i in range(0, len(data)):
        x_ = f*x
        p_ = f*p*f+q
        k = p_*h/(h*p_*h+r)
        # print("data: ", data[i])
        # print("h: ", h)
        # print("x:", x_)
        # print("h*x_", h*x_)
        x = x_+k*(data[i]-h*x_)
        if(i>=40):
            x_p = x_+k*(x1[i-1]-h*x_)
            x2.append(x_p)
        else:
            x2.append(x)
        # print(data[i])
        # print("\n")
        # print(data[i]-h*x_)
        # print("\n")
        p = (1-k*h)*p_
        x1.append(x)

        #x2.append(x[1])
        #print(x1)
        '''
    data = data[0:50]
    x1 = []
    x2 = []
    x3 = []
    for i in range(0, len(data)):
        x1.append(kf1.estimate(data[i]))
        x2.append(kf2.estimate(data[i]))
        x3.append(kf3.estimate(data[i]))

    y = []
    for i in range(0, len(data)):
        y.append(i)
    plt.plot(y, x1, 'b-')
    plt.plot(y, data, 'r-')
    plt.plot(y, x2, 'g-')
    plt.plot(y, x3, 'y')
    plt.show()