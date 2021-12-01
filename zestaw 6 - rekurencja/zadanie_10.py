def perm(n, s, i=0):
    if i == len(n):
        s.append(n.copy())
        return
    for j in range(i, len(n)):
        n[i], n[j] = n[j], n[i]
        perm(n, s, i + 1)
        n[i], n[j] = n[j], n[i]


def inv_m(el_s):
    inv = 0
    for i in range(len(el_s)-1):
        for j in range(len(el_s)):
            if el_s[i] > el_s[j]:
                inv += 1
    return inv


def main_f(m):
    n = [i for i in range(len(m))]
    s = []
    perm(n, s)
    det = 0
    for i in range(len(s)):
        il = 1
        for j in range(len(m)):
            il *= m[j][s[i][j]]

        if inv_m(s[i]) % 2 == 0:
            det += il
        else:
            det -= il
    return det


print(main_f([[1, 7], [4, 3]]))
