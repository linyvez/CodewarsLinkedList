"""Linked Lists - Get Nth Node"""

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    """
    Get nth node by index.
    """
    current = node
    lst = []
    while current is not None:
        lst.append(current)
        current = current.next
    if (len(lst) > 0 and 0 <= index <= len(lst) - 1):
        return lst[index]
    raise Exception
