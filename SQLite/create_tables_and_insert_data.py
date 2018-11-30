import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_sensor_type(conn, sensor_type):
    """
    Create a new sensor_type into the sensor_types table
    :param conn:
    :param sensor_type:
    :return:  id
    """
    sql = ''' INSERT INTO sensor_types(name) VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, sensor_type)
    return cur.lastrowid


def create_room(conn, room):
    """
    Create a new room into the rooms table
    :param conn:
    :param room:
    :return:  id
    """
    sql = ''' INSERT INTO rooms(name) VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, room)
    return cur.lastrowid


def create_floor(conn, floor):
    """
    Create a new floor into the floors table
    :param conn:
    :param floor:
    :return:  id
    """
    sql = ''' INSERT INTO floors(name) VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, floor)
    return cur.lastrowid


def create_building(conn, building):
    """
    Create a new building into the buildings table
    :param conn:
    :param building:
    :return:  id
    """
    sql = ''' INSERT INTO buildings(name) VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, building)
    return cur.lastrowid


def create_sensor(conn, sensor):
    """
    Create a new sensor into the sensors table
    :param conn:
    :param sensor:
    :return:  id
    """
    sql = ''' INSERT INTO sensors(sensor_address, building_id, floor_id, room_id, sensor_type_id) VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, sensor)
    return cur.lastrowid


def main():
    db_file = "home_automation_231.db"

    # create a database connection
    conn = create_connection(db_file)
    with conn:
        building = 'house231'
        building_id = create_building(conn, building)

        floor = 'floor_00'
        floor_id = create_floor(conn, floor)

        room = 'Raum vorne'
        room_id = create_room(conn, room)

        sensor_type = 'DS18B20 and alike'
        sensor_type_id = create_sensor_type(conn, sensor_type)

        sensor = ('28:FF:34:43:43:43:43:3A', building_id, floor_id, room_id, sensor_type_id)
        create_sensor(conn, sensor)
        sensor = ('28:FF:45:43:43:43:43:3A', building_id, floor_id, room_id, sensor_type_id)
        create_sensor(conn, sensor)
        # sensor_id = create_sensor(conn, sensor)


if __name__ == '__main__':
    main()
