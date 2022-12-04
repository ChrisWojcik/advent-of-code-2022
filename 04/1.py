import sys

pairs = []

for line in sys.stdin:
  line = line.strip()
  pair = line.split(',')

  pair = list(map(lambda elf: [int(_) for _ in elf.split('-')], pair))
  pairs.append(pair)

answer = 0

for [elf1, elf2] in pairs:
  [elf1_low, elf1_high] = elf1
  [elf2_low, elf2_high] = elf2

  if (elf1_low <= elf2_low and elf1_high >= elf2_high) or \
     (elf2_low <= elf1_low and elf2_high >= elf1_high):
    answer += 1

print(answer)