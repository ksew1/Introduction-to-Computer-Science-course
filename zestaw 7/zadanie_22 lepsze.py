class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def is_cycle(p):
    fast = p
    slow = p
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False
