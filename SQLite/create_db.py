import sqlite3
from sqlite3 import Error


def create_connection_fs(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)

    return None


def create_connection_mem_only():
    """ create a database connection to a database that resides
        in the memory
    """
    try:
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
        return None


if __name__ == '__main__':
    db_file = "home_automation_231.db"

    # open DB connection
    c = create_connection_fs(db_file)
    c.close()

    # just a test:
    # my_two = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
