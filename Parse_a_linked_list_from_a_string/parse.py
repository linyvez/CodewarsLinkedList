"""Parse a linked list from a string"""

class Node:
    """Node class"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    """Return the list of Nodes from string"""
    if s == 'None':
        return None
    nodes = s.split(' -> ')
    nodes = nodes[:-1]

    head = Node(int(nodes[0]))
    current = head

    for node in nodes[1:]:
        current.next = Node(int(node))
        current = current.next

    return head
