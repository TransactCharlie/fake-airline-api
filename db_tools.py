__author__ = 'Charlie'

import sqlite3
from config import DATABASE_NAME

def dict_factory(cursor, row):
    """returns a dictionary representation of a row object"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d



def dict_connection(database_name):
    """returns a connection for {database_name} with a dict row factory"""
    conn = sqlite3.connect(database_name)
    conn.row_factory = dict_factory
    return conn



def std_connection():
    """returns the default connection to {DATABASE_NAME}"""
    return dict_connection(DATABASE_NAME)