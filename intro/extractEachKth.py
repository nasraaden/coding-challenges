'''
Given array of integers, remove each kth element from it.
'''


def extractEachKth(inputArray, k):
    del inputArray[k-1::k]
    return inputArray
