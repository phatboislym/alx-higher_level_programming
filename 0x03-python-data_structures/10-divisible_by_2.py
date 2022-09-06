#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    mod_2 = []
    for i in range(length):
        if my_list[i] % 2:
            mod_2.append(False)
        else:
            mod_2.append(True)
    return (mod_2)
