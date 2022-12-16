#!/bin/bash
# a Bash script that sends a request to a URL using curl passed as an argument, and displays only the status code of the response. You are not allowed to use any pipe, redirection, ;, &&, etc.
curl -s -o /dev/null -w "%{http_code}" "$1"
