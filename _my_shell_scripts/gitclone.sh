#!/usr/bin/env bash

BNAME=`basename $0 .sh`
DIR_NAME=`echo "$BNAME" | cut -f 2 -d "_"`

if [ ! -d ${DIR_NAME} ]
then
  # if the dir does not exist then show the index finger or so...
  echo "dir ${DIR_NAME} does not exist!"
  exit 1
fi

#
# now act according to "$DIR_NAME"
#
if [ "$DIR_NAME" == "UH" ]
then
    cd ${DIR_NAME}
    git clone https://github.com/uherting/RasPi.git
    git clone https://github.com/uherting/PyLibs.git
    git clone https://github.com/uherting/TimeCheck.git
    cd -
fi

if [ "$DIR_NAME" == "misc" ]
then
    cd ${DIR_NAME}
    git clone https://github.com/waveform80/picamera.git
    git clone https://github.com/petrockblog/RPi-MCP23S17.git
    git clone https://github.com/RPi-Distro/python-gpiozero.git
    git clone https://github.com/adafruit/Adafruit_Python_DHT.git
    git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
    git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git
    git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
    git clone https://github.com/mxgxw/MFRC522-python.git
    mv MFRC522-python MFRC522-python---mxgxw
    git clone https://github.com/rasplay/MFRC522-python.git
    mv MFRC522-python MFRC522-python---rasplay
    git clone https://github.com/steve71/RasPiBrew.git
    git clone https://github.com/timofurrer/w1thermsensor.git
    cd -
fi

