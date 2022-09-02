#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return ("None")
    else:
        x = my_list[idx:idx+1]
        for i in x:
            return (i)
