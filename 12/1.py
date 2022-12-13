import sys
from collections import deque

locations = {}
elevations = {}
start = None
end = None

MAP_WIDTH = 0
MAP_HEIGHT = 0

y = 0

for line in sys.stdin:
  line = line.strip()

  for x in range(0, len(line)):
    location = (x, y)
    elevation = line[x]

    if elevation == 'S':
      start = location
      elevations[location] = ord('a')
      locations[location] = set()
    elif elevation == 'E':
      end = location
      elevations[location] = ord('z')
      locations[location] = set()
    else:
      elevations[location] = ord(elevation)
      locations[location] = set()

  MAP_WIDTH = len(line)
  y += 1

MAP_HEIGHT = y

for location, elevation in elevations.items():
  x, y = location
  
  above = None if y == 0 else (x, y - 1)
  below = None if y == MAP_HEIGHT - 1 else (x, y + 1)
  left  = None if x == MAP_WIDTH - 1 else (x + 1, y)
  right = None if x == 0 else (x - 1, y)

  neighbors = [above, below, left, right]

  for neighbor in neighbors:
    # a "node" in the grid is only "connected" to one of its neighbors if
    # the elevation of the neighbor is AT MOST one step higher
    if neighbor != None and elevations[neighbor] <= elevation + 1:
      locations[location].add(neighbor)

# unweighted - start and end
def bfs_shorest_path(graph, start, end):
  q = deque([[start]])
  visited = set()

  if start == end:
    return [start]

  while len(q) > 0:
    path = q.popleft()
    node = path[-1]

    if node not in visited:
      neighbors = graph[node]
      
      for neighbor in neighbors:
        new_path = list(path)
        new_path.append(neighbor)
        q.append(new_path)

        if neighbor == end:
          return new_path
      
      visited.add(node)
  
  return None

fewest_steps = len(bfs_shorest_path(locations, start, end)) - 1
print(fewest_steps)
