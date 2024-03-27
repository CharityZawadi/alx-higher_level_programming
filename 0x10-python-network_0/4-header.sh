#!/bin/bash
# This script sends a GET request to the URL passed as an argument and displays the body of the response
# It sends a header variable X-School-User-Id with the value 98
curl -sH "X-School-User-Id: 98" -X GET "$1"
