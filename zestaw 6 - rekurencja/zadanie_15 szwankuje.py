def main_f():
    def dead_points(board, w, k, val):
        for i in range(8):
            board[w][i] += val
        for i in range(8):
            board[i][k] += val
        i = 1
        while w - i >= 0 and k - i >= 0:
            board[w-i][k-i] += val
            i += 1
        i = 0
        while w + i < 8 and k + i < 8:
            board[w+i][k+i] += val
            i += 1
        board[w][k] -= 2 * val
        board[w][k] += val * 10
        if val == 1:
            wb[w][k] = "H"
        if val == -1:
            wb[w][k] = 0

    def tablica(t):
        for i in range(len(t)):
            for j in range(len(t)):
                print(t[i][j], end='\t')
            print('')
        print()

    def rek(board, w=0, k=0, h=0):
        global wb
        tablica(board)
        if h == 8:
            tablica(board)
            return True
        for i in range(8):
            for j in range(8):
                if board[i][j] == 0:
                    dead_points(board, i, j, 1)
                    if rek(board, i, j, h + 1):
                        return True
                    dead_points(board, i, j, -1)
        return False

    tab = [[0 for _ in range(8)] for _ in range(8)]
    wb = [[0 for _ in range(8)] for _ in range(8)]
    print(rek(tab))
    tablica(wb)

main_f()
