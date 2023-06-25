import time
import io
import  RPi.GPIO as GPIO
import africastalking


GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 23
GPIO_ECHO    = 24
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  
GPIO.setup(GPIO_ECHO,GPIO.IN)    
GPIO.output(GPIO_TRIGGER, False)

username = "sandbox"    # use 'sandbox' for development in the test environment
api_key = "9ef1fb7d93d80e420a853697bc0f571d13c096a501786e453f7e79e7f347f242"      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)

time.sleep(0.5)
GPIO.output(GPIO_TRIGGER, True)
time.sleep(0.00001)
GPIO.output(GPIO_TRIGGER, False)
start = time.time()
while GPIO.input(GPIO_ECHO)==0:
	start = time.time()

while GPIO.input(GPIO_ECHO)==1:
	stop = time.time()
	elapsed = stop-start
	distance = elapsed * 0.034/2
print(distance)

while distance :
	sms = africastalking.SMS
	sender = "30487"
	response = sms.send("Hello Ngacha there is an intruder at your place.", ["+254711"], sender)
	print(response)
	break
