class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return None
    node = head.next
    prev = head
    while node is not None:
        if node.data == prev.data:
            prev.next = node.next
            node = node.next
        else:
            node, prev = node.next, prev.next
    return head
