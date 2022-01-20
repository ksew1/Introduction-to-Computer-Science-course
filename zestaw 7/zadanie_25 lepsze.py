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
            while fast != slow.next:
                slow = slow.next
                fast = fast.next
            return slow
    return None
