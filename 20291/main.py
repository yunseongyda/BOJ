N = int(input())
files = {}

for _ in range(N):
  file = input().split('.')[1]
  if file in files:
    files[file] += 1
  else:
    files[file] = 1

sorted_files = sorted(files.items(), key=lambda x: x[0])

for key, value in sorted_files:
  print(key, value)