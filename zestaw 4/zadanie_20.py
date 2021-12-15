from copy import deepcopy


tab = [[1 for _ in range(8)] for _ in range(8)]


def tablica(t):
    for i in range(len(t)):
        for j in range(len(t)):
            print(t[i][j], end='\t')
        print('')
    print()


for el in tab:
    print(el)


def f(t):
    N = len(t)

    def count(w, k, bit_t):
        s = 0
        temp = bit_t[w][k]
        for z in range(N):
            s += bit_t[z][k] + bit_t[w][z]
            bit_t[z][k], bit_t[w][z] = 0, 0
        s -= bit_t[w][k]
        bit_t[w][k] = temp
        return s
    max_s = - 10**10
    id_s = None
    for i in range(N**2):
        for j in range(i + 1, N**2):
            temp_t = deepcopy(t)
            temp_s = count(i % N, i // N, temp_t) + count(j % N, j // N, temp_t)
            tablica(temp_t)
            if temp_s > max_s:
                max_s = temp_s
                id_s = ((i % N, i // N), (j % N, j // N))

    return id_s, max_s

tablica(tab)
print(f(tab))
tablica(tab)
