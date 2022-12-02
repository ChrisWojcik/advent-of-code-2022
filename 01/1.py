import sys

calories_per_elf = [0]
current_elf = 0

for line in sys.stdin:
  line = line.strip()

  if line:
    calories = int(line)
    calories_per_elf[current_elf] += calories
  else:
    calories_per_elf.append(0)
    current_elf += 1

answer = max(calories_per_elf)
print(answer)
  