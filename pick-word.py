import random
with open('filename.txt', 'r') as f:
  words = f.readlines()
print(random.choice(words).strip())
