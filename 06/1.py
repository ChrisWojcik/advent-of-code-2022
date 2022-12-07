import sys

datastream = sys.stdin.read().strip()

for i in range(3, len(datastream)):
  last_four = set([datastream[i - n] for n in range(0, 4)])

  if len(last_four) == 4:
    print(i + 1)
    break