#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and displays
    the value of the variable X-Request-Id in the response header
"""

from sys import argv
from requests import get


if __name__ == "__main__":
    page = argv[1]

    content = get(page)
    print(content.headers.get("X-Request-Id"))
