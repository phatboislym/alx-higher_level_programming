#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or roman_string is None):
        return (0)

    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    arabic_number = 0
    length = len(roman_string)
    for i in range(length):
        if roman_numerals.get(roman_string[i], 0) == 0:
            return (0)

        if (i != (length - 1) and roman_numerals[roman_string[i]] < roman_numerals[roman_string[i + 1]]):
                arabic_number += roman_numerals[roman_string[i]] * -1

        else:
            arabic_number = arabic_number + roman_numerals[roman_string[i]]
    return (arabic_number)
