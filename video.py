import time
import io
import  RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
from datetime import datetime


while True:
	now = datetime.now()
	camera = PiCamera()
	path = "/home/pi/Desktop/gearbox/New/{}.h264".format(now)
	camera.start_recording(path)
	sleep(30)
	camera.stop_recording()
	camera.close()
	print("video captured")
	break
