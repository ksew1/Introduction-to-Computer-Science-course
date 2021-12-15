def get_first_n(n):
    while n > 9:
        n //= 10
    return n


steps = (((0, 1), (1, 0), (1, 1)),
         ((0, -1), (-1, 0), (-1, -1)),
         ((0, 1), (-1, 0), (-1, 1)),
         ((0, -1), (1, 0), (1, -1)))


def rek(w, k):
    global steps
    global board
    if w == 7 and k == 7 or w == 0 and k == 7 or w == 0 and k == 0 or w == 7 and k == 0:
        return True
    for i in range(4):
        for x, y in steps[i]:
            if 0 <= w + x < 8 and 0 <= k + y < 8:
                if board[w][k] % 10 < get_first_n(board[w + x][k + x]):
                    if rek(w + x, k + y):
                        return True

    return False


board = [
    [1, 4, 6, 2, 3, 5, 35, 2],
    [1, 4, 6, 2, 3, 5, 35, 2],
    [1, 4, 6, 82, 3, 5, 35, 2],
    [1, 4, 6, 2, 3, 5, 35, 2],
    [1, 4, 6, 2, 3, 5, 91, 2],
    [1, 4, 6, 82, 3, 5, 24, 2],
    [1, 4, 6, 2, 3, 5, 35, 7],
    [1, 4, 6, 2, 3, 5, 35, 8],
]

print(rek(0, 1))
