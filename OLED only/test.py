#!/usr/bin/python

#
# test script for ...
# playing around with a DHT22 sensor attached to a GPIO pin of the raspberry pi and a
# OLED for displaying the values
#

import sys
import os
import time
import threading

# import core classes for Raspberry Pi
# import Adafruit_DHT

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

# Einbindung 0,96 Zoll OLED Display 128x64 Pixel
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont


# Global für Anzahl der Temperaturanzeigen auf Display
displaySensorBezeichnung = ""
displayTempWert = ""
a = u"°"  # damit Sonderzeichen korrekt dargestellt wird

# Global für Aktivitätsstatus einzelner Threads/Programmteile
Display_aktiv = True

#
# functions
# -----------------------------


def aktuelleZeit(werta, wertb):
    zeitpunktMessung = time.localtime()
    jahr, monat, tag = zeitpunktMessung[0:3]
    stunde, minute, sekunde = zeitpunktMessung[3:6]
    systemUhrzeit = str(stunde).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(sekunde).zfill(2)
    systemDatum = str(tag).zfill(2) + "." + str(monat).zfill(2) + "." + str(jahr)
    if werta == "time" and wertb == "date":
        ermittelteZeit = systemUhrzeit + " " + systemDatum
    elif werta == "date" and wertb == "time":
        ermittelteZeit = systemDatum + " " + systemUhrzeit
    elif werta == "time" and wertb == "":
        ermittelteZeit = systemUhrzeit
    elif werta == "date" and wertb == "":
        ermittelteZeit = systemDatum
    else:
        ermittelteZeit = zeitpunktMessung
    return ermittelteZeit


def displaySensorwertAusgabe():
    global displaySensorBezeichnung, displayTempWert, a, dhtSensorLuftfeuchtigkeit, dhtSensorTemperatur
    displaySensorBezeichnung = "DHT22 Sensor :"
    displayTempWert = dhtSensorLuftfeuchtigkeit + " % " + dhtSensorTemperatur + " " + a + "C"


# Display einrichten

# Raspberry Pi pin configuration:
RST = 24

# Display 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# First define some constants to allow easy resizing of shapes.
padding = 2
shape_width = 20
top = padding
bottom = height - padding

# Move left to right keeping track of the current x position for drawing shapes.
x = padding

# Load default font.
# font = ImageFont.load_default() # Wenn keine eigene Schrift vorhanden ist!!!!
font = ImageFont.truetype("font/arial.ttf", 12)  # Schriftart, Schriftgröße
font_b = ImageFont.truetype("font/arial.ttf", 18)
font_c = ImageFont.truetype("font/arial.ttf", 14)

# Write one line of text.
draw.text((x, top + 25), 'Start', font=font_b, fill=255)

# Display image.
disp.image(image)
disp.display()

# Abfrage des DHT Sendor in eigenem Thread starten
sensorenAbfrageThread = threading.Thread(target=sensorenAbfrage)  # Sensorenabfrage
sensorenAbfrageThread.start()
time.sleep(5)  # damit alle Sensorwerte zum Start eingelesen sind

# Hauptroutine
# TODO: Hauptroutine edited by UH finishes after z loops
z = 0
# while Display_aktiv:
while z < 5:
    draw.rectangle((0, 0, width, height), outline=0, fill=0)  # Display leeren
    displayTime = aktuelleZeit("time", "date")  # bei Abfrage "date","time" ändert die Reihenfolge der Ausgabe
    draw.text((x, top), displaySensorBezeichnung, font=font, fill=255)
    draw.text((x, top + 20), displayTempWert, font=font_c, fill=255)
    draw.line((x, top + 45, x + width, top + 45), fill=255)
    draw.text((x, top + 50), displayTime, font=font, fill=255)
    disp.image(image)
    disp.display()
    z = z + 1
