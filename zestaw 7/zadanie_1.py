class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def is_in(self, num):
        def rek(p, n):
            if p.val == n:
                return True
            if p.next is None:
                return False
            rek(p.next, n)

        return rek(self, num)

    def add_to(self, num):
        def rek(p, n):
            if p.next is None:
                p.next = Node(n)
                return
            rek(p.next, n)

        if not self.is_in(num):
            rek(self, num)

    def remove_from(self, num):

        def rek(p, n):
            if p.next.val == n:
                p.next = p.next.next
                return self
        if self.val == num:
            return self.next
        else:
            return rek(self, num)

def print_set(p):
    while p is not None:
        print(p.val, "", end="")
        p = p.next



set1 = Node(5)
set1.add_to(3)
set1.add_to(2)
set1.add_to(-2)
set1 = set1.remove_from(5)
print_set(set1)
