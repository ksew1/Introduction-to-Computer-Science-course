for nr in range(2, 1_000_000):
    i = 2
    sum_nr = 1
    while i*i < nr:
        if nr % i == 0:
            sum_nr += i + nr // i
        i += 1
    if i*i == nr:
        sum_nr += i
    if sum_nr == nr:
        print("Perfect number: ", nr)
