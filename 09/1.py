import sys

def move_head(head, dir):
  hx, hy = head

  if dir == 'U':
    return (hx, hy + 1)
  if dir == 'D':
    return (hx, hy - 1)
  if dir == 'R':
    return (hx + 1, hy)
  if dir == 'L':
    return (hx - 1, hy)

def move_tail(tail, head):
  hx, hy = head
  tx, ty = tail

  separation_x = hx - tx
  separation_y = hy - ty

  # same row
  if hy == ty:
    if abs(separation_x) > 1:
      tx = tx + 1 if separation_x > 0 else tx - 1
  # same column
  elif hx == tx:
    if abs(separation_y) > 1:
      ty = ty + 1 if separation_y > 0 else ty - 1
  # diagonal
  else:
    if abs(separation_y) > 1 or abs(separation_x) > 1:
      tx = tx + 1 if separation_x > 0 else tx - 1
      ty = ty + 1 if separation_y > 0 else ty - 1

  return (tx, ty)

def move_rope(rope, dir):
  head = move_head(rope[0], dir)
  tail = move_tail(rope[1], head)

  return [head, tail]

rope = [(0,0), (0,0)]
tail_visited = { rope[1] }

for line in sys.stdin:
  [dir, dist] = line.strip().split(' ')
  dist = int(dist)

  for _ in range(0, dist):
    rope = move_rope(rope, dir)
    tail_visited.add(rope[1])

print(len(tail_visited))
