'''
Given an array of strings, return another array containing all of its longest strings.
'''


def allLongestStrings(inputArray):
    max_length = len(max(inputArray, key=len))
    longest = []
    for i in range(len(inputArray)):
        string_length = len(inputArray[i])
        if string_length == max_length:
            longest.append(inputArray[i])
    return longest


inputArray = ["enyky", "benyky", "yely", "varennyky"]

print(allLongestStrings(inputArray))
