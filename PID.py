import numpy as np
import time
import matplotlib.pyplot as plt
import random
class PID():
    def __init__(self, kp, ki, kd, set):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.error = 0
        self.laste = 0
        self.sum_e = 0
        self.set = set

    def compute(self, input):
        currinput = input
        self.error = self.set - currinput
        self.sum_e = self.sum_e + self.error
        pidout = self.kp*self.error + self.ki*self.sum_e + self.kd*(self.error - self.laste)
        self.laste = self.error

        return pidout

if __name__ == '__main__':
    '''
    中心点为(119,98)
    (x,y)为位置坐标，初始设置为(80,80),速度为(10,13),速度set为(0,0)
    需要4个PID类
    '''

    kp = 0.106
    ki = 0.06
    kd = 1.106
    target = 100
    pid = PID(kp, ki, kd, target)


    start = 0
    cnt = []

    out = 0
    Out = []
    while(abs(target-out)>0.1):
        Out.append(out)
        cnt.append(start)
        out = pid.compute(out)
        out = out+random.uniform(0.1, 5.0)
        print(out)
        start = start+1

    plt.plot(cnt, Out)
    plt.show()



