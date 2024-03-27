#!/bin/bash
# This script sends a POST request to the URL passed as an argument and displays the body of the response
# It sends variables email and subject with specified values
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
