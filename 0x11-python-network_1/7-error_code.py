#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and displays
the body of the response. If the HTTP status code is greater than or equal to
400, print: Error code: followed by the value of the HTTP status code
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""
from sys import argv
from requests import get


if __name__ == "__main__":
    page = argv[1]

    content = get(page)
    if content.status_code >= 400:
        print("Error code: {}".format(content.status_code))
    else:
        print(content.text)
