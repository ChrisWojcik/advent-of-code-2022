import sys

x = 1
cycle = 1

screen = ''

def tick(screen, x, cycle):
  pixel = (cycle - 1) % 40

  if pixel in [x - 1, x, x + 1]:
    screen = screen + '#'
  else:
    screen = screen + '.'

  if cycle % 40 == 0:
    screen = screen + '\n'

  return screen

for line in sys.stdin:
  line = line.strip().split(' ')

  if line[0] == 'addx':
    value = int(line[1])

    screen = tick(screen, x, cycle)
    cycle += 1

    screen = tick(screen, x, cycle)
    x += value
    cycle += 1
  else:
    screen = tick(screen, x, cycle)
    cycle += 1

print(screen)
