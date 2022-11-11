import io, pygame, rpc, serial, serial.tools.list_ports, socket, sys
import cv2
from PIL import Image
import numpy as np
from PIL import ImageFile
import re
import xlwt
import time


def jpg_frame_buffer_cb(data):
    sys.stdout.flush()
    #print(data)
    cnt = 0
    try:
        img = Image.open(io.BytesIO(data))
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        img = np.asarray(img)
        #print(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cnt += 1
        print(time.time())
        cv2.imshow("1", img)
        path = ".\\picture\\pic\\"+str(time.time())+".jpg"
        cv2.imwrite(path, img)
        #time.sleep(0.020)
        key = cv2.waitKey(1)
        if (key == 27):
            cv2.destroyAllWindows()
    except pygame.error: pass

    #print(clock.get_fps())



if __name__ == '__main__':
    #camera_port
    cPort = 'com12'
    #bPort
    bPort = 'com13'
    #board = serial.Serial(bPort, 115200)
    camera = rpc.rpc_usb_vcp_master(port=cPort)
    #clock = pygame.time.Clock()
    fps_cnt = 0
    pos_dic = []

    while (True):

        sys.stdout.flush()
        # You may change the pixformat and the framesize of the image transfered from the remote device
        # by modifying the below arguments.
        result = camera.call("jpeg_image_stream", "sensor.RGB565,sensor.QVGA")
        #print(result)
        '''
        char = str(bPort.readline())
        print(len(char))
        if(len(char)>63):
            continue
        # char = char[2:-5]
        nums = re.findall("\d+",char)
        pos=[]
        pos.append(str(nums[0]))
        pos.append(str(nums[1]))
        pos.append(str(nums[2]))
        pos.append(str(nums[3]))
        pos_dic.append(pos)
        
        # worksheet.write(cnt, 0, str(nums[0]))
        # worksheet.write(cnt, 1, str(nums[1]))
        # worksheet.write(cnt, 2, str(nums[2]))
        # worksheet.write(cnt, 3, str(nums[3]))
        cnt += 1
        print(nums)
        if(cnt == 1000000):
            break
        '''
        if result is not None:
            # THE REMOTE DEVICE WILL START STREAMING ON SUCCESS. SO, WE NEED TO RECEIVE DATA IMMEDIATELY.
            camera.stream_reader(jpg_frame_buffer_cb, queue_depth=20)
            fps_cnt += 1
            # key = cv2.waitKey(1)
            # if(key==27):
            #     break
