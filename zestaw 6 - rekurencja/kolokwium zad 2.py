def f(x, y, n):
    def zwieksz_parzyste(x):
        temp = x
        temp2 = 0
        i = 0
        while temp > 0:
            if (temp % 10) % 2 == 0:
                temp2 += ((temp % 10) + 1) * (10**i)
            else:
                temp2 += (temp % 10) * (10 ** i)
            i += 1
            temp //= 10
        return temp2


    def rek(x, y, n, essa, p=0, last=0):
        if x == y and p <= n:
            print(essa)
            return p
        if p > n:
            return 99999
        if last == 3:
            return min(rek(x + 3, y, n,essa + ["A"] , p + 1, 1), rek(x*2, y, n, essa + ["B"], p + 1, 2))
        if last == 2:
            return min(rek(x + 3, y, n,essa + ["A"], p + 1, 1), rek(zwieksz_parzyste(x), y, n,essa + ["C"], p + 1, 3))
        if last == 1:
            return min(rek(x*2, y, n, essa + ["B"], p + 1, 2), rek(zwieksz_parzyste(x), y, n, essa + ["C"], p + 1, 3))
        else:
            return min(rek(x + 3, y, n, essa + ["A"], p + 1, 1), rek(x * 2, y, n, essa + ["B"], p + 1, 2), rek(zwieksz_parzyste(x), y, n, essa + ["C"], p + 1, 3))
    x = rek(11, 31, 4, [])
    if x == 99999:
        return 0
    else:
        return x

print(f(1,2,3))