"""Linked Lists - Sorted Insert"""
class Node(object):
    """Node class"""
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    """Sort the list of Nodes and add a new one"""
    new_node = Node(data)
    if head is None or head.data >= data:
        new_node.next = head
        return new_node
    current = head
    while current.next is not None and current.next.data < data:
        current = current.next
    new_node.next = current.next
    current.next = new_node

    return head
