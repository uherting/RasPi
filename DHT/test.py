#!/usr/bin/python

#
# test script for ...
# playing around with a DHT22 sensor attached to a ...
# GPIO pin of the raspberry pi
#

import sys
import os

# import core classes for Raspberry Pi
import Adafruit_DHT

# add classes directory of current project to the search path in order
# to find custom classes used in this script
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/classes')

# import custom classes
import debuguh

#  script global setting of debugging and create the object to the debug class
debug = 1
duh = debuguh.debuguh_out() # create the object

# show some debugging info depending on the value of the parameter
duh.show_info(debug)

# determine type of sensor and GPIO pin
sensor = Adafruit_DHT.DHT22
gpio_pin = 4

# read data
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio_pin)

# output
print('Temperatur: {0:0.1f}*C Luftfeuchtigkeit: {1:0.1f}%'.format(temperature, humidity))
