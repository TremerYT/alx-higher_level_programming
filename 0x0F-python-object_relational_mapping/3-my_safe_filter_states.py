#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", username=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3], port=3306)
    cursor = database.cursor()
    match = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    database.close()
