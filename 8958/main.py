n = int(input())

for i in range(n):
    ox = input().split('X')
    result=0
    ox = list(filter(None, ox))
    for j in range(len(ox)):
        for k in range(1, len(ox[j])+1):
            result += k
    print(result)

