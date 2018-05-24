#!/bin/bash

#
# source: https://unix.stackexchange.com/questions/316401/how-to-mount-a-disk-image-from-the-command-line/430415#430415
#
# purpose: this script (un)mounts the image and its containing partitions

BNAME=`basename $0 .sh`
DNAME=`dirname $0`


if [ "${BNAME}" == "sudo_loop_mount" ]
then
  cd ${DNAME}

  for TGT in sudo_loop_mount_mnt sudo_loop_mount_umnt
  do
    if [ ! -h ${TGT} ]
    then
      echo "create sym link ${TGT}.sh"
      ln -s ${BNAME}.sh ${TGT}.sh
    fi
  done

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
if [ "${BNAME}" == "sudo_loop_mount_mnt" ]
then
  img=`readlink -f $1`
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
if [ "${BNAME}" == "sudo_loop_mount_umnt" ]
then
  img=`readlink -f $1`

  # define the loop device
  dev="`sudo losetup -l | grep /home/uwe/Downloads/Raspi/2018-99-99-raspbian-stretch-lite.img | cut -f1 -d\" \"`"

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


# Example:
# ========
# $ # mount the file to a loop device
# $ sudo_loop_mount_mnt my.img
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
# $ # proof of mounting activity by using "sudo losetup -l"
# $ sudo losetup -l
# NAME       SIZELIMIT OFFSET AUTOCLEAR RO BACK-FILE  DIO
# /dev/loop1         0      0         0  0 /full/path/to/my.img
#
# $ # umount the partitions and the img file
# $ # Cleanup.
# $ sudo_loop_mount_umntsudo_loop_mount_umnt 0
# $ ls /mnt/loop0p1
# $ ls /dev | grep loop0
# loop0
#

