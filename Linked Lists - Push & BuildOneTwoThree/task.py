class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    node = push(None, 3)
    node = push(node, 2)
    node = push(node, 1)
    return node
