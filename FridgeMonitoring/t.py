# # ! #/usr/bin/python3

import UH.w1.find_sensors as w1fs

# if __name__ == "__main__":
#print(__name__ + "\n")

w1s = w1fs.FindSensors
w1s.get_that()

import rrdtool

# in real life data_sources would be populated in loop or something similar
data_sources = ['DS:speed1:COUNTER:600:U:U',
                'DS:speed2:COUNTER:600:U:U',
                'DS:speed3:COUNTER:600:U:U']

rrdtool.create('speed.rrd',
               '--start', '920804400',
               data_sources,
               'RRA:AVERAGE:0.5:1:24',
               'RRA:AVERAGE:0.5:6:10')
