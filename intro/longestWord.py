'''
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.
'''


def longestWord(text):
    l = list()
    print(ord("a"), ord("z"), ord("A"), ord("Z"))

    s = ""
    for i in range(len(text)):
        if 97 <= ord(text[i]) and ord(text[i]) <= 122 or 65 <= ord(text[i]) and ord(text[i]) <= 90:
            s += text[i]
        else:
            l.append(s)
            s = ""
    l.append(s)
    return max(l, key=len)
