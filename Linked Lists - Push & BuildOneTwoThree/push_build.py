"""Linked Lists - Push & BuildOneTwoThree"""

class Node:
    """Node class"""
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    """Push the node"""
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    """Build Node(1, Node(2, Node(3))) without next node"""
    node = push(None, 3)
    node = push(node, 2)
    node = push(node, 1)
    return node