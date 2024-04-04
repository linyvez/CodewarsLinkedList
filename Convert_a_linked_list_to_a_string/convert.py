"""Convert a linked list to a string"""

class Node():
    """Create a node"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    """
    Stringify the node and its next nodes.
    """
    current = node
    output = ''
    while current is not None:
        output += str(current.data) + ' -> '
        current = current.next
    output += str(current)
    return output
