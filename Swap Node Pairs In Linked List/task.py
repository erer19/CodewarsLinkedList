class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_pairs(head):
    if head is None:
        return None
    if head.next is None:
        return head
    node = head.next
    prev = head
    head = node
    very_prev = None
    while True:
        prev.next = node.next
        node.next = prev
        if very_prev is not None:
            very_prev.next = node
        very_prev = prev
        try:
            prev, node = prev.next, prev.next.next
        except AttributeError:
            break
        if prev is None or node is None:
            break
    return head
