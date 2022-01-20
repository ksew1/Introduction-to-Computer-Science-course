
from helper_module import print_ll, arr2list


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def sort(p, q):
    while p.next is not None and p.next.val < q.next.val:
        p = p.next
    if p.next is None:
        p.next = Node(q.next.val)
    if p.next.val > q.next.val:
        temp = Node(q.next.val)
        p.next, temp.next = temp, p.next
    q.next = q.next.next


def sentinel(p):
    temp = Node(None)
    temp.next = p
    return temp


def f(p, q):
    p_start = sentinel(p)
    q_start = sentinel(q)
    q = q_start
    p = p_start
    while q.next is not None:
        sort(p, q)
    return p_start.next


a = arr2list([2, 4, 5, 6, 7, 876])
b = arr2list([63, 234, 25, 6, 1, 2, 4])
a = a.next
b = b.next
print(a)
print(b)
a = f(a, b)
print_ll(a)
