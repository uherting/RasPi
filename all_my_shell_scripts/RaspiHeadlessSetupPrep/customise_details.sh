#!/bin/bash

if [ "`whoami`" != "root" ]
then
  echo "NOTE: For execution of this script you need root use priviledges. Script stops here."
  exit 99
fi

BNAME=`basename $0 .sh`
DNAME=`dirname $0`

HOSTNAME_NEW=$1

ADDITIONAL_CUSTOMISATION_SCRIPT="myVeryOwnCustScript.sh"


#TGT_ROOT_DIR="/root/Raspi_UH/headless_install/zero"

BOOT_DIR="boot"
ROOT_DIR="rootfs"

. ${DNAME}/mod.conf

if [ $# -lt 1 ]
then
  echo "hostname expected"
  exit 1
fi

FILE_TO_WORK_ON=""

# function declaration follows
function getNextNumber() {
  local retVal=$1
  ((retVal++))
  echo "${retVal}"
}


function getBackupFileName () {
  local BASE_FILENAME_BAK="$1"
  local PREFIX="_bak.${2}"

  if [ $2 -eq 0 ]
  then
    PREFIX=""
  fi

  echo "${BASE_FILENAME_BAK}${PREFIX}"
}


function backupFiles() {
  local BASE_FILENAME=$1
  local nextInLineNumber=0
  local FILE_TO_WORK_ON=""
  local FILE_TO_WORK_MV_TGT=""

  #echo "BASE_FILENAME = ${BASE_FILENAME}"

  for i in 4 3 2 1 0
  do
echo " "
echo "LOOP START"
    FILE_TO_WORK_ON=$(getBackupFileName ${BASE_FILENAME} ${i})
    echo "FILE_TO_WORK_ON=${FILE_TO_WORK_ON}"

    if [ $i -eq 4 ]
    then
      if [ -f ${FILE_TO_WORK_ON} ]
      then
        echo "ACTION: rm -f ${FILE_TO_WORK_ON}"
        #rm -f ${FILE_TO_WORK_ON}
      fi
    else
      nextInLineNumber=$(getNextNumber $i)
      FILE_TO_WORK_MV_TGT=$(getBackupFileName ${BASE_FILENAME} ${nextInLineNumber})
      echo "FILE_TO_WORK_MV_TGT=${FILE_TO_WORK_MV_TGT}"
      if [ -f ${FILE_TO_WORK_ON} ]
       then
        if [ $i -gt 0 ]
        then
          echo "ACTION: mv ${FILE_TO_WORK_ON} ${FILE_TO_WORK_MV_TGT}"
          #mv ${FILE_TO_WORK_ON} ${FILE_TO_WORK_MV_TGT}"
        else
          echo "ACTION: cp -a ${FILE_TO_WORK_ON} ${FILE_TO_WORK_MV_TGT}"
          #cp -a ${FILE_TO_WORK_ON} ${FILE_TO_WORK_MV_TGT}"
        fi
      else
          echo "ACTION: no action required"
      fi
    fi
echo "LOOP FINISH"
  done
  
  return 0
}


function customiseBoot() {
  # create tailor made files from template files in boot partition
  for FILE_NAME in /config.txt
  do
    # backup the file to be newly created
    backupFiles ${FILE_NAME}

    # create the file from the template or otherwise
    #foobar....
  done

  return 0
}


function customiseRoot() {
  # create tailor made files from template files in root partition
  for FILE_NAME in /etc/hostname /etc/hosts
  do
    # preparation
    FILE_IN="${TEMPLATE_LOCATION_ROOT}${FILE_NAME}"
    FILE_OUT="${IMG_LOCATION_EDIT}/${ROOT_DIR}${FILE_NAME}"

    # backup the file to be newly created
    backupFile(${FILE_NAME})

    # create the file from the template
    echo "creating ${FILE_NAME} from template"
    #sed -e "s/YYYYYY/${HOSTNAME_NEW}/g" < ${FILE_IN} > ${FILE_OUT}
    echo "TEMPLATE: ${FILE_IN}"
    echo "FILE_OUT: ${FILE_OUT}"
  done

  return 0
}


#
#
# now the "real" thing: 
# execution of main functions for 
# customising boot and root partition
#
#
cd ${IMG_LOCATION_EDIT}

for partition in 1 2
do
  echo "partition ${partition} in progress"

  BASE_DIR_EDIT=`ls -d *p${partition} 

  # boot
  if [ ${partition} -eq 1 ]
  then
    echo "Customising boot partition"
    customiseBoot()
  fi

  # root
  if [ ${partition} -eq 2 ]
  then
    echo "Customising root partition"
    customiseRoot()
  fi
done

cd -

exit 0

if [ -x ${ADDITIONAL_CUSTOMISATION_SCRIPT} ]
then
 echo "trying to execute additional customisation script"
 ${ADDITIONAL_CUSTOMISATION_SCRIPT}
 ADDITIONAL_CUSTOMISATION_EXIT_CODE=$?
 if [ ${ADDITIONAL_CUSTOMISATION_EXIT_CODE} -ne 0 ]
 then
   echo "additional customisation script ended with error / exit code ${ADDITIONAL_CUSTOMISATION_EXIT_CODE}."
 fi
fi
