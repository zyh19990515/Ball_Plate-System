import cv2
import numpy as np
import xlrd
import matplotlib.pyplot as plt

def getPt():
    book = xlrd.open_workbook(".\\ptdata\\ballpt.xls")
    # book = xlrd.open_workbook(".\\ptdata\\ptdata4.xls")
    sheet = book.sheets()[0]
    nrows = sheet.nrows
    pt1_x = sheet.col_values(0)
    pt1_y = sheet.col_values(1)
    del pt1_x[0]
    del pt1_x[0]
    del pt1_y[0]
    del pt1_y[0]

    pt1_x = np.array(pt1_x, dtype=np.float32)
    pt1_y = np.array(pt1_y, dtype=np.float32)
    return pt1_x, pt1_y

def interpro(pt_x, pt_y):

    pt_czx = []
    pt_czy = []
    for i in range(0, len(pt_x) - 1):
        pt_czx.append(pt_x[i])
        pt_czy.append(pt_y[i])
        cz_x = abs(pt_x[i + 1] - pt_x[i]) / 2
        pt_czx.append(cz_x)
        cz_y = abs(pt_y[i + 1] - pt_y[i]) / 2
        pt_czy.append(cz_y)
    pt_czx = np.array(pt_czx, dtype=np.float32)
    pt_czy = np.array(pt_czy, dtype=np.float32)

    return pt_czx, pt_czy

if __name__ == '__main__':
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

    eprch=2
    for i in range(eprch):
        pt1_x, pt1_y = interpro(pt1_x, pt1_y)
    print(len(pt1_x))
