import sys

ROCK = '#'
SAND = 'o'
AIR = '.'
SOURCE = '+'

source_point = (500, 0)

blocked = {
  source_point: SOURCE
}

for line in sys.stdin:
  line = line.strip()
  endpoints = line.split(' -> ')
  endpoints = list(map(lambda point: tuple([int(_) for _ in point.split(',')]), endpoints))

  for i in range(1, len(endpoints)):
    x1,y1 = endpoints[i - 1]
    x2,y2 = endpoints[i]

    blocked[(x1, y1)] = ROCK
    blocked[(x2, y2)] = ROCK

    if x1 == x2 and y1 == y2:
      continue

    # vertical line
    if x1 == x2:
      x = x1

      for y in range(y1, y2, 1 if y2 > y1 else -1):
        blocked[(x,y)] = ROCK

    # horizontal line
    elif y1 == y2:
      y = y1

      for x in range(x1, x2, 1 if x2 > x1 else -1):
        blocked[(x,y)] = ROCK

points = blocked.keys()

MIN_X = min(points, key=lambda point: point[0])[0]
MAX_X = max(points, key=lambda point: point[0])[0]
MIN_Y = min(points, key=lambda point: point[1])[1]
MAX_Y = max(points, key=lambda point: point[1])[1]

answer = 0
grain_at = source_point

while True:
  x1, y1 = grain_at

  if y1 + 1 > MAX_Y: # into the abyss
    break
  
  # continue moving in any available direction
  if (x1, y1 + 1) not in blocked:
    grain_at = (x1, y1 + 1)
    continue
  if (x1 - 1, y1 + 1) not in blocked:
    grain_at = (x1 - 1, y1 + 1)
    continue
  if (x1 + 1, y1 + 1) not in blocked:
    grain_at = (x1 + 1, y1 + 1)
    continue
  
  # come to rest and start tracking new grain
  answer += 1
  blocked[grain_at] = SAND
  grain_at = source_point

print(answer)

def draw_cave():
  visualization = ''

  for y in range(MIN_Y, MAX_Y + 1):
    row = ''

    for x in range(MIN_X, MAX_X + 1):
      row += AIR if (x, y) not in blocked else blocked[(x, y)]
    
    row += '\n'
    visualization += row

  return visualization

f = open("vis-1.txt", "w")
f.write(draw_cave())
f.close()