'''
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!
'''


def sortByHeight(a):
    b = []
    c = []
    for i in range(len(a)):
        if a[i] != -1:
            b.append(a[i])
        else:
            c.append(i)
    b.sort()
    for i in c:
        b.insert(i, -1)
    return b


a = [-1, 150, 190, 170, -1, -1, 160, 180]

print(sortByHeight(a))
