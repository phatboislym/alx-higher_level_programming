#!/bin/bash
# a Bash script that sends a JSON POST request to a URL passed as the first argument using curl, and displays the body of the response. Your script must send a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
