import io, pygame, rpc, serial, serial.tools.list_ports, socket, sys
import cv2
from PIL import Image
import numpy as np
from PIL import ImageFile

def jpg_frame_buffer_cb(data):
    sys.stdout.flush()

    try:
        img = Image.open(io.BytesIO(data))
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        img = np.asarray(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        cv2.imshow("1", img)


        #img = pygame.image.load(io.BytesIO(data), "jpg")
        #img = pygame.surfarray.array3d(img)
        #cv2.imshow("1", img)
        screen.blit(pygame.transform.scale(pygame.image.load(io.BytesIO(data), "jpg"), (screen_w, screen_h)), (0, 0))
        pygame.display.update()
        clock.tick()
    except pygame.error: pass

    print(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

if __name__ == '__main__':
    print("\nAvailable Ports:\n")
    for port, desc, hwid in serial.tools.list_ports.comports():
        print("{} : {} [{}]".format(port, desc, hwid))
    sys.stdout.write("\nPlease enter a port name: ")
    sys.stdout.flush()
    interface = rpc.rpc_usb_vcp_master(port=input())
    print("")
    sys.stdout.flush()
    pygame.init()
    screen_w = 640
    screen_h = 480
    try:
        screen = pygame.display.set_mode((screen_w, screen_h), flags=pygame.RESIZABLE)
    except TypeError:
        screen = pygame.display.set_mode((screen_w, screen_h))
    pygame.display.set_caption("Frame Buffer")
    clock = pygame.time.Clock()
    while (True):
        sys.stdout.flush()

        # You may change the pixformat and the framesize of the image transfered from the remote device
        # by modifying the below arguments.
        result = interface.call("jpeg_image_stream", "sensor.RGB565,sensor.QVGA")
        if result is not None:
            # THE REMOTE DEVICE WILL START STREAMING ON SUCCESS. SO, WE NEED TO RECEIVE DATA IMMEDIATELY.
            interface.stream_reader(jpg_frame_buffer_cb, queue_depth=12)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()