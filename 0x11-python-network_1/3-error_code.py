#!/usr/bin/python3
""" Sends a request to a given URL and displays the response body """
from sys import argv
from urllib import error
from urllib import request


if __name__ == "__main__":
    page = argv[1]

    content = request.Request(page)
    try:
        with request.urlopen(content) as fetch:
            print(fetch.read().decode("ascii"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
