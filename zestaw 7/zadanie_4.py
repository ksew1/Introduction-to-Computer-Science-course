class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse(p):
    if p.next is None:
        return p
    q = p.next
    p.next = None
    while q is not None:
        temp = q.next
        q.next = p
        p = q
        q = temp

    return p


def print_set(p):
    while p is not None:
        print(p.val, "", end="")
        p = p.next
    print()


first = Node(1)
pointer = first
for i in [2,3,4,5,6,7,8,9]:
    pointer.next = Node(i)
    pointer = pointer.next
print_set(first)
first = reverse(first)
print_set(first)

