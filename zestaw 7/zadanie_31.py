from helper_module import print_ll, arr2list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def sentinel(p):
    temp = Node(None)
    temp.next = p
    return temp
def f(p):
    p_start = sentinel(p)
    p = p_start
    q_start = Node(None)
    q = q_start
    counter = 0
    while p.next is not None:
        if p.next.val > 0 and p.next.val % 2 == 0:
            q.next = p.next
            p.next = p.next.next
            q.next.next = None
            q = q.next
        elif p.next.val < 0 and p.next.val % 2 != 0:
            p = p.next
        else:
            counter += 1
            p.next = p.next.next
    return p_start.next, q_start.next


a = arr2list([3, -5, -23, 342, 42, 65, 23])
print_ll(a.next)
a = a.next
a, b= f(a)
print_ll(a)
print_ll(b)



