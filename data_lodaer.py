__author__ = 'Charlie'
# This loads the flat file into the database for use by the API
# It will wipe the database if any data exists

import os
import sqlite3
import csv

from config import DATABASE_NAME, DATA_FILE_NAME
from sql_statements import CREATE_PRICES_TABLE, INSERT_PRICES_TABLE
from db_tools import std_connection



def create_prices_table(con):
    """creates the table route_prices on the database (con)"""
    cur = con.cursor()
    cur.execute(CREATE_PRICES_TABLE)
    con.commit()



def insert_price_data(con, data):
    """inserts the data into the connection"""
    cursor = con.cursor()
    SQL = INSERT_PRICES_TABLE

    for d in data:
        cursor.execute(SQL, d)
        print "Inserted", d

    con.commit()



def read_data_file(data_file_name):
    """parses the csv file {data_file_name} and returns
       a list of dictionaries"""
    with open(data_file_name, "r") as f:
        return [row for row in csv.DictReader(f)]



if __name__ == "__main__":
    # drop the database
    os.remove(DATABASE_NAME)

    # Get a connection to the database (making a new one in the process)
    conn = std_connection()

    # Create the table
    create_prices_table(conn)

    # Load the table from the file.
    data = read_data_file(DATA_FILE_NAME)

    # Insert it
    insert_price_data(conn, data)

