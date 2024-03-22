#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connects to a MySQL database and retrieves all cities of the specified state.
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

        # Execute SQL query to retrieve all cities of the specified state using parameterized query
        query = """
                SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                """
        cursor.execute(query, (state_name,))

        # Fetch the result and print it
        cities = cursor.fetchone()[0]
        if cities:
            print(cities)

        # Close cursor and database connection
        cursor.close()
        db.close()
    except Exception as e:
        print("Error:", e)


