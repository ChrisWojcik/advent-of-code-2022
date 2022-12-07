import sys

datastream = sys.stdin.read().strip()

for i in range(13, len(datastream)):
  last_fourteen = set([datastream[i - n] for n in range(0, 14)])

  if len(last_fourteen) == 14:
    print(i + 1)
    break