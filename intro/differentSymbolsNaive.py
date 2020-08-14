'''
Given a string, find the number of different characters in it.
'''

from collections import Counter


def differentSymbolsNaive(s):
    s_counter = Counter(s)
    return len(s_counter)
