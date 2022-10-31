import re
import serial
import cv2
import numpy as np
import time
if __name__ == '__main__':
    s = serial.Serial('com5', 115200)

    x = 0
    y = 0
    pos = []
    while True:
        img = np.zeros((200, 260), dtype=np.uint8)
        st = ''
        while True:

            char = str(s.read(), 'utf-8')
            try:
                st = st + char
            except:
                continue
            if(char == '\n'):
                break
                
        #print(st)
        try:
            # if(st[0]=='X'):
            #     x = int(st[2:])
            #     print("x:", x)
            # elif(st[0]=='Y'):
            #     y = int(st[2:])
            #     print("y:", y)
            st1 = re.findall(r'[XY]:[0-9]*', st)
            x = int(st1[0][2:])
            y = int(st1[1][2:])
            print(x, " ", y)
        except:
            print("no pos")
        cv2.circle(img, [y, x], radius=3, color=255, thickness=3)
        cv2.imshow("1", img)
        k = cv2.waitKey(1)
        time.sleep(0.01)
        if(k == 27):
            cv2.destroyAllWindows()
            break
