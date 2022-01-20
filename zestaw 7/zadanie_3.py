class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def f(p1, p2):
    core = Node(None)
    p = core
    while p2 is not None and p1 is not None:
        if p2.val > p1.val:
            p.next = p1
            p1 = p1.next
            p = p.next
        else:
            p.next = p2
            p2 = p2.next
            p = p.next
    if p2 is None:
        p.next = p1
    else:
        p.next = p2

    return core.next


def rek_f(p1, p2):
    if p1 is None:
        return p2
    if p2 is None:
        return p1
    if p2.val > p1.val:
        p = p1
        p.next = rek_f(p1.next, p2)
    else:
        p = p2
        p.next = rek_f(p1, p2.next)
    return p


def print_set(p):
    while p is not None:
        print(p.val, "", end="")
        p = p.next
    print()


first = Node(1)
pointer1 = first
for i in [1, 4, 7, 9, 10, 13, 15]:
    pointer1.next = Node(i)
    pointer1 = pointer1.next


first2 = Node(1)
pointer2 = first2
for i in [1, 2, 3, 4, 5, 6, 10]:
    pointer2.next = Node(i)
    pointer2 = pointer2.next
print_set(first)
print()
print_set(first2)
print_set(f(first, first2))
print_set(rek_f(first, first2))