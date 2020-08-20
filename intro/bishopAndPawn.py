'''
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example below to see how it can move:
'''


def bishopAndPawn(bishop, pawn):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8']

    listBishop = list(bishop)

    listPawn = list(pawn)

    for i in range(len(letters)):
        if listBishop[0] == letters[i]:
            idxBshp = i

        if listPawn[0] == letters[i]:
            idxPawn = i

    dstLtr = abs(idxBshp-idxPawn)

    if (int(listBishop[1]) == (int(listPawn[1]) - dstLtr)) | (int(listBishop[1]) == (int(listPawn[1]) + dstLtr)):
        return True
    else:
        return False
