#!/usr/bin/env python3
# Sharon Chu, Joseph Cannaday
# Junior Design 2023
import RPi.GPIO as GPIO
import pigpio
import time

class Light:
    def __init__(self, ledPin=14, name = "snapdragon_LED"):
        self.name = name
        self.ledPin = ledPin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.ledPin, GPIO.OUT)
        GPIO.output(self.ledPin, GPIO.HIGH)

    def testLed(self):
        # Turn on lights
        self.setLow()

        print("Light on")
        time.sleep(10)
        print("Light off")

        # Turn off lights
        self.setHigh()
        print('LED Test Complete')
    
    def setHigh(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.output(self.ledPin, GPIO.HIGH)

    def setLow(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.output(self.ledPin, GPIO.LOW)

if __name__ == '__main__':
    LED_PIN = 14
    led = Light()
    led.testLed(LED_PIN)