#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
The letter must be sent in the variable q, if no argument is given, set q=""
If the response body is properly JSON formatted and not empty, display the id
and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
"""
from sys import argv
from requests import post


if __name__ == "__main__":
    if len(argv) == 1:
        parameter = ""
    else:
        parameter = argv[1]
    test = {"q": parameter}

    request = post("http://0.0.0.0:5000/search_user", data=test)
    try:
        result = request.json()
        if result == {}:
            print("No result")
        else:
            print(f"[{result.get("id")}] {result.get("name")}")
    except ValueError:
        print("Not a valid JSON")
