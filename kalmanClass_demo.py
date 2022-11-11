import numpy as np

class Kalman():
    def __init__(self):
        self.x = np.array([[0], [0]], dtype=np.float)
        self.p = np.array([[1, 0], [0, 1]], dtype=np.float)
        self.f = np.array([[1, 1], [0, 1]], dtype=np.float)
        self.q = np.array([[0.1, 0], [0, 0.1]], dtype=np.float)
        self.h = np.array([1, 0], dtype=np.float)
        self.r = 0.8
        self.x_ = 0.
        self.p_ = 0.

    def filter(self, data):

        self.x_ = self.f * self.x
        self.p_ = self.f * self.p * self.f.T + self.q
        k = self.p_ * self.h.T / (self.h * self.p_ * self.h.T + self.r)
        self.x = self.x_ + k * (float(data) - self.h * self.x_)
        self.p = (np.eye(2) - k * self.h) * self.p_
        return self.x[0][0]
