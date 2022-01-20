class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def f(p):
    fast = p
    slow = p
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            slow = p
            counter = 0
            while fast != slow:
                counter += 1
                slow = slow.next
                fast = fast.next
            return counter
    return None
