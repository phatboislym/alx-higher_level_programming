#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    a_list = list(a_dictionary.items())
    max_value = a_list[0][1]
    max_key = a_list[0][0]
    for i in range(len(a_list)):
        if a_list[i][-1] > max_value:
            max_value = a_list[i][1]
            max_key = a_list[i][0]
    return (max_key)
