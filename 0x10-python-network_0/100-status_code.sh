#!/bin/bash

# This script sends a request to a URL passed as an argument and displays only the status code of the response

# Send a GET request to the URL passed as an argument and save the response headers to a temporary file
curl -sI "$1" > /tmp/response_headers

# Extract and display the status code from the response headers
awk 'NR==1 {print $2}' /tmp/response_headers

# Clean up the temporary file
rm /tmp/response_headers
