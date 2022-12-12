import math

class Monkey():
  def __init__(self, starting_items, operation, divisor):
    self.items = starting_items
    self.operation = operation
    self.divisor = divisor
    self.items_inspected = 0
    self.true_monkey = None
    self.false_monkey = None

  def set_friends(self, true_monkey, false_monkey):
    self.true_monkey = true_monkey
    self.false_monkey = false_monkey

  def catch(self, item):
    self.items.append(item)

  def round(self):
    if self.true_monkey == None or self.false_monkey == None:
      raise Exception('Monkey has no friends to play with')
    for item in self.items:
      new_value = self.operation(item)
      new_value = math.floor(new_value / 3)
      self.items_inspected += 1

      if new_value % self.divisor == 0:
        self.true_monkey.catch(new_value)
      else:
        self.false_monkey.catch(new_value)

    self.items = []

#monkeys = [
#  Monkey([79,98], lambda old: old * 19, 23),
#  Monkey([54, 65, 75, 74], lambda old: old + 6, 19),
#  Monkey([79, 60, 97], lambda old: old * old, 13),
#  Monkey([74], lambda old: old + 3, 17)
#]

#monkeys[0].set_friends(monkeys[2], monkeys[3])
#monkeys[1].set_friends(monkeys[2], monkeys[0])
#monkeys[2].set_friends(monkeys[1], monkeys[3])
#monkeys[3].set_friends(monkeys[0], monkeys[1])

monkeys = [
  Monkey([63,84,80,83,84,53,88,72], lambda old: old * 11, 13),
  Monkey([67,56,92,88,84], lambda old: old + 4, 11),
  Monkey([52], lambda old: old * old, 2),
  Monkey([59,53,60,92,69,72], lambda old: old + 2, 5),
  Monkey([61,52,55,61], lambda old: old + 3, 7),
  Monkey([79,53], lambda old: old + 1, 3),
  Monkey([59,86,67,95,92,77,91], lambda old: old + 5, 19),
  Monkey([58,83,89], lambda old: old * 19, 17)
]

monkeys[0].set_friends(monkeys[4], monkeys[7])
monkeys[1].set_friends(monkeys[5], monkeys[3])
monkeys[2].set_friends(monkeys[3], monkeys[1])
monkeys[3].set_friends(monkeys[5], monkeys[6])
monkeys[4].set_friends(monkeys[7], monkeys[2])
monkeys[5].set_friends(monkeys[0], monkeys[6])
monkeys[6].set_friends(monkeys[4], monkeys[0])
monkeys[7].set_friends(monkeys[2], monkeys[1])

for round in range(0, 20):
  for i, monkey in enumerate(monkeys):
    monkey.round()

sorted_by_activity = sorted([monkey.items_inspected for monkey in monkeys], reverse=True)
monkey_business = sorted_by_activity[0] * sorted_by_activity[1]
print(monkey_business)