#!/usr/bin/python

import atexit
import signal
import sys
import time

import pyupm_grove as grove
import pyupm_grovespeaker as upmGrovespeaker
import pyupm_i2clcd as lcd

button = grove.GroveButton(8)
display = lcd.Jhd1313m1(0, 0x3E, 0x62)
knob = grove.GroveRotary(0)
light = grove.GroveLight(0)
relay = grove.GroveRelay(2)

def SIGINTHandler(signum, frame):
	raise SystemExit

def exitHandler():
	print "Exiting"
	sys.exit(0)

atexit.register(exitHandler)
signal.signal(signal.SIGINT, SIGINTHandler)

if __name__ == '__main__':

    message = "Hi! I'm Main!"

    while True:

        luxes = light.value()
        luxes = int(luxes)    
        display.setColor(luxes, luxes, luxes)
        display.clear()

        absdeg = knob.abs_deg()
        print "Abs values: %4d" % int(abs) , " raw %4d" % int(absdeg), "deg = %5.2f" % absrad , " rad "

        if button.value() is 1:
            display.setColor(255, 0, 0)
            display.setCursor(0,0)
            display.write(str(message))
            relay.on()
            time.sleep(1)
            relay.off()

