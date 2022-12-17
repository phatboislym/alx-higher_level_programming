#!/usr/bin/python3
""" a Python script that fetches https://intranet.hbtn.io/status """
from requests import get


if __name__ == "__main__":
    content = get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(content.text)))
    print("\t- content: {}".format(content.text))
