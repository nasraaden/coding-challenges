'''
Given a string, output its longest prefix which contains only digits.
'''


def longestDigitsPrefix(inputString):
    s = ""
    for i in inputString:
        if i.isnumeric() == True:
            s += i
        else:
            break
    return s
