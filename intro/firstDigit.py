'''
Find the leftmost digit that occurs in a given string.
'''


def firstDigit(inputString):
    for i in inputString:
        if i.isdigit() == True:
            return i
