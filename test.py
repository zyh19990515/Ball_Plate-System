import cv2
import numpy as np
import time
from solvePerspective import perspectiveMatrix
from detect import boardDetect


if __name__ == '__main__':
    img_1 = cv2.imread(".\\1.jpg")
    img_2 = cv2.imread(".\\3.jpg")
    start = time.time()
    bd1 = boardDetect(img_1)
    bd2 = boardDetect(img_2)
    img_1, corner_pts1 = bd1.main()
    print(corner_pts1)
    img_2, corner_pts2 = bd2.main()
    M = perspectiveMatrix()
    perM = M.getperspectiveMatrix(corner_pts1, corner_pts2)
    pts = M.calculatePerspective(corner_pts2, np.linalg.pinv(perM))
    end = time.time()
    print(pts)
    print(perM)
    print(end-start)