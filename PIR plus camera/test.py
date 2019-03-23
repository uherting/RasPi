#
#
# purpose: playing around with motion detection (PIR and the camera)
# trigger: PIR
# hostname:
# location:
#
#

# import sys
# import os
import time
import threading
# from datetime import datetime
import datetime
# from signal import pause

# import core classes for Raspberry Pi
from gpiozero import MotionSensor, LED
from picamera import PiCamera

# import custom classes
import debuguh

# create objects from gpiozero classes
pin_motion_sensor = 4
pin_led = 16
used_sensor_01 = MotionSensor(pin_motion_sensor)  # PIR connected to pin x
led_01 = LED(pin_led)  # LED connected to pin x
capture_enable = False

# create objects from other tool classes
camera = PiCamera()


def current_time(val_a, val_b):
    local_time = time.localtime()
    now_year, now_month, now_day = local_time[0:3]
    now_hour, now_minute, now_second = local_time[3:6]
    system_time = str(now_hour).zfill(2) + ":" + str(now_minute).zfill(2) + ":" + str(now_second).zfill(2)
    system_date = str(now_day).zfill(2) + "." + str(now_month).zfill(2) + "." + str(now_year)

    if val_a == "time" and val_b == "date":
        time_to_return = system_time + " " + system_date
    elif val_a == "date" and val_b == "time":
        time_to_return = system_date + " " + system_time
    elif val_a == "time" and val_b == "":
        time_to_return = system_time
    elif val_a == "date" and val_b == "":
        time_to_return = system_date
    else:
        time_to_return = local_time

    return time_to_return


def capture():
    time_stamp = datetime.datetime.now().isoformat()
    camera.capture('/home/pi/%s.jpg' % time_stamp)


def sensors_check():
    global used_sensor_01, led_01, camera, capture_enable

    print("Thread for checking sensors started.")

    while True:
        used_sensor_01.wait_for_motion()
        print("Motion detected at " + current_time("time", "date"))

        led_01.on()

        if capture_enable:
            capture()

        time.sleep(1)
        led_01.off()


# a few debug tests first
#  script global setting of debugging and create the object to the debug class
debug = 1
duh = debuguh.debuguh_out()  # create the object

# show some debugging info depending on the value of the parameter
duh.show_info(debug)

#
#
# now "the real thing" (TM)
#
#

# start check of PIR sensor in its own thread
sensors_check_thread = threading.Thread(target=sensors_check)
sensors_check_thread.start()
# time.sleep(5)  # all sensor values have to be read right at the beginning

# main routine
# the main loop finishes after z loops for debugging purposes
z = 5
i = 0
while i < z:
    # display of time and date
    # current_time("date","time") will change the order of the output
    displayTime = current_time("time", "date")
    print(displayTime)

    time.sleep(5)

    i += 1
