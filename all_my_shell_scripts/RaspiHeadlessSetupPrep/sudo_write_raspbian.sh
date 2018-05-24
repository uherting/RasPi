#!/bin/bash

BNAME=`basename $0 .sh`
DNAME=`dirname $0`

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

IMG_FILE=`ls -drt /home/uwe/Downloads/Raspi/*-raspbian-stretch${VERSION}.img | tail -n1`
DEVICE_WR=/dev/mmcblk0

echo "${IMG_FILE} gets written to TF card at ${DEVICE_WR}"

echo "start at `date`"
time dd bs=4M if=${IMG_FILE} of=${DEVICE_WR} status=progress
sync
echo "finished at `date`"

