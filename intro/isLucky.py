'''
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.
'''


def isLucky(n):
    n = str(n)
    first_sum = 0
    second_sum = 0
    left = n[:len(n)//2]
    right = n[len(n)//2:]

    for i in left:
        first_sum += int(i)

    for j in right:
        second_sum += int(j)

    if first_sum == second_sum:
        return True

    return False
