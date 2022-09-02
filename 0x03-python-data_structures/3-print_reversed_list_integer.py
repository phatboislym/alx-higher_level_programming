#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        return (my_list)
    else:
        reversed_list = list(reversed(my_list))
        for index in range(len(reversed_list)):
            print("{:d}".format(reversed_list[index]))
