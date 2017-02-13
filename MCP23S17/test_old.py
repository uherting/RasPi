#!/usr/bin/python

#
# test script for ...
# playing around with a MCP23S17 circiut attached to the ...
# SPI bus of the raspberry pi
#

import sys
import os

# import core classes for Raspberry Pi
import spidev

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
