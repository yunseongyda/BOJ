def getRemainder(n,b):
  remainders.append(chr(ord('A')+(n%b-10)))
  if n < b:
    return 0
  return getRemainder(n//b, b)

N, B = map(int, input().split())
remainders = []
getRemainder(N,B)
print(''.join(remainders))