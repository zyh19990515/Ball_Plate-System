import xlrd
import matplotlib.pyplot as plt
from kalmanClass_demo import Kalman
book = xlrd.open_workbook(".\\ptdata\\ptdata4.xls")
sheet = book.sheets()[0]
nrows = sheet.nrows
pt1_x = sheet.col_values(0)
pt1_y = sheet.col_values(1)
del pt1_x[0]
del pt1_y[0]
pt1_x_0_100 = pt1_x[0:100]
K = Kalman()
pt1 = []
for i in range(0, len(pt1_x_0_100)):
    pt1.append(K.filter(pt1_x_0_100[i]))
print(pt1[50])
print(pt1_x_0_100[50])
plt.figure()
plt.plot(pt1_x_0_100)
plt.figure()
plt.plot(pt1)
plt.show()