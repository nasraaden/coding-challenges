'''
A string is said to be beautiful if each letter in the string appears at most as many times as the previous letter in the alphabet within the string; ie: b occurs no more times than a; c occurs no more times than b; etc.

Given a string, check whether it is beautiful.
'''


def isBeautifulString(inputString):
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in range(1, len(letters)):
        if inputString.count(letters[i-1]) >= inputString.count(letters[i]):
            continue
        return False
    return True
