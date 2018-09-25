if [ $# -lt 1 ]
then
  echo "version expected (lite or desktop)"
  exit 1
fi

VERSION=""
if [ "$1" == "lite" ]; then
  VERSION="_lite"
fi

if [ "$1" == "desktop" ]; then
  VERSION=""
fi

wget --trust-server-names https://downloads.raspberrypi.org/raspbian${VERSION}_latest

