#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for val in a_dictionary:
        new_dic[val] = a_dictionary[val] * 2
    return (new_dic)
