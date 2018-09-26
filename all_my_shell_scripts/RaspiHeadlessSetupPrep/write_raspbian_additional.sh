#!/bin/bash

BNAME=`basename $0 .sh`
DNAME=`dirname $0`


echo "No proper programming done here so far. Sorry."
exit 1


SRC_ROOT_DIR="/root/Raspi_UH/headless_install/zero"
TGT_ROOT_DIR="/root/Raspi_UH_media"

echo "start at `date`"
echo "cp -a ${SRC_ROOT_DIR}/* ${TGT_ROOT_DIR}"
cp -a ${SRC_ROOT_DIR}/* ${TGT_ROOT_DIR}
echo "finished at `date`"

