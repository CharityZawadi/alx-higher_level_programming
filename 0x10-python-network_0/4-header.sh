#!/bin/bash
# This script sends a GET request to the URL passed as an argument, including a header variable X-School-User-Id with the value 98, and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
