#!/bin/bash

#
# source: https://unix.stackexchange.com/questions/316401/how-to-mount-a-disk-image-from-the-command-line/430415#430415
#
# purpose: this script (un)mounts the image and its containing partitions

BNAME=`basename $0 .sh`
DNAME=`dirname $0`

# if this script was called under its real name it just creates
# the sym links sudo_loop_mount_mnt and sudo_loop_mount_umnt which
# are to be used to mount the image on a loop device.
if [ "${BNAME}" == "loop_mount" ]
then
  # change to the directory where this script is located
  # (the sym links are created at the same location as the script is located)
  cd ${DNAME}

  for TGT in loop_mount_mnt loop_mount_umnt
  do
    if [ ! -h ${TGT} ]
    then
      echo "create sym link ${TGT}.sh"
      ln -s ${BNAME}.sh ${TGT}.sh
    fi
  done

  # change back to the directory where we came from
  cd -

  echo "sym links were created"
  exit 99
fi

if [ $# -lt 1 ]
then
  echo "Usage $0 <image_filename>.img"
  exit 1
fi


# mount the image and its containing partitions
if [ "${BNAME}" == "loop_mount_mnt" ]
then
  img=`readlink -f $1`
  echo "The given file name of the image points to ${img}. If this is not correct please push CTRL-c."
  echo "Otherwise push ENTER to continue."
  read dummy_value

  # mount the img file on the next available loop device and assign the name of the device to a variable
  dev="$(sudo losetup --show -f -P "$img")"
  echo "$dev"
  # loop through the partitions contained in the img file and mount them to /mnt/<partition_name>
  for part in "$dev"?*; do
    if [ "$part" = "${dev}p*" ]; then
      part="${dev}"
    fi
    dst="/mnt/$(basename "$part")"
    echo "$dst"
    sudo mkdir -p "$dst"
    sudo mount "$part" "$dst"
  done
fi


# unmount the image and its containing partitions from 
if [ "${BNAME}" == "loop_mount_umnt" ]
then
  img=`readlink -f $1`
  echo "The given file name of the image points to ${img}. If this is not correct please push CTRL-c."
  echo "Otherwise push ENTER to continue."
  read dummy_value

  # define the loop device
  # dev="`sudo losetup -l | grep /home/uwe/Downloads/Raspi/2018-99-99-raspbian-stretch-lite.img | cut -f1 -d\" \"`"
  dev="`sudo losetup -l | grep ${img} | cut -f1 -d\" \"`"

  # loop through the partitions presented through the loop dev and unmount them
  for part in "$dev"?*; do
    if [ "$part" = "${dev}p*" ]; then
      part="${dev}"
    fi
    dst="/mnt/$(basename "$part")"
    sudo umount "$dst"
  done
  # detach loop device from img file
  sudo losetup -d "$dev"
fi


# What is intended by the use of the sym links pointing to this scripts?
# ======================================================================
#
# Here explanations by displaying what is done:
# ---------------------------------------------
# 1) mount the file to a loop device
# $ loop_mount_mnt my.img
# /dev/loop0
# /mnt/loop0p1
# /mnt/loop0p2
#
# $ ls /mnt/loop0p1
# /whatever
# /files
# /youhave
# /there
#
# 2) proof of mounting activity by using "sudo losetup -l"
# $ sudo losetup -l
# NAME       SIZELIMIT OFFSET AUTOCLEAR RO BACK-FILE  DIO
# /dev/loop1         0      0         0  0 /full/path/to/my.img
#
# 3) umount the partitions and the img file
# $ # Cleanup.
# $ loop_mount_umnt my.img
# $ ls /mnt/loop0p1
# $ ls /dev | grep loop0
# loop0
#

