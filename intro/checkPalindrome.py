'''
Given the string, check if it is a palindrome.
'''


def checkPalindrome(inputString):
    s = ''
    reversedString = s.join(reversed(inputString))
    # compare reversed string to input string
    if reversedString == inputString:
        return True
    else:
        return False
