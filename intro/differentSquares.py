'''
Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.
'''


def differentSquares(matrix):
    nums_set = set()
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])-1):
            nums_set.add((matrix[i][j], matrix[i+1][j],
                          matrix[i][j+1], matrix[i+1][j+1]))
    print(nums_set)
    return len(nums_set)
