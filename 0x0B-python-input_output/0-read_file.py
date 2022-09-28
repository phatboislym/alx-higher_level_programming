#!/usr/bin/python3

""" function reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """
    function reads the contents of a file and prints to stdout

    Args:

    filename (str): name of file to be read
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line)

