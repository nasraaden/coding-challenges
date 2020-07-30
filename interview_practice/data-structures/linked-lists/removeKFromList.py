'''
Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.
'''

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None


def removeKFromList(l, k):
    # STEPS
    # 1. Loop through the linked list.
    # 2. Find k and remove it
    # 3. Keep going until there is no more number that equals k

    # if there is nothing in the linked list

    curr = l
    while curr is not None:
        if curr.value != k:
            break
        curr = curr.next
    # first move and set the head
    new_head = curr
    prev = None
    # move along
    while curr is not None:
        if curr.value == k:
            if prev is not None:
                prev.next = curr.next
            curr = curr.next
            continue
        prev = curr
        curr = curr.next
    return new_head


l = [3, 1, 2, 3, 4, 5]
k = 3

print(removeKFromList(l, k))
