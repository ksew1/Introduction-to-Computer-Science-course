def remove(key):
    one = 0
    two = 0
    while key > 0:
        if key % 3 == 1:
            one += 1
        elif key % 3 == 2:
            two += 1
        key //= 3
    return one > two


def f(p):
    if remove(p.val):
        global first
        first = first.next
        p = p.next
    if p.next is not None:
        while p.next.next != None:
            if remove(p.next.val):
                p.next = p.next.next
            else:
                p = p.next
        if remove(p.next.val):
            p.next = p.next.next
