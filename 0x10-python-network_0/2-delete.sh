#!/bin/bash
# a Bash script that sends a DELETE request to the URL passed as the first argument using curl and displays the body of the response
curl -sX DELETE "$1"
