from time import time, sleep
from gpiozero import MotionSensor

#
# measuring tool for checking payload on CPU
#

# for details see https://github.com/RPi-Distro/python-gpiozero/issues/227

# a note from the ticket:
# In GPIO Zero this draws a constant 10-12% of CPU on the Raspberry PI Zero,
# but with the older RPI.GPIO library and GPIO.add_event_detect CPU usage
# barely goes above 1%.

left = MotionSensor(20)
# right = MotionSensor(21)

last_update = time()
last_reset = last_update


def pir_change():
    print("Change")
    global last_reset
    last_reset = time()


left.when_motion = pir_change
# right.when_motion = pir_change

while True:
    if time() - last_update >= 10:
        print("Idle %d secs" % (time() - last_reset))
        last_update = time()
    sleep(0.02)
