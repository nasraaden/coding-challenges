'''
Given a string, return its encoding defined as follows:
First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
'''


def lineEncoding(s):
    s = list(s)
    counter = 1
    output = ''
    for i in range(len(s) - 1):
        if s[i] != s[i+1]:
            if counter != 1:
                output += str(counter) + s[i]
            else:
                output += s[i]
            if i == len(s) - 2:
                output += s[i+1]
            counter = 1
        else:
            counter += 1
            if i == len(s) - 2:
                if counter != 1:
                    output += str(counter) + s[i]
                else:
                    output += s[i]
    return output
