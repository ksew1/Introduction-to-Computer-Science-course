class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def check(key):
    five = 0
    while key > 0:
        if key % 8 == 5:
            five += 1
        key //= 8
    return five % 2 == 0


def f(pointer):
    p = pointer
    while p.next is not None:
        print(p.next.val)
        if check(p.next.val):
            temp = p.next
            p.next = p.next.next
            temp.next = pointer
            pointer = temp
        else:
            p = p.next
    return pointer


def print_set(p):
    while p is not None:
        print(p.val, "", end="")
        p = p.next
    print()


first = Node(2)
pointer1 = first
for i in [6, 1, 5, 10, 4, 12]:
    pointer1.next = Node(i)
    pointer1 = pointer1.next
print_set(first)
first = f(first)
print_set(first)
