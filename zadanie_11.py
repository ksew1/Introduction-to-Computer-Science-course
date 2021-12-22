class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def f(p, key):
    if p.val == key:
        global first
        first = first.next
        return
    temp = p
    while p.next is not None and p.next.val != key:
        p = p.next
    if p.next is None:
        p.next = Node(key)
    else:
        p.next = p.next.next


def print_set(p):
    while p is not None:
        print(p.val, "", end="")
        p = p.next
    print()


first = Node(1)
pointer = first
for i in range(2, 6):
    pointer.next = Node(i)
    pointer = pointer.next
print_set(first)
f(first, 7)
print_set(first)
