import cv2
import serial
import re
import time

if __name__ == '__main__':
    s1 = serial.Serial('com13', 115200)
    st = ''
    while True:
        start = time.time()
        char = str(s1.readline())
        char = char[2:-5]
        print(char)
        end = time.time()
        print(end-start)

            # s2.write(bytes(char.encode()))
            # char2 = str(s2.read())+"aaa\n"
            # print(char2)
        #     try:
        #         # print(char)
        #         st = st + char
        #     except:
        #         continue
        #     if (char == '\n'):
        #         break
        # try:
        #     #ipList = re.findall(r'[0-9]+(?:\.[0-9]+){3}', st)
        #     #print(ipList[0])
        #     print(st)
        #     break
        # except:
        #     print(st)
        #     continue
