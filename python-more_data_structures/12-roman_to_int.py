#!/usr/bin/python3
def roman_to_int(roman_string):
    count = 0
    temp = 0
    leng = len(roman_string)
    dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    for letter in range(leng):
        if letter < leng - 1:
            if dic[roman_string[letter]] < dic[roman_string[letter + 1]]:
                temp = dic[roman_string[letter]]
                pass
        count += dic[roman_string[letter]] - temp
    return (count)
