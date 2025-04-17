def getRemainder(n,b):
  remainders.append(n%b)
  if n < b:
    return
  return getRemainder(n//b, b)

N, B = map(int, input().split())
remainders = []
getRemainder(N,B)

for i in remainders:
  if i >= 10:
    remainders[remainders.index(i)] = chr(ord('A')+i-10)

print(''.join(map(str, remainders))[::-1])