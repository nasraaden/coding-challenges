'''
Elections are in progress!

Given an array of the numbers of votes given to each of the candidates so far, and an integer k equal to the number of voters who haven't cast their vote yet, find the number of candidates who still have a chance to win the election.

The winner of the election must secure strictly more votes than any other candidate. If two or more candidates receive the same (maximum) number of votes, assume there is no winner at all.
'''


def electionsWinners(votes, k):
    counter = 0
    max_votes = max(votes)

    if k == 0:
        if votes.count(max(votes)) == 1:
            return 1
        else:
            return 0

    for i in range(len(votes)):
        if votes[i] + k > max_votes:
            counter += 1

    return counter
