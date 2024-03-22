#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Execute SQL query to retrieve all states
        cursor.execute("SELECT * FROM states ORDER BY id")

        # Fetch all rows and print them in the specified format
        states = cursor.fetchall()
        for state in states:
            print(state)

        # Close cursor and database connection
        cursor.close()
        db.close()
    except Exception as e:
        print("Error:", e)
