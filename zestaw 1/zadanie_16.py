max_step = 0
id_n = 0
for n in range(2, 10001):
    step = 0
    A = n
    while A > 1:
        A = (A % 2) * (3 * A + 1) + (1 - A % 2) * A / 2
        step += 1
    if step > max_step:
        max_step = step
        id_n = n
print(max_step, id_n)

