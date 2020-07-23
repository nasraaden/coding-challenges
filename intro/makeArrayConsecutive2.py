'''
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

EXAMPLE
For statues = [6, 2, 3, 8], the output should be
makeArrayConsecutive2(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.
'''


def makeArrayConsecutive2(statues):
    # get min and max of array
    min_num = min(statues)
    max_num = max(statues)
    # get total nums in the range of min and max
    nums_in_range = (max_num + 1) - min_num

    # subtract the len of statues from the total nums in range
    return nums_in_range - len(statues)
