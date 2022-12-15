#!/bin/bash
# a Bash script that takes in a URL, sends a GET request to the URL using curl,
#+ and displays the body of the response of a 200 status code response

curl -sL "$1"
