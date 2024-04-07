"""Move Node"""

class Node(object):
    """Node class"""
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    """Context class"""
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """Move the node and return """
    if not source:
        raise Exception
    new_source = source.data
    next = source.next
    new_dest = Node(new_source)
    new_dest.next = dest
    return Context(next, new_dest)
