'''
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.
'''


def avoidObstacles(inputArray):
    inputArray = sorted(inputArray)
    distance = 1
    hit = True
    while hit:
        hit = False
        distance += 1
        for i in range(len(inputArray)):
            if inputArray[i] % distance == 0:
                hit = True
    return distance


inputArray = [5, 3, 6, 7, 9]
print(avoidObstacles(inputArray))
