import numpy as np
import re
import cv2

def fun1():
    with open('E:\\file\\depth_data_2_mukuai.txt', encoding='utf-8') as file:
        content = file.readlines()
        # print(content)
        # print(content.rstrip())
    pt3D_X = np.zeros((1, 480 * 640))
    pt3D_Y = np.zeros((1, 480 * 640))
    pt3D_Z = np.zeros((1, 480 * 640))
    # print(pt3D_X)
    cnt = 0
    for line in content:
        pt3 = re.findall("([0-9]\d*\.?\d*)", line)
        # print(pt3)
        pt3D_X[0][cnt] = float(pt3[0])
        pt3D_Y[0][cnt] = float(pt3[1])
        pt3D_Z[0][cnt] = float(pt3[2])
        cnt += 1


    data = np.row_stack((pt3D_X, pt3D_Y))
    data = np.row_stack((data, pt3D_Z))
    data = np.row_stack((data, np.ones((1, 480 * 640), dtype=np.float32)))

    plane = np.array((0.0361176657, -1.43757679, -1.0, 985.958609))
    depth = np.matmul(plane, data)
    depth = depth.reshape(480, 640)
    mask1 = cv2.threshold(depth, 40, 255, cv2.THRESH_BINARY)[-1]
    mask2 = cv2.threshold(depth, 100, 1, cv2.THRESH_BINARY_INV)[-1]
    mask1 = np.array(mask1)
    mask2 = np.array(mask2)
    org_mask = np.multiply(mask1, mask2)
    org_mask = (org_mask).astype(np.uint8)
    mask = cv2.erode(org_mask, None, iterations=5)
    mask = cv2.dilate(mask, None, iterations=3)
    # cv2.imshow("1", mask1)
    # cv2.imshow("2", mask2)
    cv2.imshow("ori", org_mask)
    cv2.imshow("mask", mask)
    # contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    sorted(contours, key=cv2.contourArea, reverse=True)
    img_mask = np.stack((mask,) * 3, axis=-1)
    cv2.polylines(img_mask, contours, isClosed=True, color=(0, 255, 0), thickness=1)
    cv2.imshow("final", img_mask)
    print(contours)
    #cv2.waitKey(0)

def fun2():
    depthFrame = cv2.imread(".\\picture\\bg_plane1_mukuai.png", -1)
    dataX = np.zeros((1, 480 * 640), dtype=np.float32)
    dataY = np.zeros((1, 480 * 640), dtype=np.float32)
    for i in range(480):
        for j in range(640):
            dataX[:, i * 640 + j] = j
            dataY[:, i * 640 + j] = i

    dataX = (dataX - 320) / 577.0
    dataY = (dataY - 240) / 577.0
    dataZ = np.array(depthFrame)
    dataZ = dataZ.reshape(1, 480 * 640)
    dataX = dataX * dataZ
    dataY = dataY * dataZ

    data = np.row_stack((dataX, dataY))
    data = np.row_stack((data, dataZ))
    data = np.row_stack((data, np.ones((1, 480 * 640))))
    plane = np.array((0.0361176657, -1.43757679, -1.0, 985.958609))
    depth_by_plane = np.matmul(plane, data)
    depth_by_plane = depth_by_plane.reshape(480, 640)
    mask1 = cv2.threshold(depth_by_plane, 30, 255, cv2.THRESH_BINARY)[-1]
    mask2 = cv2.threshold(depth_by_plane, 70, 1, cv2.THRESH_BINARY_INV)[-1]
    mask1 = np.array(mask1)
    mask2 = np.array(mask2)

    org_mask = np.multiply(mask1, mask2)
    cv2.imshow("111", org_mask)
    org_mask = (org_mask).astype(np.uint8)
    mask = cv2.erode(org_mask, None, iterations=5)  # 5
    mask = cv2.dilate(mask, None, iterations=5)  # 3
    cv2.imshow("fi", mask)
    #cv2.waitKey(0)

if __name__ == '__main__':
    # fun1()
    fun2()
    cv2.waitKey(0)
