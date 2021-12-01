from random import randint


def move(t, k, cost=0, p=0):
    if k < p:
        return 999999  # float('inf')
    if k == 7 and p == 7:
        cost += t[7][7]
        return cost
    if k == 0:
        return min(move(t, k, cost + t[p][k], p+1), move(t, k+1, cost + t[p][k], p+1))
    if k == 7:
        return min(move(t, k, cost + t[p][k], p + 1), move(t, k-1, cost + t[p][k], p+1))
    else:
        return min(move(t, k, cost + t[p][k], p+1), move(t, k-1, cost + t[p][k], p+1), move(t, k+1, cost + t[p][k], p+1))


def make_a_board():
    board = []
    for i in range(8):
        board.append([])
        for j in range(8):
            board[i].append(randint(1, 5))
    for el in board:
        print(el)
    return board


board1 = make_a_board()
print("min", move(board1, 0))
