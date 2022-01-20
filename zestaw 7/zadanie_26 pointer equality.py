class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def f(pointer1, pointer2):
    p = pointer1
    q = pointer2
    while p != None or q != None:
        if p == pointer2 or q == pointer1:
            return True
        if p != None:
            p = p.next
        if q != None:
            q = q.next
    return False

