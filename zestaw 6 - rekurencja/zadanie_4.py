
moves = ((1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))


def tablica(t):
    for i in range(len(t)):
        for j in range(len(t)):
            print(t[i][j], end='\t')
        print('')
    print()


def move(board, w, k, r, p=1):
    tablica(board)

    board[w][k] = p
    if p == len(board)**2:
        print(True)
        return True
    for m in r:
        if check(board, w + m[0], k + m[1]):
            if move(board, w + m[0], k + m[1], r, p + 1):
                return True
    board[w][k] = 0


def check(board, w, k):
    if 0 <= w < n and 0 <= k < n and board[w][k] == 0:
        return True
    return False


n = 5
tab = [[0 for _ in range(n)] for _ in range(n)]
print(move(tab, 0, 0, moves))
