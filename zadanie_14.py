class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def f(p):
    val = p.val
    if p.next is not None:
        while p.next.next is not None:
            if p.next.val % val == 0:
                p.next = p.next.next
            else:
                p = p.next
                val = p.val

        if p.next.val % val == 0:
            p.next = None


def print_set(p):
    while p is not None:
        print(p.val, "", end="")
        p = p.next
    print()


first = Node(3)
pointer = first
for i in [2, 4, 2, 6, 2, 5, 10]:
    pointer.next = Node(i)
    pointer = pointer.next
print_set(first)
f(first)
print_set(first)
