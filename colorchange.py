import cv2
import numpy as np

img = cv2.imread(".\\no.1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
img1 = img[:, :, 1]
cv2.imshow("1", img1)
mask = cv2.inRange(img1, lowerb=0, upperb=25)
cv2.imshow("2", mask)
img_core = cv2.getStructuringElement(cv2.MORPH_CROSS, (10, 10))
mask = cv2.erode(mask, img_core, iterations=2)
cv2.imshow("3", mask)
kernel = np.ones((4, 4), np.uint8)
mask = cv2.dilate(mask, kernel, iterations=5)
cv2.imshow("4", mask)
cv2.waitKey(0)