#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
The email must be sent in the email variable
You must use the packages urllib and sys
You must use the with statement
"""
from sys import argv
from urllib import parse
from urllib import request


if __name__ == "__main__":
    page = argv[1]
    email = {"email": argv[2]}
    data = parse.urlencode(email).encode("ascii")

    content = request.Request(page, data)
    with request.urlopen(content) as fetch:
        print(fetch.read().decode("utf-8"))
