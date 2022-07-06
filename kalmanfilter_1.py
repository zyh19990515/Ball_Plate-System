import numpy as np
import matplotlib.pyplot as plt
import random
import cv2
# if __name__ == '__main__':
#     z = np.linspace(0, 100, 100)
#     for i in range(0, 100):
#         noise = random.gauss(1, 10)
#         z[i] = z[i]+noise
#     x = np.array([[0], [0]])
#     p = np.array([[1, 0], [0, 1]])
#     f = np.array([[1, 1], [0, 1]])
#     q = np.array([[0.05, 0], [0, 0.05]])
#     h = np.array([1, 0])
#     r = 1
#     x1 = []
#     x2 = []
#     for i in range(0, 100):
#         x_ = f*x
#         p_ = f*p*f.T+q
#         k = p_*h.T/(h*p_*h.T+r)
#         x = x_+k*(z[i]-h*x_)
#         p = (np.eye(2)-k*h)*p_
#         x1.append(x[0][0])
#         #x2.append(x[1])
#     print(len(x1))
#     y=[]
#     for i in range(0, 100):
#         y.append(i)
#     plt.plot(y, x1)
#     plt.plot(y, z)
#     plt.show()
#
#
if __name__ == '__main__':
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt

    pos = np.array([
        [10, 50],
        [12, 49],
        [11, 52],
        [13, 52.2],
        [12.9, 50]], np.float32)

    '''
    它有3个输入参数，dynam_params：状态空间的维数，这里为2；measure_param：测量值的维数，这里也为2; control_params：控制向量的维数，默认为0。由于这里该模型中并没有控制变量，因此也为0。
    '''
    kalman = cv2.KalmanFilter(2, 2)

    kalman.measurementMatrix = np.array([[1, 0], [0, 1]], np.float32)
    kalman.transitionMatrix = np.array([[1, 0], [0, 1]], np.float32)
    kalman.processNoiseCov = np.array([[1, 0], [0, 1]], np.float32) * 1e-3
    kalman.measurementNoiseCov = np.array([[1, 0], [0, 1]], np.float32) * 0.01
    '''
    kalman.measurementNoiseCov为测量系统的协方差矩阵，方差越小，预测结果越接近测量值，kalman.processNoiseCov为模型系统的噪声，噪声越大，预测结果越不稳定，越容易接近模型系统预测值，且单步变化越大，相反，若噪声小，则预测结果与上个计算结果相差不大。
    '''

    kalman.statePre = np.array([[6], [6]], np.float32)

    for i in range(len(pos)):
        mes = np.reshape(pos[i, :], (2, 1))

        x = kalman.correct(mes)

        y = kalman.predict()
        print(kalman.statePost[0], kalman.statePost[1])
        print(kalman.statePre[0], kalman.statePre[1])
        print('measurement:\t', mes[0], mes[1])
        print('correct:\t', x[0], x[1])
        print('predict:\t', y[0], y[1])
        print('=' * 30)
