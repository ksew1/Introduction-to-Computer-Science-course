class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def length_before_cycle(p):
    fast = p
    slow = p

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            cycle_set = set()
            cycle_set.add(slow)
            slow = slow.next
            while slow != fast:
                cycle_set.add(slow)
                slow = slow.next
            while p.next not in cycle_set:
                p = p.next
            return p
    return None
