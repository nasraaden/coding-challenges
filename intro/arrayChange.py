'''
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.
'''


def arrayChange(inputArray):
    counter = 0
    for i in range(len(inputArray) - 1):
        if inputArray[i] >= inputArray[i+1]:
            add = inputArray[i] - inputArray[i+1] + 1
            counter += add
            inputArray[i+1] += add
    return counter


inputArray = [-1000, 0, -2, 0]

print(arrayChange(inputArray))
