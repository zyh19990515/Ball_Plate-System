import io, pygame, rpc, serial, serial.tools.list_ports, socket, sys
import cv2
from PIL import Image
import numpy as np
from PIL import ImageFile
import re
import xlwt
import time


class BCF():

    def __init__(self):
        self.cnt = 0
        # camera serial port
        self.cPort = 'com12'
        # board serial port
        #self.bPort = 'com13'

        #self.board = serial.Serial(self.bPort, 115200)
        #camera = rpc.rpc_usb_vcp_master(port=self.cPort)


    def jpg_frame_buffer_cb(self, data):
        sys.stdout.flush()
        # print(data)
        cnt = 0
        try:
            img = Image.open(io.BytesIO(data))
            ImageFile.LOAD_TRUNCATED_IMAGES = True
            img = np.asarray(img)
            # print(img)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            print(time.time())
            cv2.imshow("1", img)
            path = ".\\picture\\pic\\" + str(time.time()) + ".jpg"
            cv2.imwrite(path, img)
            # time.sleep(0.020)
            key = cv2.waitKey(1)
            if (key == 27):
                cv2.destroyAllWindows()
        except pygame.error:
            pass

    def process(self):
        camera = rpc.rpc_usb_vcp_master(port=self.cPort,)
        while True:

            sys.stdout.flush()
            result = camera.call("jpeg_image_stream", "sensor.RGB565,sensor.QQVGA")

            if result is not None:
                # THE REMOTE DEVICE WILL START STREAMING ON SUCCESS. SO, WE NEED TO RECEIVE DATA IMMEDIATELY.
                camera.stream_reader(self.jpg_frame_buffer_cb, queue_depth=20)

                # key = cv2.waitKey(1)
                # if(key==27):
                #     break


if __name__ == '__main__':
    bcf = BCF()
    bcf.process()