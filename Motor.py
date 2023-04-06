#!/usr/bin/env python3
# Sharon Chu, Joseph Cannaday
# Junior Design 2023
import RPi.GPIO as GPIO
import pigpio
import time
import subprocess


class Motor:
    def __init__(self, name="snapdragon_wings", l_wing_pin = 12, r_wing_pin = 18, errorLed_pin = 8):
        self.name = name
        self.l_wing_pin = l_wing_pin
        self.r_wing_pin = r_wing_pin
        self.errorLed_pin = errorLed_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.errorLed_pin, GPIO.OUT)
        GPIO.output(self.errorLed_pin, GPIO.HIGH)
        return

    def testMotors(self):
        print("Testing motors")
        error = 0

        subprocess.call('sudo pigpiod', shell = True)

        l_wing = pigpio.pi()
        l_wing.set_mode(self.l_wing_pin, pigpio.OUTPUT)
        l_wing.set_PWM_frequency(self.l_wing_pin, 50)

        r_wing = pigpio.pi()
        r_wing.set_mode(self.r_wing_pin, pigpio.OUTPUT)
        r_wing.set_PWM_frequency(self.r_wing_pin, 50)
        
        print("Test 0 deg")
        l_wing.set_servo_pulsewidth(self.l_wing_pin, 500)
        r_wing.set_servo_pulsewidth(self.r_wing_pin, 500)
        time.sleep(1)
        if l_wing.get_servo_pulsewidth(self.l_wing_pin) == 500 and r_wing.get_servo_pulsewidth(self.r_wing_pin) == 500:
            error += 0
        else:
            error += 1

        print("Test 90 deg")
        l_wing.set_servo_pulsewidth(self.l_wing_pin, 1500)
        r_wing.set_servo_pulsewidth(self.r_wing_pin, 1500)
        time.sleep(1)
        if l_wing.get_servo_pulsewidth(self.l_wing_pin) == 1500 and r_wing.get_servo_pulsewidth(self.r_wing_pin) == 1500:
            error += 0
        else:
            error += 1

        print("Test 45 deg")
        l_wing.set_servo_pulsewidth(self.l_wing_pin, 1050)
        r_wing.set_servo_pulsewidth(self.r_wing_pin, 1050)
        time.sleep(1)
        if l_wing.get_servo_pulsewidth(self.l_wing_pin) == 1050 and r_wing.get_servo_pulsewidth(self.r_wing_pin) == 1050:
            error += 0
        else:
            error += 1

        print("Test 135 deg")
        l_wing.set_servo_pulsewidth(self.l_wing_pin, 1950)
        r_wing.set_servo_pulsewidth(self.r_wing_pin, 1950)
        time.sleep(1)
        if l_wing.get_servo_pulsewidth(self.l_wing_pin) == 1950 and r_wing.get_servo_pulsewidth(self.r_wing_pin) == 1950:
            error += 0
        else:
            error += 1

        # if error code is not 0, turn on motor error LED
        if error:
            GPIO.output(self.errorLed_pin, GPIO.LOW)

        return

    def flapWings(self, duration):
        subprocess.call('sudo pigpiod', shell = True)

        l_wing = pigpio.pi()
        l_wing.set_mode(self.l_wing_pin, pigpio.OUTPUT)
        l_wing.set_PWM_frequency(self.l_wing_pin, 50)

        r_wing = pigpio.pi()
        r_wing.set_mode(self.r_wing_pin, pigpio.OUTPUT)
        r_wing.set_PWM_frequency(self.r_wing_pin, 50)


        print("0 deg")
        l_wing.set_servo_pulsewidth(self.l_wing_pin, 500)
        r_wing.set_servo_pulsewidth(self.r_wing_pin, 500)
        time.sleep(1)

        print("45 deg")
        l_wing.set_servo_pulsewidth(self.l_wing_pin, 1050)
        r_wing.set_servo_pulsewidth(self.r_wing_pin, 1050)
        time.sleep(1)

        # duration is in seconds; it takes 2 seconds to complete a flapping cycle, thus divide by 2
        for i in range(duration // 2):
            print("135 deg")
            l_wing.set_servo_pulsewidth(self.l_wing_pin, 1950)
            r_wing.set_servo_pulsewidth(self.r_wing_pin, 1950)
            time.sleep(1)

            print("45 deg")
            l_wing.set_servo_pulsewidth(self.l_wing_pin, 1050)
            r_wing.set_servo_pulsewidth(self.r_wing_pin, 1050)
            time.sleep(1)
            i += 1

        l_wing.set_servo_pulsewidth(self.l_wing_pin, 500)
        r_wing.set_servo_pulsewidth(self.r_wing_pin, 500)
        time.sleep(1)

        print("0 deg")
        l_wing.set_PWM_dutycycle(self.l_wing_pin, 0)
        l_wing.set_PWM_frequency(self.l_wing_pin, 0)
        r_wing.set_PWM_dutycycle(self.r_wing_pin, 0)
        r_wing.set_PWM_dutycycle(self.r_wing_pin, 0)

if __name__=='__main__':
    motor = Motor()
    motor.testMotors()
    motor.flapWings(10)
