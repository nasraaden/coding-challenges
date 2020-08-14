'''
Given two strings, find the number of common characters between them.
'''


def commonCharacterCount(s1, s2):
    counter = 0
    s1 = list(s1)
    s2 = list(s2)
    for char1 in s1:
        if char1 in s2:
            counter += 1
            s2.remove(char1)
    return counter
