#!/bin/bash
# a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response. You are not allow to use echo, cat, etc. to display the final result
curl -sLX PUT -d "You got me!" 0.0.0.0:5000/catch_me
