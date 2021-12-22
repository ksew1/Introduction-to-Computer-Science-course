class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def f(p1, p2):

    p3 = Node(p1.val + p2.val)
    temp3 = p3
    temp1 = p1.next
    temp2 = p2.next
    while temp1 is not None or temp2 is not None:
        v = 0
        if temp1 is not None:
            v += temp1.val
            temp1 = temp1.next
        if temp2 is not None:
            v += temp2.val
            temp2 = temp2.next
        temp3.next = Node(v)
        temp3 = temp3.next
    return p3


def print_set(p):
    while p is not None:
        print(p.val, "", end="")
        p = p.next
    print()


first = None
for i in range(1, 7):
    pointer = Node(i)
    pointer.next = first
    first = pointer

first1 = None
for i in range(2, 8):
    pointer = Node(i)
    pointer.next = first1
    first1 = pointer
print_set(first)
print_set(first1)
first2 = f(first, first1)
print_set(first2)
