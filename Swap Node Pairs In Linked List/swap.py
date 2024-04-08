"""Swap Node Pairs In Linked List"""

class Node:
    """Node class"""
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    """Swap pairs of Nodes in the list"""
    if head is None or head.next is None:
        return head
    new_head = head.next
    current = head
    while current is not None and current.next is not None:
        next_pair = current.next.next
        second = current.next
        second.next = current
        current.next = next_pair

        if current.next is not None and current.next.next is not None:
            current.next = current.next.next
        current = next_pair

    return new_head
