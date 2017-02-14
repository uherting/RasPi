#!/usr/bin/python

#
# test script for ...
# playing around with a DHT22 sensor attached to a GPIO pin of the raspberry pi and a
# OLED for displaying the values
#

import sys
import os

# import core classes for Raspberry Pi
#import Adafruit_GPIO.I2C as I2C

# add classes directory of current project to the search path in order
# to find custom classes used in this script
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/classes')

# import custom classes
import debuguh

#  script global setting of debugging and create the object to the debug class
debug = 1
duh = debuguh.debuguh_out()  # create the object

# show some debugging info depending on the value of the parameter
duh.show_info(debug)

#pcf8574_01 = I2C.Device(0x21, 1)
