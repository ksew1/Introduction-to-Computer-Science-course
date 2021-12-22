class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def is_in(self, num):
        p = self
        while p is not None:
            if p.val == num:
                return True
            p = p.next
        return False

    def add_to(self, num):
        if self.is_in(num):
            return
        p = self
        while p.next is not None:
            p = p.next
        p.next = Node(num)

    def remove_from(self, num):

        if self.val == num:
            return self.next
        p = self
        while p.next is not None and p.next.val != num:
            p = p.next
        if p.next is None:
            return self
        else:
            p.next = p.next.next
            return self


def print_set(p):
    while p is not None:
        print(p.val, "", end="")
        p = p.next


set1 = Node(21)
set1.add_to(3)
set1.add_to(3)
set1.add_to(2)
set1 = set1.remove_from(5)
set1 = set1.remove_from(2)
print_set(set1)
