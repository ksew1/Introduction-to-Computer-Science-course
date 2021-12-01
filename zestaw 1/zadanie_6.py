max_x = 10
min_x = 0
epsilon = 0.0000001

while abs(max_x - min_x) > epsilon:
    x = (max_x + min_x) / 2
    if x**x - 2020 == 0:
        break
    elif (min_x**min_x - 2020) * (x**x - 2020) < 0:
        max_x = x
    else:
        min_x = x
print(x)
print(x**x)