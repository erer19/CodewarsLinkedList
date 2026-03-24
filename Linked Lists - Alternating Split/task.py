class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError
    first_head, second_head = None, None
    first_turn = True
    first, second = None, None
    while True:
        if first_turn:
            if first is None:
                first = Node(head.data)
                first_head = first
            else:
                first.next = Node(head.data)
                first = first.next
        else:
            if second is None:
                second = Node(head.data)
                second_head = second
            else:
                second.next = Node(head.data)
                second = second.next
        head = head.next
        if head is None:
            break
        first_turn = not first_turn
    return Context(first_head, second_head)
