board = []
for _ in range(4):
    board.append(input().split())

for i in range(4):
    print(' '.join(reversed(board[3-i])))
