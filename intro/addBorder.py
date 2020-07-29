'''
Given a rectangular matrix of characters, add a border of asterisks(*) to it.
'''


def addBorder(picture):
    new_picture = []
    picture.append('*' * (len(picture[0])))
    picture.insert(0, '*' * (len(picture[0])))
    for i in range(len(picture)):
        string = list(picture[i])
        string.append('*')
        string.insert(0, '*')
        string = ''.join(string)
        new_picture.append(string)
    return new_picture


picture = ["abc", "ded"]

print(addBorder(picture))
