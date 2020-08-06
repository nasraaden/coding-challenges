def equalEdgedStrings(words):
    bool_arr = []
    # two for loops
    # check each string against the next one
    for i in range(len(words) - 1):
        last = len(words[i]) - 1
        print(last)
        for j in range(len(words[i])):
            if words[i][0] == words[i+1][0] and words[i][last] == words[i+1][last]:
                bool_arr.append(True)
            else:
                bool_arr.append(False)
    return bool_arr


# You're trying to solve a puzzle that involves arranging squares of numbers according to their missing values. Each square has dimensions 4 × 4, containing all the numbers between 1 and 16 inclusively, except for one missing number represented by "?". All of these 4 × 4 squares are stored side-by-side within a larger matrix mat with dimensions 4 × (4 * n) (where n represents the number of square matrices).

# Your task is to complete the following steps:

# For each 4 × 4 square, find the value of the missing element and replace the "?" with this value.
# Rearrange the squares inside the larger matrix by these missing values in ascending order. In the case of a tie (if two 4 × 4 matrices have the same missing value), place them in the relative order they were originally presented in the larger matrix mat.
# Return the updated matrix mat as a result.


# You are given a string s. Consider the following algorithm applied to this string:

# Take all the prefixes of the string, and choose the longest palindrome between them.
# If this chosen prefix contains at least two characters, cut this prefix from s and go back to the first step with the updated string. Otherwise, end the algorithm with the current string s as a result.
# Your task is to implement the above algorithm and return its result when applied to string s.

# Note: you can click on the prefixes and palindrome words to see the definition of the terms if you're not familiar with them.


# Given an array of strings words, for each consecutive pair of words check if they start and end with the same character.

# Return a boolean array of length words.length - 1, where ith element is true if words[i] and words[i + 1] start and end with the same character, and false otherwise.


# You are given n, an integer representing the length of a binary string a, which is all '0's in the beginning.

# You are also given operations, an array of strings, each representing an operation of one of these two types:

# "L" - find the smallest index i, for which a[i] = '0', and set a[i] = '1'. If there is no such index, do nothing.
# "C{ind}" - set a[ind] = '0'. This operation does not depend on the previous value of a[ind]. It is guaranteed that ind is a valid 0-based index of a (ie: ind < n).
# Given n and operations, your task is to return a, the binary string after all operations have been applied.
