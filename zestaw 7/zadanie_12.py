class Node:
    def __init__(self, char):
        self.char = char
        self.next = None


def f(point, string):
    temp = Node(None)
    temp.next = point
    point = temp
    ans = True
    for c in string:
        p = point
        if ord(p.next.char) > ord(c):
            global first
            temp = Node(c)
            temp.next = first
            first = temp
            continue
        while p.next.next is not None:
            if ord(p.next.char) == ord(c):
                break
            if ord(p.next.char) > ord(c):
                ans = False
                temp = Node(c)
                p.next, temp.next = temp, p.next
                break
            p = p.next
        else:
            ans = False
            temp = Node(c)
            if ord(p.next.char) > ord(c):
                p.next = temp
                temp.next = p.next.next
            else:
                p.next.next = temp
    return ans

# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def print_set(p):
    while p is not None:
        print(p.char, "", end="")
        p = p.next
    print()


first = Node("p")
pointer = first
for i in ["q", "r", "t"]:
    pointer.next = Node(i)
    pointer = pointer.next
print_set(first)
print(f(first, "z"))
print_set(first)
