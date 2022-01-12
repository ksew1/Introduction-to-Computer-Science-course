class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def is_cycle(p):
    been_before = set()
    while p is not None:
        if p in been_before:
            return True
        been_before.add(p)
        p = p.next
    return False
