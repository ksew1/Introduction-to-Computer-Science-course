class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove_sorted(p, val):
    while p.next != None and p.next.val < val:
        p = p.next
    if p.next != None:
        if p.next.val == val:
            p.next = p.next.next
            return True
    return False


def sentinel(p):
    temp = Node(None)
    temp.next = p
    return temp

def remove(p, q):
    p = sentinel(p)
    q = sentinel(q)
    counter = 0
    while q.next != None:
        if remove_sorted(p, q.next.val):
            counter += 1
            q.next = q.next.next
        else:
            q = q.next
    return counter * 2