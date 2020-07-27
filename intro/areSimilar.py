'''
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.
'''


def areSimilar(a, b):
    counter = 0

    if sorted(a) != sorted(b):
        return False

    for i in range(len(a)):
        if a[i] != b[i]:
            counter += 1

    if counter > 2:
        return False

    return True


a = [1, 2, 3]
b = [2, 1, 3]

print(areSimilar(a, b))
