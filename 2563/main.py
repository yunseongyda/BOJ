def put_paper(ta, n):
  papers[n] = list(map(int, input().split()))
  ta += 100
  return ta

def checkOverlap(rec, prev):
  x1, y1 = rec[0], rec[1]
  x2, y2 = prev[0], prev[1]
  if x2 >= x1+10 or y2 >= y1+10 or x2+10 <= x1 or y2+10 <= y1:
    return 0
  return 1

def get_x(rec, prev):
  x1, y1 = rec[0], rec[1]
  x2, y2 = prev[0], prev[1]
  if x1 < x2:
    x = x1+10 - x2
  elif x1 > x2:
    x = x2+10 - x1
  elif x1 == x2:
    x = x1+10 - x1
  return x

def get_y(rec, prev):
  x1, y1 = rec[0], rec[1]
  x2, y2 = prev[0], prev[1]
  if y1 < y2:
    y = y1+10 - y2
  elif y1 > y2:
    y = y2+10 - y1
  elif y1 == y2:
    y = y1+10 - y1
  return y

total_area = 0
papers = []
N = int(input())
papers = [[0,0] for i in range(N)]
total_area = put_paper(total_area, 0)

for i in range(1, N):
  total_area = put_paper(total_area, i)
  for j in range(1, i+1):
    if checkOverlap(papers[-1], papers[-j-1]):
      total_area -= get_x(papers[-1], papers[-j-1]) * get_y(papers[-1], papers[-j-1])
    
print(total_area)