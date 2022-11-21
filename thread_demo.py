import threading
import time

class mythread():
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("开启线程")

def func1():
    print(1)
    time.sleep(0.5)

def func2():
    print(2)
    time.sleep(1)

if __name__ == '__main__':
    mt1 = mythread()
