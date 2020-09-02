'''
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.
'''


def chessKnight(cell):
    move = 0
    cell = [ord(cell[0]), int(cell[1])]
    moves = [[1, 2], [2, 1], [-1, -2], [-2, -1],
             [-1, 2], [-2, 1], [1, -2], [2, -1]]
    for m in moves:
        if onboard(cell[0]+m[0], cell[1]+m[1]):
            move += 1
    return move


def onboard(a, n):
    if ord("a") <= a <= ord("h") and 1 <= n <= 8:
        return True
    return False
