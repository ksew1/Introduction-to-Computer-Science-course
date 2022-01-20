from helper_module import print_ll, arr2list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
def f(p, q):
    new_pointer = Node(None)
    new = new_pointer
    while p != None and q != None:
        temp = Node(p.val - q.val)
        new.next = temp
        new = new.next
        p = p.next
        q = q.next
    if p != None or q != None:
        if p == None:
            new.val = q.val
            new.next = q.next
        if q == None:
            new.val = p.val
            new.next = p.next
    return new_pointer.next


a = arr2list([2,4,643,534,68,23])
b = arr2list([5,23,4,1,1,1,1,1,1,1,1,1,1])
a = a.next
b = b.next
print_ll(a)
print_ll(b)
z = f(a, b)
print_ll(z)