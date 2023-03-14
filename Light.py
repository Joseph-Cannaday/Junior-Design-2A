#!/usr/bin/env python3
# Sharon Chu, Joseph Cannaday
# Junior Design 2023
import RPi.GPIO as GPIO
import pigpio
import time

LED_PIN = 14
class Light:
    def __init__(self, ledPin=14, name = "snapdragon_LED"):
        self.name = name
        self.ledPin = ledPin

    def testLed(self):
        error = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.ledPin, GPIO.OUT)
        GPIO.output(self.ledPin, GPIO.LOW)
        #GPIO.setup(self.ledPin, GPIO.IN)
        #if (GPIO.input(self.ledPin) == 0):
        #    error = 0
        #else:
        #    error = 1

        print("Light on")
        time.sleep(10)
        print("Light off")

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.ledPin, GPIO.OUT)
        GPIO.output(self.ledPin, GPIO.HIGH)
        #GPIO.setup(self.ledPin, GPIO.IN)
        #if (GPIO.input(self.ledPin) == 1):
        #    error = 0
        #else:
        #    error = 1
        print("LED Error: " + str(error))
        return

    def doLed(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.ledPin, GPIO.OUT)
        # set ledPin to low to activate
        GPIO.output(self.ledPin, GPIO.LOW)
        return

if __name__ == '__main__':
    led = Light()
    led.testLed(LED_PIN)