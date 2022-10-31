import cv2
import numpy as np


def cornerdetec(img):
    img = np.array(img, dtype=np.uint8)
    #img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    corners = cv2.goodFeaturesToTrack(img, 100, qualityLevel=0.5, minDistance=50)
    corners = np.int0(corners)
    corner_arr = []
    for i in corners:
        x, y = i.ravel()
        corner_arr.append((x, y))

    return corner_arr

def fu(corn):
    corn = np.array(corn, dtype=np.int32)
    #corn2 = np.array(corn2, dtype=np.int32)
    b = corn[:, 1]
    #b2 = corn[:, 1]
    index = np.lexsort((b,))
    #index2 = np.lexsort((b2,))
    corn = corn[index]
    #corn2 = corn2[index2]
    return corn


if __name__ == '__main__':
    img_1 = cv2.imread("E://file//1.png")
    img_2 = cv2.imread("E://file//2.png")


    img = cv2.cvtColor(img_1, cv2.COLOR_RGB2GRAY)
    size = img.shape
    img2 = cv2.cvtColor(img_2, cv2.COLOR_RGB2GRAY)
    #img2 = cv2.resize(img2, dsize=(381, 394))
    ret, img = cv2.threshold(img, 90, 255, cv2.THRESH_BINARY)
    ret2, img2 = cv2.threshold(img2, 90, 255, cv2.THRESH_BINARY)
    corn = cornerdetec(img)
    corn2 = cornerdetec(img2)
    corn = fu(corn)
    corn2 = fu(corn2)
    x = corn[2][0]-corn[0][0]
    x2 = corn2[2][0]-corn2[0][0]

    scale = -x2/x

    size2 = img2.shape
    img2 = cv2.resize(img2, dsize=(int(size2[1]/scale), int(size2[0]/scale)))
    img_2 = cv2.resize(img_2, dsize=(int(size2[1]/scale), int(size2[0]/scale)))
    print(img_2)
    img_1 = np.array(img_1, dtype=np.float32)
    img_2 = np.array(img_2, dtype=np.float32)
    corn = cornerdetec(img)
    corn2 = cornerdetec(img2)
    corn = fu(corn)
    corn2 = fu(corn2)
    flag = corn2[0][1]-corn[0][1]
    print(flag)
    aaa = []
    for i in range(0,flag):
        aaa.append(i)

    img2 = np.delete(img2, aaa, axis=0)
    img_2 = np.delete(img_2, aaa, axis=0)
    size = img.shape
    size2 = img2.shape
    flag = size2[0]-size[0]
    print(size2[0]-size[0])
    aa = []
    for i in range(0, flag):
        aa.append(size2[0]-i)
    print(aa)

    img2 = np.delete(img2, aa, axis=0)
    img_2 = np.delete(img_2, aa, axis=0)
    img_finish = np.zeros([size[1], size[0]], dtype=np.int8)
    img2 = cv2.resize(img2, dsize=(size[1], size[0]))

    img_2 = cv2.resize(img_2, dsize=(size[1], size[0]))
    img_1 = np.array(img_1, dtype=np.int8)
    img_2 = np.array(img_2, dtype=np.int8)
    n = np.hstack([img_1, img_2])
    n = abs(n)
    print(n)
    cv2.imshow("3", n)
    # for i in corn:
    #     cv2.circle(img, i, radius=5, color=(255, 0, 0), thickness=1)
    #     for i in corn2:
    #         cv2.circle(img2, i, radius=5, color=(255, 0, 0), thickness=1)


    #cv2.imshow("1", img)
    #cv2.imshow("2", img2)
    cv2.waitKey(0)