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

# must be a smarter way to do this, but our p1 solution is fast enough
# that this runs in "mere minutes"! rather than hours
def scan_square(min, max):
  # between min and max Y values, apply p1 solution
  for Y in range(min, max + 1):   
    excluded_intervals = scan_line(Y)

    # if there aren't at least 2 intervals, there can't be any gaps
    # on this line where the beacon could be
    if len(excluded_intervals) > 2:
      continue
    
    # loop through the intervals
    for i in range(1, len(excluded_intervals)):
      s1, e1 = excluded_intervals[i - 1]
      s2, e2 = excluded_intervals[i]

      # find an x coordinate in a "gap" between a pair of intervals
      # if x is within our min/max range and (x, Y) is not occupied
      # by another beacon, we've found our point
      if s2 > e1 + 1:
        x = e1 + 1
        if (x, Y) in beacons:
          continue
        if x < min or x > max:
          continue
        else:
          return (x, Y)

MIN_XY = 0
MAX_XY = 4000000
#MAX_XY = 20

MULTIPLIER = 4000000

bx, by = scan_square(MIN_XY, MAX_XY)
tuning_frequency = bx * MULTIPLIER + by

print(tuning_frequency)