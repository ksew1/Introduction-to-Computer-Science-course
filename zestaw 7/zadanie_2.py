class Node:
    def __init__(self, val, i=0):
        self.val = val
        self.next = None
        self.id = i


def make_set(val):
    s = Node(val)
    return s


def find_id(p, i):
    if i == 0:
        return p.val
    while p.next is not None and p.next.id < i:
        p = p.next
    if p.next is not None and p.next.id == i:
        return p.next.val


def change_val(p, val, i):
    if i == 0:
        p.val = val
        return
    while p.next is not None and p.next.id < i:
        p = p.next
    if p.next is not None and p.next.id == i:
        p.next.val = val
        return
    temp = Node(val, i)
    if p.next is None:
        p.next = temp
    else:
        temp.next = p.next
        p.next = temp


def print_set(p):
    while p is not None:
        print(p.val, "", end="")
        p = p.next
    print()


first = Node(1, 0)
pointer = first
for j in range(2, 6):
    pointer.next = Node(j, j - 1)
    pointer = pointer.next
print_set(first)
print(find_id(first, 1))
change_val(first, 10, 1)
print_set(first)
