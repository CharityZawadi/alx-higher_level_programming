#!/bin/bash

# This script sends a JSON POST request to a URL passed as the first argument,
# with the contents of a file passed as the second argument,
# and displays the body of the response

# Check if the file exists
if [ ! -f "$2" ]; then
    echo "File not found: $2"
    exit 1
fi

# Validate if the file contains valid JSON
if ! jq . "$2" >/dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

# Send a POST request with the contents of the file in the body and display the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
