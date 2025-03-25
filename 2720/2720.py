T = int(input())

for _ in range(T):
  change = []
  c = int(input())
  change.append(c // 25)
  c %= 25
  change.append(c//10)
  c %= 10
  change.append(c//5)
  c %= 5
  change.append(c//1)
  
  print(*change)