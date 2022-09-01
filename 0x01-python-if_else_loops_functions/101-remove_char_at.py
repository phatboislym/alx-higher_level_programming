#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return (str)
    else:
        new_string = (str[0:n] + str[n+1:])
        return (new_string)
