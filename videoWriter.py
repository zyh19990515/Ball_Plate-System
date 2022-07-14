import cv2
import numpy as np
import serial
import re
from selenium import webdriver

def serialData():
    s = serial.Serial('com3', 115200)

    st = ''
    while True:

        while True:
            char = str(s.read(), 'utf-8')
            # print(char)
            try:
                # print(char)
                st = st + char

            except:
                continue
            if (char == '\n'):
                break
        try:
            ipList = re.findall(r'[0-9]+(?:\.[0-9]+){3}', st)
            print(ipList[0])

            break
        except:
            print(st)
            continue
    return str(ipList[0])

def camera_init(ip):
    bor = webdriver.Chrome()
    ip = "http://" + ip
    #bor.get("http://192.168.137.156")
    bor.get(ip)


    select = bor.find_element_by_id('framesize')
    all_options = select.find_elements_by_tag_name('option')
    for option in all_options:
        if (option.get_attribute("value") == '10'):
            print("finish")
            option.click()
            break
    bor.quit()

if __name__ == '__main__':
    fource = cv2.VideoWriter_fourcc(*'DIVX')
    ip = serialData()
    camera_init(ip)
    cnt = 1
    videoIp = "http://" + ip + ":81/stream"
    # video = cv2.VideoCapture("http://192.168.137.156:81/stream")
    video = cv2.VideoCapture(videoIp)
    result = cv2.VideoWriter('1.mp4', fource, 20.0, (640, 480))
    cnt=0
    while True:
        ret, frame = video.read()
        if ret is True:
            result.write(frame)
            cv2.imshow("1", frame)
            cv2.imwrite(".\\frame\\"+str(cnt)+".jpg", frame)
            if cv2.waitKey(1)==ord('q'):
                break
        else:
            break

    video.release()
    result.release()
    cv2.destroyAllWindows()
