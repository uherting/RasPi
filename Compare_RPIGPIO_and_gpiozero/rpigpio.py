from time import time, sleep
from RPi import GPIO

#
# measuring tool for checking payload on CPU
#

# for details see https://github.com/RPi-Distro/python-gpiozero/issues/227

# a note from the ticket:
# In GPIO Zero this draws a constant 10-12% of CPU on the Raspberry PI Zero,
# but with the older RPI.GPIO library and GPIO.add_event_detect CPU usage
# barely goes above 1%.

GPIO.setmode(GPIO.BCM)

LEFT_PIR = 20
RIGHT_PIR = 21

GPIO.setup(LEFT_PIR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RIGHT_PIR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

last_update = time()
last_reset = last_update


def pir_change(channel):
    print("Change")
    global last_reset
    last_reset = time()


GPIO.add_event_detect(LEFT_PIR, GPIO.RISING, callback=pir_change, bouncetime=1000)
GPIO.add_event_detect(RIGHT_PIR, GPIO.RISING, callback=pir_change, bouncetime=1000)

while True:
    if time() - last_update >= 10:
        print("Idle %d secs" % (time() - last_reset))
        last_update = time()
    sleep(0.02)