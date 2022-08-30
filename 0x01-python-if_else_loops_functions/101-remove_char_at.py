#!/usr/bin/python3

def remove_char_at(str, n):
    index = 0
    new_string = ""
    for letter in str:
        if index != n:
            new_string += letter
            index += 1
    return (new_string)
