from helper_module import arr2list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def sentinel(p):
    temp = Node(None)
    temp.next = p
    return temp


def remove(p, q):
    p_start = sentinel(p)
    q_start = sentinel(q)
    p = p_start
    q = q_start
    counter = 0
    while p.next is not None and q.next is not None:
        if p.next.val == q.next.val:
            p.next = p.next.next
            q.next = q.next.next
            counter += 1
        elif p.next.val < q.next.val:
            p = p.next
        else:
            q = q.next
    return counter, p_start.next, q_start.next


a = arr2list([1, 2, 3, 4, 645, 7567, 42344])
b = arr2list([3, 4, 5, 6, 7, 8, 9])
a = a.next
b = b.next
print(a)
print(b)
_, a, b = remove(a, b)
print(a)
print(b)
