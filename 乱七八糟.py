import numpy as np
import cv2
import xlrd
import time

if __name__ == '__main__':
    video = cv2.VideoCapture(".\\video\\ball6(15f).avi")
    cnt = 0
    while True:
        ret, img = video.read()
        if not ret:
            print(ret)
            cv2.destroyAllWindows()
            break
        cv2.imshow("1", img)
        cv2.imwrite(".\\frame\\"+str(cnt)+".png", img)
        time.sleep(0.06)
        k = cv2.waitKey(1)
        cnt+=1
        if (k == 27):
            cv2.destroyAllWindows()
            # book.save(".\\ptdata\\a.csv")
            break