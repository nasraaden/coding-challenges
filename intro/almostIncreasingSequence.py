'''
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

EXAMPLE
For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.
'''


def almostIncreasingSequence(sequence):
    deleted = 0
    for i in range(len(sequence)-1):
        if sequence[i] <= sequence[i-1]:
            deleted += 1
            if sequence[i] <= sequence[i-2] and sequence[i+1] <= sequence[i-1]:
                return False

    if deleted > 1:
        return False

    return True


sequence = [10, 1, 2, 3, 4, 5]

print(almostIncreasingSequence(sequence))
