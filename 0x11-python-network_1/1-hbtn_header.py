#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
you must use the packages urllib and sys
you must use a with statement
"""
from sys import argv
from urllib import request


if __name__ == "__main__":
    url = argv[1]
    page = request.Request(url)
    with request.urlopen(page) as fetch:
        print(dict(fetch.headers).get("X-Request-Id"))
