import cv2
import pandas as pd
import numpy as np
import time

if __name__ == '__main__':
    # data = pd.read_csv(".\\ptdata\\predict.csv", nrows=2700, usecols=[0, 1])
    # data = data.values
    # data = np.array(data, dtype=np.int)
    # print(data)

    #img = np.zeros((480, 640, 3))
    img = cv2.imread("C:\\Users\\Administrator\\Desktop\\PPT\\1.png")
    ptData = [[307, 412], [261, 377], [233, 339], [215, 330], [180, 291]]
    realPt = [[307, 412], [271, 379], [250, 361], [229, 343], [187, 304]]
    for i in ptData:
        cv2.circle(img, i, radius=5, color=(255, 100, 0), thickness=2)
    for i in realPt:
        cv2.circle(img, i, radius=2, color=(0, 255, 0), thickness=2)

    cv2.imshow("1", img)
    cv2.imwrite("C:\\Users\\Administrator\\Desktop\\PPT\\example.png", img)
    cv2.waitKey(0)


