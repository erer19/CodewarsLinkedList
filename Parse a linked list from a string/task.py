class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == 'None':
        return None
    lst = list_repr.split(' -> ')
    start = Node(int(lst.pop(0)))
    node = start
    for data in lst[:-1]:
        node.next = Node(int(data))
        node = node.next
    return start
