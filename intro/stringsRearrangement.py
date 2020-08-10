'''
Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements in such a way that each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.

Note: You're only rearranging the order of the strings, not the order of the letters within the strings!
'''
from itertools import permutations


def stringsRearrangement(inputArray):
    allPermutations = permutations(inputArray)
    for permu in allPermutations:
        match = True
        for i in range(len(permu) - 1):
            if differByOneChar(permu[i], permu[i + 1]) == False:
                match = False
                break
        if match == True:
            return True
    return False


def differByOneChar(str1, str2):
    differ_count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            differ_count += 1
    if differ_count != 1:
        return False
    return True


inputArray = ["aba", "bbb", "bab"]

print(stringsRearrangement(inputArray))
