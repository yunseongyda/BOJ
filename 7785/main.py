n = int(input())
employees = {}
for _ in range(n):
  name, state = input().split()
  employees[name] = state

working = [name for name, state in employees.items() if state == 'enter']
working.sort(reverse=True)

print(*working, sep='\n')