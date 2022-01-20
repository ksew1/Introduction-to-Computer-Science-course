class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def f(p, q):
    p_start = p
    q_start = q
    while p != None:
        if q == None:
            return True
        if p.val == q.val:
            p = p.next
            q = q.next
        else:
            p_start = p_start.next
            p = p_start
            q = q_start
    if p == None and q == None:
        return True
    return False
