#!/usr/bin/python3

import sys
#import os
from time import sleep

# special to Raspberry Pi
from gpiozero import PiBoardInfo

# add classes directory of current project to the search path in order
# to find custom classes used in this script
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/classes')

#sleep(1)

# import custom class
# import
# import

# script global setting of debugging
debug = 1

if debug == 1:
    pi_model = 'M'  # PiBoardInfo.model
    pi_rev = 'R'  # PiBoardInfo.revision
    pi_pcbrev = 'PR'  # PiBoardInfo.pcb_revision
else:
    pi_model = PiBoardInfo.model
    pi_rev = PiBoardInfo.revision
    pi_pcbrev = PiBoardInfo.pcb_revision

print('PiBoardInfo')
print('\tModel: ' + pi_model)
print('\tRevision: ' + pi_rev)
print('\tPCB-Rev.: ' + pi_pcbrev)
