class Node:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.next = None

def f(pointer):
    p = pointer
    last = pointer
    while p is not None:
        q = p
        changes = False
        while q.next is not None:
            if p.a <= q.next.a <= p.b or p.a <= q.next.b <= p.b:
                changes = True
                p.a, p.b = min(q.next.a, p.a), max(q.next.b, p.b)
                q.next = q.next.next
            else:
                q = q.next

        if changes:
            q.next = Node(p.a, p.b)
            if p == last:
                pointer = pointer.next
            else:
                pointer = pointer.next
                last.next = p.next
            p = last.next
        else:
            p = p.next
    return pointer


def print_set(p):
    while p is not None:
        print("(", p.a, ",", p.b, ")", "", end="")
        p = p.next
    print()


#[15,19] [2,5] [7,11] [8,12] [5,6] [13,17]
a = Node(15,19)
a.next = Node(2,5)
a.next.next = Node(7,11)
a.next.next.next = Node(8,12)
a.next.next.next.next = Node(5,6)
a.next.next.next.next.next = Node(13,17)
print_set(a)
a = f(a)
print_set(a)

