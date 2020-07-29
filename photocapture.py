import time
import io
import  RPi.GPIO as GPIO
from picamera import PiCamera
from datetime import datetime
from os import system


import socket
import sys

while True:
	for i in range(24):		
		now = datetime.now()
		camera = PiCamera()
		camera.resolution = (1024, 768)
		path = "/home/pi/Desktop/gearbox/New/image{}.jpg".format(now)
		camera.capture(path)    
		camera.close()
		print("image captured")
		time.sleep(1)
	break
system('convert -delay 10 -loop 0 /home/pi/Desktop/gearbox/New/image*.jpg /home/pi/Desktop/gearbox/timelapse.gif')
system('ffmpeg -framerate 30 -pattern_type glob -i "/home/pi/Desktop/gearbox/New/image*.jpg" -s:v 1024x768 -c:v libx264 -crf 17 -pix_fmt yuv420p /home/pi/Desktop/gearbox/timelapse.mp4')
print('done')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    image = {'photo': open('/home/pi/Desktop/gearbox/image.jpg', 'rb')}
    sock.sendall(image)

finally:
    print('closing socket')
    sock.close()
