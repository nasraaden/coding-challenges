'''You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).'''


def rotateImage(a):
    N = len(a)

    # STEP 1: SWITCH DIAGONALLY
    for i in range(0, N):
        for j in range(i, N):
            temp = a[i][j]
            a[i][j] = a[j][i]
            a[j][i] = temp

    # STEP 2: FLIP HORIZONTALLY
    for i in range(0, N):
        for j in range(0, N//2):
            temp = a[i][j]
            a[i][j] = a[i][N - 1 - j]
            a[i][N - 1 - j] = temp

    return a


a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(rotateImage(a))
