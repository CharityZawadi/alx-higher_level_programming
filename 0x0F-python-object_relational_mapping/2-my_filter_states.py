#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connects to a MySQL database and retrieves states based on user input.
    """

    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Execute SQL query to retrieve states matching the user input
        query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id"
        cursor.execute(query, (state_name,))

        # Fetch all rows and print them
        states = cursor.fetchall()
        for state in states:
            print(state)

        # Close cursor and database connection
        cursor.close()
        db.close()
    except Exception as e:
        print("Error:", e)
