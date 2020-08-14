'''
Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.
'''


def digitDegree(n):
    counter = 0
    while True:
        if n >= 10:
            n = sum([int(i) for i in str(n)])
            counter += 1
        else:
            return counter
