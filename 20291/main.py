N = int(input())
files = []

for _ in range(N):
  files.append(input().split('.')[1])

setFiles = set(files)
setFiles = list(setFiles)
setFiles.sort()
files.sort()

for ext in setFiles:
  print(ext, files.count(ext))