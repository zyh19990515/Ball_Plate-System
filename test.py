import os
import re
import cv2
import numpy as np
from PIL import Image
def opecv_fun():
    path = ".\\picture\\pic\\20221111_1\\100_87.jpg"
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    thresh, img_thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
    print(thresh)
    cv2.imshow("1", img_thresh)
    kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    img_erode = cv2.erode(img_thresh, kernel=kernal, iterations=5)
    img_dilate = cv2.dilate(img_erode, kernel=kernal, iterations=5)
    cv2.imshow("erode", img_dilate)

    img_jian = np.abs(img_thresh - img_dilate)
    cv2.imshow("jian", img_jian)

    img_pil = Image.fromarray(img_dilate)
    print(type(img_pil))
    cv2.waitKey(0)


def pil_fun():
    path = ".\\picture\\pic\\20221111_1\\100_87.jpg"

def aaa():
    n = int(input("n:"))
    m = int(input("m:"))
    ans = 1.0
    for i in range(1, n-m+1):
        ans*=0.2*(n-i+1)/i
    for i in range(0, m):
        ans*=0.8
    print(format(ans, '.4f'))



if __name__ == '__main__':
    aaa()