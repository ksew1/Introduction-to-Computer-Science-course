nr = int(input(">"))
i = 2
prime_number = True
while i**2 <= nr:
    if nr % i == 0:
        prime_number = False
        break
    i += 1
if nr <= 1:
    print(False)
else:
    print(prime_number)
