#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", username=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3], port=3306)
    cursor = database.cursor()
    cursor.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = cursor.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cursor.close()
    database.close()
