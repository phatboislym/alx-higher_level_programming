#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
        reversed_list = list(reversed(my_list))
        for index in range(len(reversed_list)):
            print("{:d}".format(reversed_list[index]))
