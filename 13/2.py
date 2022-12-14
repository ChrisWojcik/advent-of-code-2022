import sys
from functools import cmp_to_key

def comparator(left, right):
  if left == None and right == None:
    return 0
  
  if left == None:
    return -1
  
  if right == None:
    return 1

  left_is_integer = isinstance(left, int)
  right_is_integer = isinstance(right, int)
  
  # both integers
  if left_is_integer and right_is_integer:
    if left == right:
      return 0
    if left < right:
      return -1
    else:
      return 1
  
  # mixed types
  elif left_is_integer or right_is_integer:
    left_as_list = [left] if left_is_integer else left
    right_as_list = [right] if right_is_integer else right

    # convert and retry
    return comparator(left_as_list, right_as_list)

  # both lists, loop through items
  else:
    for index in range(0, max(len(left), len(right))):
      left_at_index = None if index >= len(left) else left[index]
      right_at_index = None if index >= len(right) else right[index]

      compared = comparator(left_at_index, right_at_index)

      # stop early, we have our comparison
      if compared != 0:
        return compared

  # fall through, values equal
  return 0

packets = []

for line in sys.stdin:
  line = line.strip()

  if line:
    packets.append(eval(line))

first_divider = [[2]]
second_divider = [[6]]

packets.append(first_divider)
packets.append(second_divider)

packets.sort(key=cmp_to_key(comparator))

decoder_key = (packets.index(first_divider) + 1) * (packets.index(second_divider) + 1)
print(decoder_key)
