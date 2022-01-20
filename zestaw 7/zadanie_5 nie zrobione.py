class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def f(p):
    first1 = [None for _ in range(10)]
    last = [None for _ in range(10)]
    while p is not None:
        v = p.val % 10
        temp = p.next
        if first1[v] is None:
            first1[v] = p
            first1[v] = last[v]
        else:
            last[v] = p
            last[v].next = None
            last[v] = last[v].next
        p = temp
    for i in first1:
        print_set(i)


def print_set(p):
    while p is not None:
        print(p.val, "", end="")
        p = p.next
    print()


first = Node(1)
pointer = first
for i in [2,4,6,230,34,6,54234,234,2,34,2,3,4,23,4,234234234457690890,7,56,8,678,23]:
    pointer.next = Node(i)
    pointer = pointer.next
print_set(first)

f(first)