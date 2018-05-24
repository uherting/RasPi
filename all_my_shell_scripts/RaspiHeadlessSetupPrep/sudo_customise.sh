#!/bin/bash

BNAME=`basename $0 .sh`
DNAME=`dirname $0`

TGT_ROOT_DIR="/root/Raspi_UH/headless_install/zero"
BOOT_DIR="boot"
ROOT_DIR="rootfs"

if [ $# -lt 1 ]
then
  echo "hostname expected"
  exit 1
fi

HOSTNAME_NEW=$1

for i in hostname hosts
do
  FILE="${TGT_ROOT_DIR}/${ROOT_DIR}/etc/$i"
  echo "creating $FILE from template"
  sed -e "s/YYYYYY/${HOSTNAME_NEW}/g" < ${FILE}.tmpl > ${FILE}
done

