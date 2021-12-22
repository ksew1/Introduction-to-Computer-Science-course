class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def f(p):
    while p.next is not None:
        p.next = p.next.next
        if p.next is not None:
            p = p.next


def print_set(p):
    while p is not None:
        print(p.val, "", end="")
        p = p.next


first = None
for i in range(5):
    s = int(input(">"))
    pointer = Node(s)
    pointer.next = first
    first = pointer


print_set(first)
f(first)
print()
print_set(first)
