#!/usr/bin/env bash

BNAME=`basename $0 .sh`
DNAME=`dirname $0`
DIR_NAME=`echo "$BNAME" | cut -f 2 -d "_"`
REPO_PATH=`echo "$BNAME" | cut -f 2- -d "_"`

if [ "${BNAME}" == "gitclone" ]
then
  # create sym links if not existing
  cd ${DNAME}
  for TGT in gitclone_misc.sh gitclone_misc_upd.sh gitclone_UH.sh
  do
    if [ ! -h ${TGT} ]
    then
      ln -s ${BNAME}.sh ${TGT}
    fi
  done
  cd -
  exit 0
fi

if [ ! -d ${DIR_NAME} ]
then
  echo
  # if the dir does not exist then show the index finger or so...
  echo "dir ${DIR_NAME} does not exist!"
  exit 1
fi

function uh_gitclone {
  git clone $1
}

#
# now act according to "$DIR_NAME"
#
if [ "$DIR_NAME" == "UH" ]
then
    cd ${DIR_NAME}
    uh_gitclone https://github.com/uherting/RasPi.git
    uh_gitclone https://github.com/uherting/PyLibs.git
    uh_gitclone https://github.com/uherting/TimeCheck.git
    cd -
fi

if [ "$DIR_NAME" == "misc" ]
then
    cd ${DIR_NAME}
    uh_gitclone https://github.com/waveform80/picamera.git
    uh_gitclone https://github.com/petrockblog/RPi-MCP23S17.git
    uh_gitclone https://github.com/RPi-Distro/python-gpiozero.git
    uh_gitclone https://github.com/adafruit/Adafruit_Python_DHT.git
    uh_gitclone https://github.com/adafruit/Adafruit_Python_SSD1306.git
    uh_gitclone https://github.com/adafruit/Adafruit_Python_CharLCD.git
    uh_gitclone https://github.com/adafruit/Adafruit_Python_GPIO.git
    uh_gitclone https://github.com/mxgxw/MFRC522-python.git
    uh_gitclone https://github.com/steve71/RasPiBrew.git
    uh_gitclone https://github.com/timofurrer/w1thermsensor.git
    uh_gitclone https://github.com/python-telegram-bot/python-telegram-bot.git
    uh_gitclone https://github.com/nickoala/telepot.git

    # clone repositories which are necessary for epsilon only
#    if [ "`hostname`" == "epsilon" ]
#    then
#      uh_gitclone https://github.com/nodemcu/nodemcu-devkit-v1.0.git
#      uh_gitclone https://github.com/nodemcu/nodemcu-firmware.git
#    fi

    cd -
fi

