import sys
import re

# [crate stacks, procedure]
puzzle_input = [[],[]]
index = 0

# split the input in half on the empty line
for line in sys.stdin:
  if line in ('\n', '\r\n'):
    index += 1
  else:
    puzzle_input[index].append(line)

# last line of crate_stacks is the crate numbers
crate_numbers = puzzle_input[0].pop()
num_stacks = len(crate_numbers.strip().split('   '))

# create an array of "stacks" (LIFO) from the puzzle input
# stack "0" stays empty to match the 1-indexed procedure steps
# 0 - []
# 1 - ['Z', 'N']
# 2 - ['M', 'C', 'D']
# 3 - ['P']
crate_stacks = [[] for _ in range(0, num_stacks + 1)]

for line in reversed(puzzle_input[0]):
  current_crate = 1

  for i in range(1, num_stacks * 4, 4):
    if i < len(line) and line[i] != ' ':
      crate_stacks[current_crate].append(line[i])
    
    current_crate += 1

# parse the integers out of each procedure step
# e.g. "move 1 from 2 to 1" becomes [1, 2, 1]
procedure = []

for line in puzzle_input[1]:
  step = [int(_) for _ in re.findall(r'\d+', line)]
  procedure.append(step)

# move one crate at a time
for step in procedure:
  [num_crates, before, after] = step

  for i in range(0, num_crates):
    crate_to_move = crate_stacks[before].pop()
    crate_stacks[after].append(crate_to_move)

message = ''

for stack in crate_stacks:
  if len(stack) > 0:
    message += stack[len(stack) - 1]

print(message)