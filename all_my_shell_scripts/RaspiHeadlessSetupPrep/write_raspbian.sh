#!/bin/bash

# This scripts writes the latest image file to the SD card.
# The latest image is determined by the date/time stamp given in the file name.
BNAME=`basename $0 .sh`
DNAME=`dirname $0`

# define the location where the image file is located
IMG_ROOT_DIR="/home/uwe/Downloads/Raspi"

if [ $# -lt 1 ]
then
  echo "version expected (lite or desktop)"
  exit 1
fi

VERSION=""
if [ "$1" == "lite" ]; then
  VERSION="-lite"
fi

if [ "$1" == "desktop" ]; then
  VERSION=""
fi

IMG_FILE=`ls -d ${IMG_ROOT_DIR}/*-raspbian-stretch${VERSION}.img | sort | tail -n1`
DEVICE_WR=/dev/mmcblk0

echo "${IMG_FILE} gets written to TF card at ${DEVICE_WR}"
echo "In case this is not the image you want to be written or"
echo "the intended target device please push CTRL-c to stop the process"
echo "Otherwise push ENTER to start writing the image file ${IMG_FILE} to ${DEVICE_WR}"
read dummy_value

echo "start at `date`"
time sudo dd bs=4M if=${IMG_FILE} of=${DEVICE_WR} status=progress
sync
echo "finished at `date`"

