class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    """def remove_last(self):
        p = self
        if p.next is None:
            return None
        while p.next.next is not None:
            p = p.next
        p.next = None
        return self"""


def remove_last(p):
    p_temp = p
    if p.next is None:
        return None
    while p.next.next is not None:
        p = p.next
    p.next = None
    return p_temp


def print_set(p):
    while p is not None:
        print(p.val, "", end="")
        p = p.next


first = None
for i in range(1):
    s = int(input(">"))
    pointer = Node(s)
    pointer.next = first
    first = pointer
print_set(first)
first = remove_last(first)
print(first)
print()
print_set(first)
