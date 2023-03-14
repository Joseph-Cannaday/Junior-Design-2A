#!/usr/bin/env python3
# Joseph Cannaday
# Junior Design 2023
import Connect
import Motor
import Light
import Speaker
import time

def doTest():
    led = Light.Light()
    wings = Motor.Motor()
    spkr = Speaker.Speaker()
    return

def startPlay():
    # declare robot components
    led = Light.Light()
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
                    led.set_low()
                    sleeptime = spkr.sayLine('command')# return the amount of time the speaker will take to play the line (in seconds)
                    wings.flapWings()
                    time.sleep(sleeptime)# sleep for as long as speaker needs to finish lines
                    c1.s.send(c1.encode_json({ "cmd": "LINE_COMPLETE" }))
                    #make sure pwm/led deactivates
                    led.set_high()
        except socket.error:
            print("[CLIENT] Failed...", )
            c1.s.close()

def readSwitch():
    #do something
    state = 1
    return state

if __name__ == "__main__":
    #initialize switch and read status
    switch_pos = readSwitch()
    if switch_pos == 0:
        doTest()
    else:
        startPlay()
