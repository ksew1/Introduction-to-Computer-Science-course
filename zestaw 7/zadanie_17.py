class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def check(key):
    one = 0
    while key > 0:
        if key % 2 == 1:
            one += 1
        key //= 2
    return one % 2 == 1


def f(pointer):

    while check(pointer.val):
        if pointer.next is not None:
            pointer.next.prev = None
            pointer = pointer.next
        else:
            return None
    p = pointer.next
    while p.next is not None:
        if check(p.val):
            p.prev.next, p.next.prev = p.next, p.prev
        p = p.next
    return pointer


def print_set(p):
    temp = None
    while p is not None:
        temp = p
        print(p.val, "", end="")
        p = p.next
    print()
    p = temp
    while p is not None:
        print(p.val, "", end="")
        p = p.prev
    print()


first = Node(2)
pointer1 = first
for i in [1, 5, 2, 35, 1, 2, 3, 1, 45, 1]:
    pointer1.next = Node(i)
    pointer1.next.prev = pointer1
    pointer1 = pointer1.next

print_set(first)
first = f(first)
print_set(first)