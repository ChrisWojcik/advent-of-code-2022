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

visible_trees = 0

for location, height in forest.items():
  row, col = location

  # on border
  if row == 0 or col == 0 or row == ROWS - 1 or col == COLS - 1:
    visible_trees += 1
    continue
  
  # up
  visible_from_top = True

  for r in range(row - 1, -1, -1):
    tree_above = (r, col)

    if forest[tree_above] >= height:
      visible_from_top = False
      break

  # down
  visible_from_bottom = True

  for r in range(row + 1, ROWS):
    tree_below = (r, col)

    if forest[tree_below] >= height:
      visible_from_bottom = False
      break
  
  # left
  visible_from_left = True

  for c in range(col - 1, -1, -1):
    tree_to_left = (row, c)

    if forest[tree_to_left] >= height:
      visible_from_left = False
      break
  
  # right
  visible_from_right = True

  for c in range(col + 1, COLS):
    tree_to_right = (row, c)

    if forest[tree_to_right] >= height:
      visible_from_right = False
      break

  if visible_from_top or \
      visible_from_bottom or \
      visible_from_left or \
      visible_from_right:

    visible_trees += 1

print(visible_trees)