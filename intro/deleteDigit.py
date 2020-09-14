'''
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.
'''


def deleteDigit(n):
    n = list(str(n))
    max_arr = []
    for i in range(len(n)):
        copy_arr = n.copy()
        copy_arr.pop(i)
        max_arr.append(int(''.join(copy_arr)))
    return max(max_arr)
