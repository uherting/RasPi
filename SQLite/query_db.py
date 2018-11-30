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


def get_sensor(conn, sensor_address):
    """
    :param conn:
    :param sensor_address:
    :return: rows
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM sensors WHERE sensor_address=?", (sensor_address,))

    rows = cur.fetchall()

    return rows


def main():
    db_file = "home_automation_231.db"

    # create a database connection
    conn = create_connection(db_file)
    with conn:
        rows = get_sensor(conn, '28:FF:FF:12')
        for row in rows:
            print(row)


if __name__ == '__main__':
    main()
