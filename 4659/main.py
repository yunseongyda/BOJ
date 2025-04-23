consonants = [
  'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 
  'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
]
vowels = ['a', 'e', 'i', 'o', 'u']

while True:
  pw = input()
  if pw == 'end':
    break

  is_acceptable = True
  
  # 1
  if not any(char in vowels for char in pw):
    print(f"<{pw}> is not acceptable.")
    is_acceptable = False
    continue

  for i in range(len(pw)):
    # 2
    if i == len(pw) - 1:
      break
    if pw[i + 1] in ['e','o']:
      pass
    elif pw[i] == pw[i + 1]:
      print(f"<{pw}> is not acceptable.")
      is_acceptable = False
      break

    # 3
    if i == len(pw) - 2:
      break
    if pw[i] in consonants and pw[i + 1] in consonants and pw[i + 2] in consonants:
      print(f"<{pw}> is not acceptable.")
      is_acceptable = False
      break
    elif pw[i] in vowels and pw[i + 1] in vowels and pw[i + 2] in vowels:
      print(f"<{pw}> is not acceptable.")
      is_acceptable = False
      break

  if is_acceptable:
      print(f"<{pw}> is acceptable.")