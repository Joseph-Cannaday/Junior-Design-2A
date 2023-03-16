#!/usr/bin/env python3
# Joseph Cannaday
# Junior Design 2023
import Connect
import Motor
import Light
import Speaker
import time
import socket
import RPi.GPIO as GPIO

def doTest():
    led = Light.Light(ledPin=14)
    wings = Motor.Motor()
    spkr = Speaker.Speaker()
    wings.testMotors()
    led.testLed()

def startPlay():
    DIRECTOR_HOST = "107.23.238.206"
    DIRECTOR_PORT = 3336
    LED_PIN = 14
    # declare robot components
    led = Light.Light(ledPin=LED_PIN)
    wings = Motor.Motor()
    spkr = Speaker.Speaker()
    c1 = Connect.Connect()
    while 1:
        c1.connect(DIRECTOR_HOST, DIRECTOR_PORT)
    
        if (c1.status != 'CONNECTED'): return print("Failed connection, exiting")
        try:
            while True:
                command = c1.decode_message(c1.s.recv(1024).decode())# return command for line, else return ''
                # program will hang on c1.s.recv until it receives the next line
                if command:
                    print(f"[CLIENT] Got a line: {command}")
                    led.setLow()
                    sleeptime = spkr.sayLine(command)# return the amount of time the speaker will take to play the line (in seconds)
                    wings.flapWings()
                    time.sleep(sleeptime)# sleep for as long as speaker needs to finish lines
                    c1.s.send(c1.encode_json({ "cmd": "LINE_COMPLETE" }))
                    #make sure pwm/led deactivates
                    led.setHigh()
        except socket.error:
            print("[CLIENT] Failed...", )
            c1.s.close()

def readSwitch():
    switch_pin = 24# GPIO 24, pin 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(switch_pin, GPIO.IN)
    state = GPIO.input(switch_pin)
    return state

if __name__ == "__main__":
    #initialize switch and read status
    while 1:
        try:
            if not readSwitch():
                doTest()
            else:
                startPlay()
        except:
            print('[Error] Ending Process')
