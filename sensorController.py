Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
    
#Manually set trigger distance for sensor
def setTrigger():
	print ("Set Distance? \n")
	trigger = input()
	proper = trigger.isdigit()
	while proper == false:
		print ("Please Enter a Number \n")
		trigger = input()
		proper = trigger.isdigit()
		print ("Height Threshold is now " + trigger)
	return trigger
    
#Use the sensor to set trigger distance
def setTrigger2():
	print ("Adjusting Trigger Distance \n")
	i = 4
	dist = 0
	while i > 1:
		dist += distance()
		i = i - 1
		time.sleep(1)
	trigger = dist / 4
	print ("Height Threshold is now " + trigger)
	return trigger
    
def distanceTest():
    return 35
    
#Main will be changed when it is known of how program must run	
if __name__ == '__main__':
    thresh = 35
    try:
        while True:
            dist = distanceTest()  
            if dist < thresh + 5:
                detect = true
                print ("Height Threshold Detected: Unlocking Gate")
                #send signal to unlock gate
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(3)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
