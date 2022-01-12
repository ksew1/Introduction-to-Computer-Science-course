class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def is_cycle(p):
    pointer = p
    been_before = set()
    i = 0
    while p is not None:
        i += 1
        if p in been_before:
            while pointer == p:
                i -= 1
                pointer = pointer.next
            return True
        been_before.add(p)
        p = p.next
    return False
