#!/bin/bash

BNAME=`basename $0 .sh`
DNAME=`dirname $0`

HOSTNAME_NEW=$1

ADDITIONAL_CUSTOMISATION_SCRIPT="myVeryOwnCustScript.sh"
TGT_ROOT_DIR="/root/Raspi_UH/headless_install/zero"
BOOT_DIR="boot"
ROOT_DIR="rootfs"

if [ $# -lt 1 ]
then
  echo "hostname expected"
  exit 1
fi

# create tailor made /etc/hostname and /etc/hosts from template files
for i in hostname hosts
do
  FILE="${TGT_ROOT_DIR}/${ROOT_DIR}/etc/$i"
  echo "creating $FILE from template"
  sed -e "s/YYYYYY/${HOSTNAME_NEW}/g" < ${FILE}.tmpl > ${FILE}
done

if [ -f ${ADDITIONAL_CUSTOMISATION_SCRIPT} ]
then
 echo "trying to execute additional customisation script"
 ${ADDITIONAL_CUSTOMISATION_SCRIPT}
 ADDITIONAL_CUSTOMISATION_EXIT_CODE=$?
 if [ ${ADDITIONAL_CUSTOMISATION_EXIT_CODE} -ne 0 ]
 then
   echo "additional customisation script ended with error / exit code ${ADDITIONAL_CUSTOMISATION_EXIT_CODE}."
 fi
fi