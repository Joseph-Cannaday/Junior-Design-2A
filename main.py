#!/usr/bin/env python3
# Joseph Cannaday
# Junior Design 2023
import Connect
import Motor
import Light
import Speaker

def doTest():
    return

def startPlay():
    led = Light()
    wings = Motor()
    spkr = Speaker()
    while 1:
        # TODO connection object
        #wait for line
        # when line received:
            led.toggle()
            spkr.sayLine()
            wings.flapWings()

def readSwitch():
    #do something
    return state

if __name__ == "__main__":
    #initialize switch and read status
    switch_pos = 1
    if switch_pos==1:
        doTest()
    else:
        startPlay()
