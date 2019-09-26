#Manually set trigger distance for sensor
import time

def setTrigger():
    print ("Set Distance? \n")
    trigger = input()
    proper = trigger.isdigit()
    while proper == False:
        print ("Please Enter a Number \n")
        trigger = input()
        proper = trigger.isdigit()
    return trigger
    
#Use the sensor to set trigger distance
def setTrigger2():
    print ("Adjusting Trigger Distance \n")
    i = 4
    dist = 0
    while i > 1:
        dist += distanceTest()
        i = i - 1
        time.sleep(1)
    trigger = dist / 4
    return trigger
    
def distanceTest():
    return 35
    
thresh = setTrigger2()
print (thresh)

thresh = setTrigger()
print (thresh)
