#!/usr/bin/python3


"""This is a first try to read a XML config file and get sensors
 which were added during the program run. In case sensors were 
 added  a new xml file will be written. 
"""

import datetime
import os
import time

import xml.etree.ElementTree as ET

__updated__ = "2015-07-08"


def get_lang():
    """Get the language which should be used if internationalisation is on the menu

    Just do it! 
    """
    return("DE")


def get_sensor_id_for_printing(sid):
    """Get the sensor id for printing out

    Returns either the sensor id or the string 'undefined'
    """
    sid_print = sid
    if (sid_print == ""):
        sid_print = "undefined"
    return(sid_print)


def get_sensor_id(room):
    """Get the sensor id of the room given

    """
    sid = room.get('sensorId')
    return(sid)


def redef_sensor(floor_name, room_name, room, sensors_base_dir, wait_secs_for_new_sensor):
    """Check if there occurs a new sensor in the given sensors directory

    """
    # get the current content of the directory
    devices_cur = os.listdir(sensors_base_dir)
    # TODO: is the following line necessary???
    # devices_cur.remove('w1_bus_master1')

    print("    " + 'Waiting for new sensor')
    time.sleep(wait_secs_for_new_sensor)

    # get the content of the directory after a sensor might have been added

    devices_new = os.listdir(sensors_base_dir)

    # find out what's new out there by removing the old entries
    # and taking the last sid to return it as found
    for dev in devices_cur:
        devices_new.remove(dev)

    sid = SID_NOT_DEFINED
    for dev in devices_new:
        # only the last new device is added
        sid = dev

    if (sid != SID_NOT_DEFINED):
        print("    " + 'new device: ' + sid)

    return(sid)


def get_name_of_backup_sensor_file(sensor_definition_file):
    sensors_definition_backup_filename = \
        sensor_definition_file + \
        '_backup_' + \
        datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S') + \
        '.xml'
    return(sensors_definition_backup_filename)


def get_new_name_of_sensor_file(sensor_definition_file):
    sensors_definition_backup_file = \
        sensor_definition_file + \
        '_new_' + \
        '.xml'
    return(sensors_definition_backup_file)

SENSORS_DEFINITION_FILE = 'w1SensorDefs.xml'
SENSORS_BASE_DIR = './sd'
# '/sys/bus/w1/devices'
SID_NOT_DEFINED = ''

LANG_SHORT = get_lang()

tree = ET.parse(SENSORS_DEFINITION_FILE)
root = tree.getroot()

# amount of time to be
WAIT_SECS_FOR_NEW_SENSOR = 5
changes_made_to_xml = 0
backup_done = 0


for floor in root.findall('floor'):
    # print(floor.attrib)
    floor_name = floor.get('name')
    if (floor_name == "MyFlat"):
        print("Floor name:" + floor_name)
        for room in floor.findall('room'):
            room_name = room.get('roomName' + LANG_SHORT)
            sid = get_sensor_id(room)
            # if the sensor id is not set than
            # we request to add a sensor to the i2c network

            print("  " + floor_name + "/" + room_name)
            # print('    ML sid=#' + sid + '#  if not def:#' + SID_NOT_DEFINED
            # + '#')

            if (sid == SID_NOT_DEFINED):
                print('    getting new sid')
                sid_new = redef_sensor(floor_name,
                                       room_name,
                                       room,
                                       SENSORS_BASE_DIR,
                                       WAIT_SECS_FOR_NEW_SENSOR)
                # if we have a sid which differs from
                # the undefined sid we change the XML
                if (sid_new != sid):
                    # write a backup only if necessary and not done during this
                    # run
                    if (backup_done == 0):
                        backup_done = 1
                        tree.write(get_name_of_backup_sensor_file(SENSORS_DEFINITION_FILE),
                                   'UTF-8',
                                   'version="1.0"')
                    # apply the change to the XML in memory
                    room.set('sensorId', sid_new)
                    sid = sid_new
                    changes_made_to_xml = 1

            sid_print = get_sensor_id_for_printing(sid)
            print("    sid = " + sid_print)

if (changes_made_to_xml == 1):
    print('\nXML file gets written.')
    tree.write(get_new_name_of_sensor_file(
        SENSORS_DEFINITION_FILE), 'UTF-8', 'version="1.0"')

print('\nProgram will exit now.')
