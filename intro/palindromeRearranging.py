'''
Given a string, find out if its characters can be rearranged to form a palindrome.
'''


def palindromeRearranging(inputString):
    counter = 0
    for char in inputString:
        if len(inputString) % 2 == 0:
            if inputString.count(char) % 2 != 0:
                return False
        else:
            if inputString.count(char) == 1:
                counter += 1
    if counter > 1:
        return False
    return True


inputString = 'aabb'

print(palindromeRearranging(inputString))
