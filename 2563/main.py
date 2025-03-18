def put_paper():
  papers.append(list(map(int, input().split())))
  total_area += 100
  return 

def get_x():
  if x1 < x2:
    x = x1+10 - x2
  elif x1 > x2:
    x = x2+10 - x1
  elif x1 == x2:
    x = x1+10 - x1
  return x

def get_y():
  if y1 < y2:
    y = y1+10 - y2
  elif y1 > y2:
    y = y2+10 - y1
  elif y1 == y2:
    y = y1+10 - y1
  return y

total_area = 0
papers = []
put_paper()
N = int(input())

for i in range(N-1):
  put_paper()
  x1, y1 = papers[0][0], papers[0][1]
  x2, y2 = papers[-1][0], papers[-1][1]
  if x1+10 <= x2 or x1 >= x2+10 or y1+10 <= y2 or y1 >= y2+10:
    papers.pop(0)
    continue
  else:
    total_area -= get_x() * get_y()
    
print(total_area)