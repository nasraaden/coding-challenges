'''Given a singly linked list of integers, determine whether or not it's a palindrome.'''

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
from collections import deque


def isListPalindrome(l):
    stack = deque()
    node = l
    while node:
        stack.append(node.value)
        node = node.next

    node = l

    while node:
        # pop off the stack
        top = stack.pop()
        if top != node.value:
            return False
        node = node.next
    return True


l = [0, 1, 0]

print(isListPalindrome(l))
