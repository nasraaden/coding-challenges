'''
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
'''


def adjacentElementsProduct(inputArray):
    # USING A DICTIONARY
    # my_dict = {}
    # loop through array, multiply adjacent numbers and store the products in       a dictionary, then return max of that dictionary
    # for i in range(len(inputArray) - 1):
    #     my_dict[inputArray[i] * inputArray[i+1]] = 0
    # return max(my_dict)

    # WITHOUT A DICTIONARY
    max_num = -1000
    for i in range(len(inputArray) - 1):
        product = inputArray[i] * inputArray[i+1]
        if product > max_num:
            max_num = product
            print(max_num)
    return max_num
