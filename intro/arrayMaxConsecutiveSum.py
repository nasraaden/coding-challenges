'''
Given array of integers, find the maximal possible sum of some of its k consecutive elements.
'''


def arrayMaxConsecutiveSum(inputArray, k):
    k_sum = sum(inputArray[0:k])
    max_sum = k_sum

    for i in range(k, len(inputArray)):
        k_sum = k_sum - inputArray[i-k] + inputArray[i]
        if k_sum > max_sum:
            max_sum = k_sum

    return max_sum
