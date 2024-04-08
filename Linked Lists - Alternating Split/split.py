"""Linked Lists - Alternating Split"""

class Node(object):
    """Node class"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    """Context class"""
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """Split one list of Nodes into two smaller ones"""
    if head is None or head.next is None:
        raise Exception
    first_node = head
    second_node = head.next

    first_current = first_node
    second_current = second_node

    while first_current.next and second_current.next:
        first_current.next = second_current.next
        first_current = first_current.next

        second_current.next = first_current.next
        second_current = second_current.next
    try:
        first_current.next = None
        second_current.next = None
    except Exception:
        pass

    return Context(first_node, second_node)
