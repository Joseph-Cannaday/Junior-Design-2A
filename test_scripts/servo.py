import time
import RPi.GPIO as GPIO

print("GPIO test")


# set GPIO numbering
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
servo1 = GPIO.PWM(12, 50)

# start pwm
servo1.start(0)
time.sleep(2)

# 0 degree, 2% duty cycle
duty = 2

# duty from 2 to 12 (0 to 180 degrees)
while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.5)
    servo1.ChangeDutyCycle(0)
    time.sleep(0.5)
    duty += 1

time.sleep(2)

# turn to 90 degrees
servo1.ChangeDutyCycle(7)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)
time.sleep(1.5)

# back to 0 degrees
servo1.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

print("End")#

#clean up
servo1.stop()
GPIO.cleanup()


