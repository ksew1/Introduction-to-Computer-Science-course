class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove(key):
    one = 0
    two = 0
    while key > 0:
        if key % 3 == 1:
            one += 1
        elif key % 3 == 2:
            two += 1
        key //= 3
    return one > two


def f(pointer):
    p = pointer
    if remove(p.val):
        pointer = pointer.next
        p = p.next
    while p.next is not None:
        if remove(p.next.val):
            p.next = p.next.next
        else:
            p = p.next
    return pointer


def print_set(p):
    while p is not None:
        print(p.val, "", end="")
        p = p.next
    print()


first = Node(3)
pointer1 = first
for i in [2, 4, 2, 6, 2, 5, 10]:
    pointer1.next = Node(i)
    pointer1 = pointer1.next
print_set(first)
first = f(first)
print_set(first)
