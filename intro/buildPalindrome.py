'''
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.
'''


def buildPalindrome(st):
    for i in range(len(st)):
        sub_st = st[i:len(st)]
        if sub_st == sub_st[::-1]:
            non_pal = st[0:i]
            return st + non_pal[::-1]
