a, b = 40, 12
while a < 1_000_000:
    print(a, " ",  end="")
    a, b = b, a + b
