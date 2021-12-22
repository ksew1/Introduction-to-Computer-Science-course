class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def f(p):
    min_val = p.val
    if p.next is not None:
        while p.next.next is not None:
            if p.next.val < min_val:
                p.next = p.next.next

            else:
                p = p.next
                min_val = p.val

        if p.next.val < min_val:
            p.next = None


def print_set(p):
    while p is not None:
        print(p.val, "", end="")
        p = p.next
    print()


first = Node(1)
pointer = first
for i in [4,53,6645,4,563,5,34,53,646,99]:
    pointer.next = Node(i)
    pointer = pointer.next
print_set(first)
f(first)
print_set(first)
