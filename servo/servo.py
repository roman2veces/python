import RPi.GPIO as GPIO 
import time

servoPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin, GPIO.OUT)
pwm = GPIO.PWM(servoPin, 50) # Set Frequency to 50Hz
pwm.start(0) # Start position of the servo motor 

# Convert an angle to DutyCycle
# Y = (1/18 * X) + 2 (math formule)
# Where Y is a DutyCycle and X is an angle
# 1/18 and 2 are values according to this servo, each servo has his own values
# tutorial: https://www.youtube.com/watch?v=SGwhx1MYXUs
def angleToDutyCycle(angle):
    return ((1./18.) * (angle)) + 2

stillRunning = True
while stillRunning:
    angle = int(input("Enter an angle (0 - 360) ... -1 to stop it"))
    if angle != -1:
        dutyCycle = angleToDutyCycle(angle)
        pwm.ChangeDutyCycle(dutyCycle)
    else:
        stillRunning = False

pwm.stop()
GPIO.cleanup()


