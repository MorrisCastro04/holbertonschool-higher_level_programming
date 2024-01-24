#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        letter = ord(str[i])
        if letter >= 97 and letter <= 122:
            letter = chr(letter - 32)
        else:
            letter = chr(letter)
        print("{}".format(letter), end='')
    print('')
