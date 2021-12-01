def main_function(tab):
    def change_system(n):
        k = 1
        new_n = 0
        while n > 0:
            new_n += (n % 5) * k
            n //= 5
            k *= 10
        return new_n
    def cyfry(a):
        tab_a = [False for _ in range(5)]
        while a > 0:
            tab_a[a % 10] = True
            a //= 10
        return tab_a
    def porownanie(tab_i, tab_j):
        for k in range(5):
            if tab_i[k] != tab_j[k]:
                return 0
        return 1
    tab_5 = [change_system(el) for el in tab]
    max_counter = 0
    i = 0

    while len(tab_5) - max_counter > i:
        tab_i = cyfry(tab_5[i])
        counter = 0

        for j in range(i, len(tab_5)):
            tab_j = cyfry(tab_5[j])
            counter += porownanie(tab_i, tab_j)

        max_counter = max(max_counter, counter)

        i += 1
    print(max_counter)

main_function([1,6, 7, 6])