'''
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.
'''


def firstNotRepeatingCharacter(string):
    str_arr = []
    my_dict = {}
    for s in string:
        if s in my_dict:
            my_dict[s] += 1
        else:
            my_dict[s] = 1
            str_arr.append(s)
    for s in str_arr:
        if my_dict[s] == 1:
            return s
    return '_'


string = 'abacabad'

print(firstNotRepeatingCharacter(string))
