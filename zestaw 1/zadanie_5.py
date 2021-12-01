nr = int(input(">"))

square = nr / 2
epsilon = 0.00001
while abs(nr / square - square) > epsilon:
    square = (nr / square + square) / 2

print(square)
