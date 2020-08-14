'''
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.
'''


def arrayMaximalAdjacentDifference(inputArray):
    difference = []
    for i in range(len(inputArray) - 1):
        difference.append(abs(inputArray[i] - inputArray[i+1]))
    return max(difference)
