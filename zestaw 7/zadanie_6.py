class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    """
    to jest metoda!!
    def add_to_end(self, n):
        p = self
        if p.val is None:
            p.val = n
            return
        while p.next is not None:
            p = p.next
        p.next = Node(n)"""


def add_to_end(p, n):
    if p.val is None:
        p.val = n
        return
    while p.next is not None:
        p = p.next
    p.next = Node(n)


def print_set(p):
    while p is not None:
        print(p.val, "", end="")
        p = p.next


first = None
for i in range(3):
    s = int(input(">"))
    pointer = Node(s)
    pointer.next = first
    first = pointer

print_set(first)
add_to_end(first, 7)
print()
print_set(first)
print()
print_set(first)
