import numpy as np
import matplotlib.pyplot as plt
import random
import xlrd
import time

if __name__ == '__main__':
    workbook = xlrd.open_workbook(".\\ptdata\\ptdata1.xls")
    sheet = workbook.sheet_by_index(0)
    data = [int(sheet.cell_value(i, 1)) for i in range(1, sheet.nrows)]
    # print(data)
    x = np.array([[0], [0]])
    p = np.array([[1, 0], [0, 1]])
    f = np.array([[1, 1], [0, 1]])
    q = np.array([[0.5, 0], [0, 0.5]])
    h = np.array([1, 0])
    r = 1
    data = data[0:100]
    x1 = []
    x2 = []
    print(len(data))
    for i in range(0, len(data)):
        start = time.time()
        x_ = f*x
        p_ = f*p*f.T+q
        k = p_*h.T/(h*p_*h.T+r)
        # print("data: ", data[i])
        # print("h: ", h)
        # print("x:", x_)
        # print("h*x_", h*x_)
        x = x_+k*(data[i]-h*x_)
        print(data[i])
        print("\n")
        print(data[i]-h*x_)
        print("\n")
        p = (np.eye(2)-k*h)*p_
        x1.append(x[0][0])
        #x2.append(x[1])
        #print(x1)
        end = time.time()
    y = []
    for i in range(0, len(data)):
        y.append(i)
    plt.plot(y, x1)
    plt.plot(y, data)
    plt.show()