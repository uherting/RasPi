if [ ! -d misc ]
then
  echo "dir misc does not exist!"
  exit 1
fi

cd misc

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

