"""Parse a linked list from a string"""

class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    # if s == 'None':
    #     return None
    nodes = s.split(' -> ')
    
    head = Node(nodes[0])
    current = head
    
    for node in nodes[1:]:
        current.next = Node(node)
        current = current.next
    
    return head

print(linked_list_from_string("1 -> 2 -> 3 -> None"))
