#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connects to a MySQL database and retrieves all cities with their respective states.
    """

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

        # Execute SQL query to retrieve all cities with their respective states
        query = """
                SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id
                """
        cursor.execute(query)

        # Fetch all rows and print them
        cities = cursor.fetchall()
        for city in cities:
            print(city)

        # Close cursor and database connection
        cursor.close()
        db.close()
    except Exception as e:
        print("Error:", e)
