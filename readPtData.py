import xlrd
import xlwt
import matplotlib.pyplot as plt
from kalmanClass_demo import Kalman
book = xlrd.open_workbook(".\\position_data\\position_20221102_5(2points).xls")
sheet = book.sheets()[0]
nrows = sheet.nrows
pt1_x = sheet.col_values(1)
# pt1_y = sheet.col_values(1)
del pt1_x[0]
# del pt1_y[0]
#pt1_x_0_100 = pt1_x[0:100]
#K = Kalman()
pt_x = []
#pt_y = []
#pt1_pre = []
#K = Kalman()
#book.write(0, 4, str(Kalman))
for i in range(0, len(pt1_x)):
#for i in range(0, 200):
    pt_x.append(int(pt1_x[i]))
    #pt_y.append(int(pt1_y[i]))
    #pt1_pre.append(K.filter(int(pt1_x[i])))
#print(pt1[50])
#print(pt1_x_0_100[50])
#plt.figure()
#plt.plot(pt1_x_0_100)
plt.figure()
plt.title("Y")
plt.plot(pt_x)
#plt.plot(pt_x, pt_y)
# plt.plot(pt1_pre, '-r')
plt.show()
