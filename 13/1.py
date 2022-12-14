import sys

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

pairs = [[]]

for line in sys.stdin:
  line = line.strip()

  if not line:
    pairs.append([])
  else:
    pairs[-1].append(eval(line))

answer = 0

for index in range(0, len(pairs)):
  left, right = pairs[index]
  compared = comparator(left, right)
  
  if compared == -1:
    answer += index + 1

print(answer)
