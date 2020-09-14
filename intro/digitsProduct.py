'''
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.
'''


def digitsProduct(product):
    if product == 0:
        return 10
    for i in range(3600):
        a = 1
        for j in str(i):
            a *= int(j)
        if a == product:
            return i
    return -1
