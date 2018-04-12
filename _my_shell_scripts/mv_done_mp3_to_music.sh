#!/bin/bash

# Naming convention mp3 files: "<artist name> - <title name> - remark.mp3"

# define the Internal Field Separator that is used for word splitting after expansion
# needed if file name contains a space (0x20)
IFS=$'\n'

function mv_file {
  SRC_DIR="${HOME}/VideoEditing/Video2/mp3"
  TGT_DIR="${HOME}/Music"

  if [ ! -d ${TGT_DIR} ]
  then
    mkdir -p ${TGT_DIR}
  fi

  for i in ${SRC_DIR}/*.mp3
  do
    BN=`basename $i`
    ARTIST=`echo $BN | cut -f 1 -d "-"`
    ARTIST=`basename ${ARTIST} \ `
    echo "${ARTIST} # FILE: $i"
    DWNLD_DIR="${TGT_DIR}/${ARTIST}/Downloaded"
    if [ ! -d ${DWNLD_DIR} ]
    then
      mkdir -p ${DWNLD_DIR}
    fi
    mv $i ${DWNLD_DIR}
  done
}

function removeSpaceFromDirNameEnd {
  TGT_DIR="${HOME}/Music"
  SRC_DIR=${TGT_DIR}

  cd ${TGT_DIR}
  if [ $? -ne 0 ]
  then
    echo "ERROR: cannot cd to ${TGT_DIR}"
    exit 1
  fi
  pwd
  echo "."
  echo "."
  echo "."

  for i in ${SRC_DIR}/*\ 
  do
    ARTIST=`basename $i \ `
    MV_DIR="./${ARTIST}"
    echo "#$i#${MV_DIR}#"
    if [ -d ${MV_DIR} ]
    then
      echo "WARNING: ${MV_DIR} exists"
    else
      mv $i ${MV_DIR}
    fi
  done
}

mv_file
