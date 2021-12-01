from math import log10

def main_function(n):
    def prime(n):
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
    def same_nr(n):
        tab = [0 for _ in range(10)]
        while n > 0:
            if tab[n % 10] == 0:
                tab[n % 10] = 1
            else:
                return False
            n //= 10
        return True
    leng = int(log10(n)) + 1
    number = 0
    i = 0
    while n > 0:
        new_n = n % 10**(leng - 1 + i)
        if same_nr(new_n) and prime(new_n):
            number = max(new_n, number)
        n //= 10
        temp = new_n
        i += 1
        j = 1
        while temp > 0:
            temp_new = n // 10**j
            temp //= 10
            if same_nr(temp_new) and prime(temp_new):
                number = max(temp_new, number)
            j += 1
    print(number)
main_function(1375)