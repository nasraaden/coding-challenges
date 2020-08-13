'''
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.
'''


def minesweeper(matrix):
    output_arr = []
    for i in range(len(matrix)):
        output_arr.append([])
        for j in range(len(matrix[0])):
            l = -matrix[i][j]
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if 0 <= i+x < len(matrix) and 0 <= j+y < len(matrix[0]):
                        l += matrix[i+x][j+y]
            output_arr[i].append(l)
    return output_arr
