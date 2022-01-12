class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def f(pointer):
    p = pointer
    while p is not None:
        q = p
        while q.next is not None and q.next.val == p.val:
            q.next = q.next.next
        p = p.next


def print_set(p):
    while p is not None:
        print(p.val, "", end="")
        p = p.next
    print()


first = Node(1)
pointer1 = first
for i in [1, 1, 1, 1, 3, 5, 6, 7, 8, 88, 88, 88, 222]:
    pointer1.next = Node(i)
    pointer1 = pointer1.next
print_set(first)
f(first)
print_set(first)
