"""Linked Lists - Recursive Reverse"""

class Node(object):
    """Node class"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    """Reverse the given list of Nodes"""
    if head is None or head.next is None:
        return head

    reversed_ = reverse(head.next)
    head.next.next = head
    head.next = None

    return reversed_
