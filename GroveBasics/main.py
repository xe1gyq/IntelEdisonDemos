#!/usr/bin/python

import atexit
import dweepy
import signal
import sys
import time

import pyupm_grove as grove
import pyupm_grovespeaker as upmGrovespeaker
import pyupm_i2clcd as lcd

button = grove.GroveButton(8)
display = lcd.Jhd1313m1(0, 0x3E, 0x62)
knob = grove.GroveRotary(0)
light = grove.GroveLight(1)
relay = grove.GroveRelay(2)

def SIGINTHandler(signum, frame):
	raise SystemExit

def exitHandler():
	print "Exiting"
	sys.exit(0)

atexit.register(exitHandler)
signal.signal(signal.SIGINT, SIGINTHandler)

if __name__ == '__main__':

    message = "ITESM IoT Lab!"

    while True:

        luxes = light.value()
        luxes = int(luxes)    

        abs = knob.abs_value()
        messagelcd = "Rotary Value %d" % int(abs)

        display.clear()
        display.setColor(luxes, luxes, luxes)
        display.setCursor(0,0)
        display.write(str(message))
        display.setCursor(1,0)
        display.write(str(messagelcd))

        if button.value() is 1:
            display.setColor(255, 0, 0)
            relay.on()
            time.sleep(.5)
            relay.off()

        data = {}
        data['alive'] = "1"
        data['luxes'] =  luxes
        data['abs'] =  abs
        data['message'] = message + ' ' + str(luxes)
        dweepy.dweet_for('TheIoTLearningInitiative', data)

        time.sleep(.25)
