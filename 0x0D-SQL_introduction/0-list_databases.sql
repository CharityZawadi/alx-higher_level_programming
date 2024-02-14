# ----------------------------------
# File: 0-list_databases.sql
# Description: Lists all databases of your MySQL server
# Author: Guillaume
# Date: Current date
# ----------------------------------

# List all databases
SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA;

