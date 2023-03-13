#!/usr/bin/env python3
# Sharon Chu, Joseph Cannaday
# Junior Design 2023
import RPi.GPIO as GPIO
import pigpio
import time
import subprocess


class Motor:
    def __init__(self, name="snapdragon_wings"):
        self.name = name
        return

    def testMotors(self):
        print("Testing motors")
        error = 0

        subprocess.call('sudo pigpiod', shell = True)
        servo1 = pigpio.pi()
        servo1.set_mode(18, pigpio.OUTPUT)
        servo1.set_PWM_frequency(18, 50)

        servo2 = pigpio.pi()
        servo2.set_mode(13, pigpio.OUTPUT)
        servo2.set_PWM_frequency(13, 50)

        servo3 = pigpio.pi()
        servo3.set_mode(19, pigpio.OUTPUT)
        servo3.set_PWM_frequency(19, 50)
        
        print("Test 0 deg")
        servo1.set_servo_pulsewidth(18, 500)
        servo2.set_servo_pulsewidth(13, 500)
        servo3.set_servo_pulsewidth(19, 500)
        time.sleep(1)
        if (servo1.get_servo_pulsewidth(18) == 500 and servo2.get_servo_pulsewidth(13) == 500 and servo3.get_servo_pulsewidth(19) == 500):
            error = 0
        else:
            error = 1

        print("Test 90 deg")
        servo1.set_servo_pulsewidth(18, 1500)
        servo2.set_servo_pulsewidth(13, 1500)
        servo3.set_servo_pulsewidth(19, 1500)
        time.sleep(1)
        if (servo1.get_servo_pulsewidth(18) == 1500 and servo2.get_servo_pulsewidth(13) == 1500 and servo3.get_servo_pulsewidth(19) == 1500):
            error = 0
        else:
            error = 1

        print("Test 45 deg")
        servo2.set_servo_pulsewidth(13, 1050)
        servo3.set_servo_pulsewidth(19, 1050)
        time.sleep(1)
        if (servo2.get_servo_pulsewidth(13) == 1050 and servo3.get_servo_pulsewidth(19) == 1050):
            error = 0
        else:
            error = 1

        print("Test 135 deg")
        servo2.set_servo_pulsewidth(13, 1950)
        servo3.set_servo_pulsewidth(19, 1950)
        time.sleep(1)
        if (servo2.get_servo_pulsewidth(13) == 1950 and servo3.get_servo_pulsewidth(19) == 1950):
            error = 0
        else:
            error = 1

        print("Motor Error: " + str(error))

        return

    def flapWings(self):   
        subprocess.call('sudo pigpiod', shell = True)
        servo1 = pigpio.pi()
        servo1.set_mode(18, pigpio.OUTPUT)
        servo1.set_PWM_frequency(18, 50)

        servo2 = pigpio.pi()
        servo2.set_mode(13, pigpio.OUTPUT)
        servo2.set_PWM_frequency(13, 50)

        servo3 = pigpio.pi()
        servo3.set_mode(19, pigpio.OUTPUT)
        servo3.set_PWM_frequency(19, 50)


        print("0 deg")
        servo1.set_servo_pulsewidth(18, 500)
        servo2.set_servo_pulsewidth(13, 500)
        servo3.set_servo_pulsewidth(19, 500)
        time.sleep(1)

        print("90 deg")
        servo1.set_servo_pulsewidth(18, 1500)
        time.sleep(1)


        servo2.set_servo_pulsewidth(13, 1050)
        servo3.set_servo_pulsewidth(19, 1050)
        time.sleep(1)


        for i in range(10):
            print("135 deg")
            servo2.set_servo_pulsewidth(13, 1950)
            servo3.set_servo_pulsewidth(19, 1950)
            time.sleep(1)

            print("45 deg")
            servo2.set_servo_pulsewidth(13, 1050)
            servo3.set_servo_pulsewidth(19, 1050)
            time.sleep(1)
            i += 1

        servo2.set_servo_pulsewidth(13, 500)
        servo3.set_servo_pulsewidth(19, 500)
        time.sleep(1)

        print("0 deg")
        servo1.set_servo_pulsewidth(18, 500)
        time.sleep(1)

        servo1.set_PWM_dutycycle(18, 0)
        servo1.set_PWM_frequency(18, 0)
        servo2.set_PWM_dutycycle(13, 0)
        servo2.set_PWM_frequency(13, 0)
        servo3.set_PWM_dutycycle(19, 0)
        servo3.set_PWM_dutycycle(19, 0)

if __name__ == '__main__':
    #Driver code
    motor = Motor()
    motor.testMotors()
    motor.flapWings()
