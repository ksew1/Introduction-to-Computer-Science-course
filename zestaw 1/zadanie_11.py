def sum_of_div(nr):
    i = 2
    sum_nr = 1
    while i * i < nr:
        if nr % i == 0:
            sum_nr += i + nr // i
        i += 1
    if i * i == nr:
        sum_nr += i
    return sum_nr


for num in range(2, 1_000_000):
    sum1 = sum_of_div(num)
    if sum1 > num:
        if num == sum_of_div(sum1):
            print(num, sum1)
