import sys

x = 1
cycle = 1

answer = 0

def tick(x, cycle):
  if cycle in [20, 60, 100, 140, 180, 220]:
    return x * cycle
  else:
    return 0

for line in sys.stdin:
  line = line.strip().split(' ')

  if line[0] == 'addx':
    value = int(line[1])

    answer += tick(x, cycle)
    cycle += 1

    answer += tick(x, cycle)
    x += value
    cycle += 1
  else:
    answer += tick(x, cycle)
    cycle += 1

print(answer)
