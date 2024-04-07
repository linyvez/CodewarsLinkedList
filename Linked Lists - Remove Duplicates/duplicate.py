"""Linked Lists - Remove Duplicates"""

class Node(object):
    """Node class"""
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    """Remove duplicates from list of Nodes"""
    if head is None:
        return head

    current = head
    while current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head
