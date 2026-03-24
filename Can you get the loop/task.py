def loop_size(node):
    turtle = node.next
    rabbit = node.next.next
    while rabbit != turtle:
        turtle = turtle.next
        rabbit = rabbit.next.next
    l = 1
    rabbit = rabbit.next
    while rabbit != turtle:
        rabbit = rabbit.next
        l += 1
    return l
