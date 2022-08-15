import numpy as np
import cv2
import xlrd
import time
import re

if __name__ == '__main__':
   st='X:123Y:15'
   start = time.time()
   s = re.findall(r'[XY]:[0-9]*', st)
   end = time.time()
   print(s)
   print(s[0][2:])
   print(s[1][2:])