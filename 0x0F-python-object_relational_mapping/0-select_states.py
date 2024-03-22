#!/usr/bin/python3
"""
Script to connect to the MySQL server.
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
        db = MySQLdb.connect(host="127.0.0.1", port=3306,
                             user=username, passwd=password, db=database)

        print("Connected to MySQL server successfully!")
        
        # Close database connection
        db.close()
    except Exception as e:
        print("Error:", e)

