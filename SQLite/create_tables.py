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


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    db_file = "home_automation_231.db"

    sql_create_buildings_table = """ 
                                    CREATE TABLE IF NOT EXISTS buildings (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL
                                    ); """

    sql_create_floors_table = """ 
                                    CREATE TABLE IF NOT EXISTS floors (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL
                                    ); """

    sql_create_rooms_table = """
                                    CREATE TABLE IF NOT EXISTS rooms (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL
                                    ); """

    sql_create_sensor_types_table = """
                                    CREATE TABLE IF NOT EXISTS sensor_types (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL
                                    ); """

    sql_create_sensors_table = """
                                    CREATE TABLE IF NOT EXISTS sensors (
                                        id integer PRIMARY KEY,
                                        sensor_address text NOT NULL,
                                        building_id integer NOT NULL,
                                        floor_id integer NOT NULL,
                                        room_id integer NOT NULL,
                                        sensor_type_id integer NOT NULL,
                                        FOREIGN KEY (building_id) REFERENCES buildings (id),
                                        FOREIGN KEY (floor_id) REFERENCES floors (id),
                                        FOREIGN KEY (room_id) REFERENCES rooms (id),
                                        FOREIGN KEY (sensor_type_id) REFERENCES sensor_types (id)
                                    );"""

    # create a database connection
    conn = create_connection(db_file)
    if conn is not None:
        create_table(conn, sql_create_buildings_table)
        create_table(conn, sql_create_floors_table)
        create_table(conn, sql_create_rooms_table)
        create_table(conn, sql_create_sensor_types_table)
        create_table(conn, sql_create_sensors_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
