#!/usr/bin/python3
"""
a Pyhton script that sends a POST request to a given URL with a given
    email
"""
from sys import argv
from requests import get
from requests import post

if __name__ == "__main__":
    page = argv[1]
    value = {"email": argv[2]}

    content = post(page, data=value)
    print(content.text)
