#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    # Create a cursor object using cursor() method
    cur = conn.cursor()

    # Execute SQL query
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],))

    # Fetch all the rows using fetchall() method
    rows = cur.fetchall()

    # Print rows
    for row in rows:
        print(row)

    # Close cursor
    cur.close()

    # Close connection
    conn.close()
