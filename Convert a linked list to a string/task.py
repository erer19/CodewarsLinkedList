def stringify(node):
    if node is None:
        return 'None'
    out = str(node.data)
    while node.next is not None:
        node = node.next
        out += ' -> ' + str(node.data)
    return out + ' -> None'
