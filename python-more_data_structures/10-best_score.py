#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    score = ''
    max_score = 0
    for value in a_dictionary:
        if a_dictionary[value] > max_score:
            max_score = a_dictionary[value]
            score = value
    return (score)
