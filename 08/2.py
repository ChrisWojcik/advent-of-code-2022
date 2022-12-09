import sys

forest = {}

ROWS = 0
COLS = 0

row = 0

for line in sys.stdin:
  line = line.strip()

  for col in range(0, len(line)):
    height = int(line[col])
    location = (row, col)
    forest[location] = height

  COLS = len(line)
  row += 1

ROWS = row

best_score = 0

for location, height in forest.items():
  row, col = location

  # on border
  if row == 0 or col == 0 or row == ROWS - 1 or col == COLS - 1:
    continue

  #up
  up = 0

  for r in range(row - 1, -1, -1):
    up += 1

    if forest[(r, col)] >= height:
      break

  #down
  down = 0

  for r in range(row + 1, ROWS):
    down += 1

    if forest[(r, col)] >= height:
      break

  #left
  left = 0

  for c in range(col - 1, -1, -1):
    left += 1

    if forest[(row, c)] >= height:
      break

  #right
  right = 0

  for c in range(col + 1, COLS):
    right += 1

    if forest[(row, c)] >= height:
      break

  score = up * down * left * right

  if score > best_score:
    best_score = score

print(best_score)