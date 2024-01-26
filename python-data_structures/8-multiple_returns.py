#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        new_tople = (0, None)
    else:
        new_tople = (len(sentence), sentence[0])
    return (new_tople)
