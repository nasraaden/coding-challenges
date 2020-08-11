'''
Given a sorted array of integers a, your task is to determine which element of a is closest to all other values of a. In other words, find the element x in a, which minimizes the following sum:

abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
(where abs denotes the absolute value)

If there are several possible answers, output the smallest one.
'''


def absoluteValuesSumMinimization(a):
    sums = []
    for i in range(len(a)):
        sum = 0
        for j in range(len(a)):
            sum += abs(a[i]-a[j])
        sums.append(sum)
    min_index = sums.index(min(sums))
    return a[min_index]


a = [2, 4, 7]

print(absoluteValuesSumMinimization(a))
