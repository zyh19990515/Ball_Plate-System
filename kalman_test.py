import numpy as np
import matplotlib.pyplot as plt
import random
import xlrd


if __name__ == '__main__':
    workbook = xlrd.open_workbook(".\\pt_data.csv")
    sheet = workbook.sheet_by_index(0)
    data = [int(sheet.cell_value(i, 1)) for i in range(1, sheet.nrows)]
    # print(data)
    x = np.array([[0], [0]])
    p = np.array([[1, 0], [0, 1]])
    f = np.array([[1, 1], [0, 1]])
    q = np.array([[0.05, 0], [0, 0.05]])
    h = np.array([1, 0])
    r = 1
    x1 = []
    x2 = []
    print(len(data))
    for i in range(0, len(data)):
        x_ = f*x
        p_ = f*p*f.T+q
        k = p_*h.T/(h*p_*h.T+r)
        x = x_+k*(data[i]-h*x_)
        p = (np.eye(2)-k*h)*p_
        x1.append(x[0][0])
        #x2.append(x[1])
        print(x1)
    y = []
    for i in range(0, 138):
        y.append(i)
    plt.plot(y, x1)
    plt.plot(y, data)
    plt.show()