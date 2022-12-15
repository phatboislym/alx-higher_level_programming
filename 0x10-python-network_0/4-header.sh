#!/bin/bash
# a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. A header variable X-School-User-Id must be sent with the value 98 Send a GET request to a given URL with a header variable.
curl -sH "X-School-User-Id: 98" "$1"
