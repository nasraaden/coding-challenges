'''
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).
'''


def alphabeticShift(inputString):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    inputString = list(inputString)
    for i in range(len(inputString)):
        if inputString[i] == 'z':
            inputString[i] = 'a'
        else:
            index = letters.index(inputString[i])
            inputString[i] = letters[index + 1]
    return "".join(inputString)
