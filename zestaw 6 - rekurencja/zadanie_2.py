def waga(n):
    i = 2
    counter = 0
    while n > 1 and i*i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            counter += 1
        i += 1
    if n > 1:
        counter += 1
    return counter


def function(tab):
    suma = 0
    t = [0] * len(tab)
    for i in range(len(tab)):
        t[i] = waga(tab[i])
        suma += t[i]
    if suma % 3 == 0:
        return div(t)


def div(t, p=0, s1=0, s2=0, s3=0):
    if p == len(t):
        return s1 == s2 and s2 == s3
    return div(t, p + 1, s1 + t[p], s2, s3) or div(t, p + 1, s1, s2 + t[p], s3) or div(t, p + 1, s1, s2, s3 + t[p])
