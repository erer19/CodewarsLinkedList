class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if not isinstance(node, Node):
        raise ValueError
    if not isinstance(index, int) or index < 0:
        raise IndexError
    for _ in range(index):
        try:
            node = node.next
        except AttributeError:
            raise ValueError
        if not isinstance(node, Node):
            raise ValueError
    return node
