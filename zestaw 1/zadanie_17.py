from random import randint
from math import inf


epsilon = 0.00000001

for _ in range(20):
    a = randint(1, 100)
    b = randint(1, 100)
    old_a = 1
    old_b = 10000000000000000
    while abs(old_b / old_a - b / a) > epsilon:
        old_b, old_a = b, a
        a, b = b, a + b
    print(b/a)
