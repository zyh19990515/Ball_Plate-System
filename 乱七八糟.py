# Image Transfer - As The Controller Device
#
# This script is meant to talk to the "image_transfer_jpg_streaming_as_the_remote_device_for_your_computer.py" on the OpenMV Cam.
#
# This script shows off how to transfer the frame buffer to your computer as a jpeg image.

import io, pygame, serial, serial.tools.list_ports, socket, sys
import rpc
# Fix Python 2.x.
#try: input = raw_input
#xcept NameError: pass

# The RPC library above is installed on your OpenMV Cam and provides mutliple classes for
# allowing your OpenMV Cam to control over USB or WIFI.

##############################################################
# Choose the interface you wish to control an OpenMV Cam over.
##############################################################

# Uncomment the below lines to setup your OpenMV Cam for controlling over a USB VCP.
#
# * port - Serial Port Name.
#
print("\nAvailable Ports:\n")
for port, desc, hwid in serial.tools.list_ports.comports():
    print("{} : {} [{}]".format(port, desc, hwid))
sys.stdout.write("\nPlease enter a port name: ")
sys.stdout.flush()
interface = rpc.rpc_usb_vcp_master(port=input())
print("")
sys.stdout.flush()

# Uncomment the below line to setup your OpenMV Cam for controlling over WiFi.
#
# * slave_ip - IP address to connect to.
# * my_ip - IP address to bind to ("" to bind to all interfaces...)
# * port - Port to route traffic to.
#
# interface = rpc.rpc_network_master(slave_ip="xxx.xxx.xxx.xxx", my_ip="", port=0x1DBA)

##############################################################
# Call Back Handlers
##############################################################

pygame.init()
screen_w = 640
screen_h = 480
try:
    screen = pygame.display.set_mode((screen_w, screen_h), flags=pygame.RESIZABLE)
except TypeError:
    screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Frame Buffer")
clock = pygame.time.Clock()
print(clock)
# This will be called with the bytes() object generated by the slave device.
def jpg_frame_buffer_cb(data):
    sys.stdout.flush()

    try:
        screen.blit(pygame.transform.scale(pygame.image.load(io.BytesIO(data), "jpg"), (screen_w, screen_h)), (0, 0))

        pygame.display.update()
        clock.tick()
    except pygame.error: pass

    print(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

while(True):
    sys.stdout.flush()

    # You may change the pixformat and the framesize of the image transfered from the remote device
    # by modifying the below arguments.
    result = interface.call("jpeg_image_stream", "sensor.RGB565,sensor.QQVGA")
    if result is not None:

        # THE REMOTE DEVICE WILL START STREAMING ON SUCCESS. SO, WE NEED TO RECEIVE DATA IMMEDIATELY.
        interface.stream_reader(jpg_frame_buffer_cb, queue_depth=8)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()