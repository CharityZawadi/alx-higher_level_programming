#!/bin/bash

# This script sends a request to a URL passed as an argument and displays only the status code of the response

# Send a GET request to the URL passed as an argument and extract the status code from the response headers
curl -sI "$1" | head -n 1 | cut -d' ' -f2
