#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_aray = set()
    for word1 in set_1:
        for word2 in set_2:
            if (word1 == word2):
                new_aray.add(word1)
    return (new_aray)
