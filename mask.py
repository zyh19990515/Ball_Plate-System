import cv2
import numpy as np
import matplotlib.pyplot as plt



if __name__ == '__main__':
    #img_hsv = cv2.imread("./ball.jpg")
    img = cv2.imread("./yuan.png")
    cv2.imshow("1", img)

    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # hsv_low = np.array([38, 39, 40])
    # hsv_high = np.array([100, 100, 100])
    # mask = cv2.inRange(img_hsv, lowerb=hsv_low, upperb=hsv_high)
    # img_done = cv2.add(img_hsv, img_hsv, mask=mask)
    # img_done = cv2.cvtColor(img_done, cv2.COLOR_RGB2GRAY)

    circle = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 1, param1=100, param2 = 36, minRadius=0, maxRadius=10000)
    print(circle)
    center = np.array([int(circle[0, 0, 0]), int(circle[0, 0, 1])])
    print(center)
    #img_done = cv2.cvtColor(img_done, cv2.COLOR_HSV2RGB)
    cv2.circle(img, center, radius=3, color=(255, 255, 255), thickness=1)
    cv2.imshow("2", img)


    cv2.waitKey(0)