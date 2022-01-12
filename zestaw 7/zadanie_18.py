class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def f(pointer):
    p = pointer
    while p is not None:
        q = p
        while q.next is not None:
            if p.val == q.next.val:
                q.next = q.next.next
            else:
                q = q.next
        p = p.next


def print_set(p):
    while p is not None:
        print(p.val, "", end="")
        p = p.next
    print()


first = Node(3)
pointer1 = first
for i in [2, 4, 2, 6, 2, 5, 5, 10]:
    pointer1.next = Node(i)
    pointer1 = pointer1.next
print_set(first)
f(first)
print_set(first)