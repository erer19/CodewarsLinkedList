class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    node = head
    if head is None:
        return Node(data)
    if node.data > data:
        head = Node(data)
        head.next = node
    else:
        while node.data < data:
            prev = node
            node = node.next
            if node is None:
                break
        prev.next = Node(data)
        prev.next.next = node
    return head
