x = 0.5 ** 0.5
next_step = (0.5 * (1 + x)) ** 0.5
for _ in range(100):
    x *= next_step
    next_step = (0.5 * (1 + next_step)) ** 0.5
print(2/ x)