#!/usr/bin/python3
for letter in range(122, 96, -1):
    if letter % 2 == 0:
        i = 0
    else:
        i = 32
    print("{}".format(chr(letter - i)), end="")
