import sys

def get_priority(item):
  if item.isupper():
    return ord(item) - 38
  else:
    return ord(item) - 96

groups = []
current_group = -1

for i, line in enumerate(sys.stdin):
  rucksack = list(line.strip())

  if i % 3 == 0:
    groups.append(list())
    current_group += 1

  groups[current_group].append(rucksack)

sum_of_priorities = 0

for group in groups:
  [sack1, sack2, sack3] = group

  intersection = set(sack1).intersection(set(sack2), set(sack3))
  badge = list(intersection)[0]
  priority = get_priority(badge)

  sum_of_priorities += priority

print(sum_of_priorities)
