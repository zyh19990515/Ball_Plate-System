#https://pysource.com/2021/10/29/kalman-filter-predict-the-trajectory-of-an-object/
import cv2
import numpy as np


class KalmanFilter:
    kf = cv2.KalmanFilter(4, 2)
    kf.measurementMatrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], np.float32)
    kf.transitionMatrix = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)


    def predict(self, coordX, coordY):
        ''' This function estimates the position of the object'''
        measured = np.array([[np.float32(coordX)], [np.float32(coordY)]])
        self.kf.correct(measured)
        predicted = self.kf.predict()
        x, y = int(predicted[0]), int(predicted[1])
        return x, y

if __name__ == '__main__':
    kf = KalmanFilter()

    img = cv2.imread(".\\picture\\blue_background.jpg")
    img = cv2.resize(img, (1640, 720))

    ball_positions = [(4, 300), (61, 256), (116, 214), (170, 180), (225, 148), (279, 120), (332, 97),
                      (383, 80), (434, 66), (484, 55), (535, 49), (586, 49), (634, 50),
                      (683, 58), (731, 69), (778, 82), (824, 101), (870, 124), (917, 148),
                      (962, 169), (1006, 212), (1051, 249), (1093, 290)]

    for pt in ball_positions:  # 先用之前规定好的点预测出第一个预测点
        cv2.circle(img, pt, 5, (0, 0, 255), -1)

        predicted = kf.predict(pt[0], pt[1])
        #print(predicted)
        cv2.circle(img, predicted, 5, (255, 255, 255), 4)

    for i in range(10):  # 用预测出的第一个预测点作为新预测点的评估对象，得出第二个预测点，之后再将第二个预测点作为第三个预测点的评估对象，得到第三个预测点，反反复复得到十个预测点
        predicted = kf.predict(predicted[0], predicted[1])
        print(predicted)
        cv2.circle(img, predicted, 5, (0, 0, 0), 4)

    cv2.imshow("Img", img)
    cv2.waitKey(0)


