import sys

def get_priority(item):
  if item.isupper():
    return ord(item) - 38
  else:
    return ord(item) - 96

def find_duplicate(rucksack):
  length = len(rucksack)
  midpoint = int(length / 2)

  compartment1 = list(rucksack[0:midpoint])
  compartment2 = list(rucksack[midpoint:length])

  return list(set(compartment1).intersection(set(compartment2)))[0]

sum_of_priorities = 0

for line in sys.stdin:
  rucksack = line.strip()
  duplicate = find_duplicate(rucksack)
  priority = get_priority(duplicate)

  sum_of_priorities += priority

print(sum_of_priorities)
