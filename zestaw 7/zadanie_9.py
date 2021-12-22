class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def f(p):
    while p.next is not None:
        p = p.next
    p.val = p.val + 1


def print_set(p):
    while p is not None:
        print(p.val, "", end="")
        p = p.next
    print()


first = None
for i in range(1, 3):
    pointer = Node(i)
    pointer.next = first
    first = pointer
print_set(first)
f(first)
print_set(first)
