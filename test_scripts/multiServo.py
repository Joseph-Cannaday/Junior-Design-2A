import time
import RPi.GPIO as GPIO

print("Multi Servo Test")


# set GPIO numbering
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
servo1 = GPIO.PWM(12, 50)
GPIO.setup(35, GPIO.OUT)
servo2 = GPIO.PWM(35, 50)
GPIO.setup(33, GPIO.OUT)
servo3 = GPIO.PWM(33, 50)

# start pwm
servo1.start(0)
servo2.start(0)
servo3.start(0)

# turn servo1 to 0 degrees
# servo1.ChangeDutyCycle(2)
# time.sleep(0.5)
# servo1.ChangeDutyCycle(0)

# turn servos to 0 degrees
servo1.ChangeDutyCycle(2)
servo2.ChangeDutyCycle(2)
servo3.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)
servo2.ChangeDutyCycle(0)
servo3.ChangeDutyCycle(0)


# turn servo1 to 90 degrees
servo1.ChangeDutyCycle(7)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# wait 1 second
time.sleep(1)

# turn servo2 to 90 degrees & servo1 back to 0
i = 0
for i in range(5):
    servo2.ChangeDutyCycle(10)
    servo3.ChangeDutyCycle(10)
    time.sleep(0.5)
    servo2.ChangeDutyCycle(0)
    servo3.ChangeDutyCycle(0)
    servo2.ChangeDutyCycle(4)
    servo3.ChangeDutyCycle(4)
    time.sleep(0.5)
    servo2.ChangeDutyCycle(0)
    servo3.ChangeDutyCycle(0)
    i += 1

# wait 1 second
time.sleep(1)

# turn servo2,3 to 90 degrees
servo2.ChangeDutyCycle(2)
servo3.ChangeDutyCycle(2)
time.sleep(0.5)
servo2.ChangeDutyCycle(0)
servo3.ChangeDutyCycle(0)

# turn servo1 to 90 degrees
servo1.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# # wait 2 seconds
# time.sleep(2)
#
# # turn servo2 to 180 degrees & servo1 to 90
# servo2.ChangeDutyCycle(12)
# servo1.ChangeDutyCycle(7)
# time.sleep(0.5)
# servo2.ChangeDutyCycle(0)
# servo1.ChangeDutyCycle(0)
#
# # wait 2 seconds
# time.sleep(2)
#
# # turn servo2 & servo1 back to 0
# servo2.ChangeDutyCycle(2)
# servo1.ChangeDutyCycle(2)
# time.sleep(0.5)
# servo2.ChangeDutyCycle(0)
# servo1.ChangeDutyCycle(0)

print("End2")

# clean up
servo1.stop()
servo2.stop()
servo3.stop()
GPIO.cleanup()


