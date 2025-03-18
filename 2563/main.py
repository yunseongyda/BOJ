board = [[0]*100 for _ in range(100)]
papers = [list(map(int, input().split())) for _ in range(int(input()))]

for x, y in papers:
  for i in range(x, x+10):
    for j in range(y, y+10):
      board[i][j] = 1

print(sum(sum(i) for i in board))