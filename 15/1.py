import sys
import re

sensor_beacon_pairs = {}
beacons = set()

for line in sys.stdin:
  sx, sy, bx, by = [int(_) for _ in re.findall(r'-?\d+', line)]

  sensor = (sx, sy)
  beacon = (bx, by)

  sensor_beacon_pairs[sensor] = beacon
  beacons.add(beacon)

def merge_intervals(intervals):
  if len(intervals) < 2:
    return intervals

  in_order = sorted(intervals, key=lambda _: _[0])
  merged = [in_order[0]]

  for interval in in_order[1:]:
    prev_interval = merged[-1]

    if interval[0] <= prev_interval[1]:
      merged[-1] = [prev_interval[0], max(prev_interval[1], interval[1])]
    else:
      merged.append(interval)

  return merged

def scan_line(Y):
  excluded_intervals = []

  # for each sensor, determine an interval of positions it
  # excludes (if it intersects the reference line)
  for sensor, beacon in sensor_beacon_pairs.items():
    sx, sy = sensor
    bx, by = beacon

    # manhattan distance
    range = abs(sx - bx) + abs(sy - by)

    # endpoints of a polygon with edges through
    # all positions a manhattan distance away
    # (surrounding anything closer)
    exclusion_zone = [
      (sx - range, sy),
      (sx, sy - range),
      (sx + range, sy),
      (sx, sy + range)
    ]

    # sensor's exclusion zone does not overlap reference line
    if Y < exclusion_zone[1][1] or Y > exclusion_zone[3][1]:
      continue
    
    # how large of an interval the exclusion zone overlaps
    # is dependent on where the line is in relation to the
    # center point of the zone (the sensor)
    dy = abs(Y - sy)
    start = exclusion_zone[0][0] + dy
    end = exclusion_zone[2][0] - dy

    excluded_intervals.append([start, end])

  return merge_intervals(excluded_intervals)

Y = 2000000
# Y = 10
excluded_intervals = scan_line(Y)
excluded_positions = 0

# sum up the lengths of the intervals (inclusive)
for interval in excluded_intervals:
  start, end = interval
  excluded_positions += end - start + 1

# don't count positions along the line which already have a beacon
# beacon - we know any existing beacons are in range of a known sensor
for beacon in beacons:
  bx,by = beacon

  if by == Y:
    excluded_positions -= 1

print(excluded_positions)