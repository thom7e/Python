"""Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3"""

import re

with open("day-11.in") as d:
  data = d.read().strip()
monkeys = data.split("Monkey ")

#0
starting_items_parsed_0 = monkeys[1].split("Starting Items")[0].split("\n")[1]#.split(" ")
starting_items_0 = [int(x) for x in re.findall("[0-9][0-9]",starting_items_parsed_0)]
#1
starting_items_parsed_1 = monkeys[2].split("Starting Items")[0].split("\n")[1]#.split(" ")
starting_items_1 = [int(x) for x in re.findall("[0-9][0-9]",starting_items_parsed_1)]
#2
starting_items_parsed_2 = monkeys[3].split("Starting Items")[0].split("\n")[1]#.split(" ")
starting_items_2 = [int(x) for x in re.findall("[0-9][0-9]",starting_items_parsed_2)]
#3
starting_items_parsed_3 = monkeys[4].split("Starting Items")[0].split("\n")[1]#.split(" ")
starting_items_3 = [int(x) for x in re.findall("[0-9][0-9]",starting_items_parsed_3)]
#4
starting_items_parsed_4 = monkeys[5].split("Starting Items")[0].split("\n")[1]#.split(" ")
starting_items_4 = [int(x) for x in re.findall("[0-9][0-9]",starting_items_parsed_4)]
#5
starting_items_parsed_5 = monkeys[6].split("Starting Items")[0].split("\n")[1]#.split(" ")
starting_items_5 = [int(x) for x in re.findall("[0-9][0-9]",starting_items_parsed_5)]
#6
starting_items_parsed_6 = monkeys[7].split("Starting Items")[0].split("\n")[1]#.split(" ")
starting_items_6 = [int(x) for x in re.findall("[0-9][0-9]",starting_items_parsed_6)]
#7
starting_items_parsed_7 = monkeys[8].split("Starting Items")[0].split("\n")[1]#.split(" ")
starting_items_7 = [int(x) for x in re.findall("[0-9][0-9]",starting_items_parsed_7)]
#print(starting_items_0,starting_items_1,starting_items_2,starting_items_3)

counter_monkey_0 = 0
counter_monkey_1 = 0
counter_monkey_2 = 0
counter_monkey_3 = 0
counter_monkey_4 = 0
counter_monkey_5 = 0
counter_monkey_6 = 0
counter_monkey_7 = 0

for round in range(0,20):
  for monkey in range(1,len(monkeys)):

    monkey_nr = monkey-1
    #starting_items_parsed = monkeys[monkey].split("Starting Items")[0].split("\n")[1]#.split(" ")
    #starting_items = re.findall("[0-9][0-9]",starting_items_parsed)

    operation_parsed = monkeys[monkey].split("Operation:")[1].split("new = old ")[1].split("\n")[0].split(" ")
    operator = operation_parsed[0]
    amount = operation_parsed[1]

    divisor_parsed = monkeys[monkey].split("divisible by ")[1].split(" ")[0]
    divisor = int(divisor_parsed)
    test_true_parsed = monkeys[monkey].split("If")[1].split("\n")[0].split(" ")[-1]
    test_false_parsed = monkeys[monkey].split("If")[2].split("\n")[0].split(" ")[-1]
    ##print(monkey_nr, starting_items, operator, amount,divisor,test_true_parsed,test_false_parsed)
    ##print("monkey nr",monkey)
    if monkey == 1:
      alt = len(starting_items_0)
      for item in starting_items_0:
        counter_monkey_0 += 1
        #print("monkey 0", item)
        item = int(item)
        if amount != "old":
          amount = int(amount)

          if operator == "*":
            worry_level = item * amount
          elif operator == "+":
            worry_level = item + amount
        if amount == "old":
          if operator == "*":
            worry_level = item * item
          elif operator == "+":
            worry_level = item + item
        ##print(worry_level)
        worry_level = int(worry_level/3)
        ##print(worry_level,"divided by 3")
        if worry_level % divisor == 0:
          if test_true_parsed == "0":
            starting_items_0.append(worry_level)
          elif test_true_parsed == "1":
            starting_items_1.append(worry_level)
          elif test_true_parsed == "2":
            starting_items_2.append(worry_level)
          elif test_true_parsed == "3":
            starting_items_3.append(worry_level)
          elif test_true_parsed == "4":
            starting_items_4.append(worry_level)
          elif test_true_parsed == "5":
            starting_items_5.append(worry_level)
          elif test_true_parsed == "6":
            starting_items_6.append(worry_level)
          elif test_true_parsed == "7":
            starting_items_7.append(worry_level)
          ##print(f"item {worry_level} throw to {test_true_parsed}")
        if worry_level % divisor != 0:
          if test_false_parsed == "0":
            starting_items_0.append(worry_level)
          elif test_false_parsed == "1":
            starting_items_1.append(worry_level)
          elif test_false_parsed == "2":
            starting_items_2.append(worry_level)
          elif test_false_parsed == "3":
            starting_items_3.append(worry_level)
          elif test_false_parsed == "4":
            starting_items_4.append(worry_level)
          elif test_false_parsed == "5":
            starting_items_5.append(worry_level)
          elif test_false_parsed == "6":
            starting_items_6.append(worry_level)
          elif test_false_parsed == "7":
            starting_items_7.append(worry_level)
          ##print(f"item {worry_level} throw to {test_false_parsed}")
        ##print(starting_items_0,str(item))
      starting_items_0 = starting_items_0[alt:] ## ##0



    elif monkey == 2:#
      alt = len(starting_items_1)
      for item in starting_items_1:
        counter_monkey_1 += 1
        ##print("monkey 2", item)
        item = int(item)
        if amount != "old":
          amount = int(amount)

          if operator == "*":
            worry_level = item * amount
          elif operator == "+":
            worry_level = item + amount
        if amount == "old":
          if operator == "*":
            worry_level = item * item
          elif operator == "+":
            worry_level = item + item
        # #print(worry_level)
        worry_level = int(worry_level / 3)
        # #print(worry_level,"divided by 3")
        if worry_level % divisor == 0:
          if test_true_parsed == "0":
            starting_items_0.append(worry_level)
          elif test_true_parsed == "1":
            starting_items_1.append(worry_level)
          elif test_true_parsed == "2":
            starting_items_2.append(worry_level)
          elif test_true_parsed == "3":
            starting_items_3.append(worry_level)
          elif test_true_parsed == "4":
            starting_items_4.append(worry_level)
          elif test_true_parsed == "5":
            starting_items_5.append(worry_level)
          elif test_true_parsed == "6":
            starting_items_6.append(worry_level)
          elif test_true_parsed == "7":
            starting_items_7.append(worry_level)

          # #print(f"item {worry_level} throw to {test_true_parsed}")
        else:
          if test_false_parsed == "0":
            starting_items_0.append(worry_level)
          elif test_false_parsed == "1":
            starting_items_1.append(worry_level)
          elif test_false_parsed == "2":
            starting_items_2.append(worry_level)
          elif test_false_parsed == "3":
            starting_items_3.append(worry_level)
          elif test_false_parsed == "4":
            starting_items_4.append(worry_level)
          elif test_false_parsed == "5":
            starting_items_5.append(worry_level)
          elif test_false_parsed == "6":
            starting_items_6.append(worry_level)
          elif test_false_parsed == "7":
            starting_items_7.append(worry_level)
      starting_items_1 = starting_items_1[alt:]
          # #print(f"item {worry_level} throw to {test_false_parsed}")
    elif monkey == 3:

      alt = len(starting_items_2)
      for item in starting_items_2:
        counter_monkey_2 += 1
        #print("monkey 2", item)
        item = int(item)
        if amount != "old":
          amount = int(amount)

          if operator == "*":
            worry_level = item * amount
          elif operator == "+":
            worry_level = item + amount
        if amount == "old":
          if operator == "*":
            worry_level = item * item
          elif operator == "+":
            worry_level = item + item
        # #print(worry_level)
        worry_level = int(worry_level / 3)
        # #print(worry_level,"divided by 3")
        if worry_level % divisor == 0:
          if test_true_parsed == "0":
            starting_items_0.append(worry_level)
          elif test_true_parsed == "1":
            starting_items_1.append(worry_level)
          elif test_true_parsed == "2":
            starting_items_2.append(worry_level)
          elif test_true_parsed == "3":
            starting_items_3.append(worry_level)
          elif test_true_parsed == "4":
            starting_items_4.append(worry_level)
          elif test_true_parsed == "5":
            starting_items_5.append(worry_level)
          elif test_true_parsed == "6":
            starting_items_6.append(worry_level)
          elif test_true_parsed == "7":
            starting_items_7.append(worry_level)
          # #print(f"item {worry_level} throw to {test_true_parsed}")
        else:
          if test_false_parsed == "0":
            starting_items_0.append(worry_level)
          elif test_false_parsed == "1":
            starting_items_1.append(worry_level)
          elif test_false_parsed == "2":
            starting_items_2.append(worry_level)
          elif test_false_parsed == "3":
            starting_items_3.append(worry_level)
          elif test_false_parsed == "4":
            starting_items_4.append(worry_level)
          elif test_false_parsed == "5":
            starting_items_5.append(worry_level)
          elif test_false_parsed == "6":
            starting_items_6.append(worry_level)
          elif test_false_parsed == "7":
            starting_items_7.append(worry_level)

      starting_items_2 = starting_items_2[alt:]
          # #print(f"item {worry_level} throw to {test_false_parsed}")
    elif monkey == 4:
      alt = len(starting_items_3)
      for item in starting_items_3:
        counter_monkey_3 += 1
        #print("monkey 3", item)
        item = int(item)
        if amount != "old":
          amount = int(amount)

          if operator == "*":
            worry_level = item * amount
          elif operator == "+":
            worry_level = item + amount
        if amount == "old":
          if operator == "*":
            worry_level = item * item
          elif operator == "+":
            worry_level = item + item
        # #print(worry_level)
        worry_level = int(worry_level / 3)
        # #print(worry_level,"divided by 3")
        if worry_level % divisor == 0:
          if test_true_parsed == "0":
            starting_items_0.append(worry_level)
          elif test_true_parsed == "1":
            starting_items_1.append(worry_level)
          elif test_true_parsed == "2":
            starting_items_2.append(worry_level)
          elif test_true_parsed == "3":
            starting_items_3.append(worry_level)
          elif test_true_parsed == "4":
            starting_items_4.append(worry_level)
          elif test_true_parsed == "5":
            starting_items_5.append(worry_level)
          elif test_true_parsed == "6":
            starting_items_6.append(worry_level)
          elif test_true_parsed == "7":
            starting_items_7.append(worry_level)
          # #print(f"item {worry_level} throw to {test_true_parsed}")
        else:
          if test_false_parsed == "0":
            starting_items_0.append(worry_level)
          elif test_false_parsed == "1":
            starting_items_1.append(worry_level)
          elif test_false_parsed == "2":
            starting_items_2.append(worry_level)
          elif test_false_parsed == "3":
            starting_items_3.append(worry_level)
          elif test_false_parsed == "4":
            starting_items_4.append(worry_level)
          elif test_false_parsed == "5":
            starting_items_5.append(worry_level)
          elif test_false_parsed == "6":
            starting_items_6.append(worry_level)
          elif test_false_parsed == "7":
            starting_items_7.append(worry_level)
      starting_items_3 = starting_items_3[alt:]

         # #print(f"item {worry_level} throw to {test_false_parsed}")
    elif monkey == 5:
      alt = len(starting_items_4)
      for item in starting_items_4:
        counter_monkey_4 += 1
        #print("monkey 3", item)
        item = int(item)
        if amount != "old":
          amount = int(amount)

          if operator == "*":
            worry_level = item * amount
          elif operator == "+":
            worry_level = item + amount
        if amount == "old":
          if operator == "*":
            worry_level = item * item
          elif operator == "+":
            worry_level = item + item
        # #print(worry_level)
        worry_level = int(worry_level / 3)
        # #print(worry_level,"divided by 3")
        if worry_level % divisor == 0:
          if test_true_parsed == "0":
            starting_items_0.append(worry_level)
          elif test_true_parsed == "1":
            starting_items_1.append(worry_level)
          elif test_true_parsed == "2":
            starting_items_2.append(worry_level)
          elif test_true_parsed == "3":
            starting_items_3.append(worry_level)
          elif test_true_parsed == "4":
            starting_items_4.append(worry_level)
          elif test_true_parsed == "5":
            starting_items_5.append(worry_level)
          elif test_true_parsed == "6":
            starting_items_6.append(worry_level)
          elif test_true_parsed == "7":
            starting_items_7.append(worry_level)
          # #print(f"item {worry_level} throw to {test_true_parsed}")
        else:
          if test_false_parsed == "0":
            starting_items_0.append(worry_level)
          elif test_false_parsed == "1":
            starting_items_1.append(worry_level)
          elif test_false_parsed == "2":
            starting_items_2.append(worry_level)
          elif test_false_parsed == "3":
            starting_items_3.append(worry_level)
          elif test_false_parsed == "4":
            starting_items_4.append(worry_level)
          elif test_false_parsed == "5":
            starting_items_5.append(worry_level)
          elif test_false_parsed == "6":
            starting_items_6.append(worry_level)
          elif test_false_parsed == "7":
            starting_items_7.append(worry_level)
      starting_items_4 = starting_items_4[alt:]

         # #print(f"item {worry_level} throw to {test_false_parsed}")
    elif monkey == 6:
      alt = len(starting_items_5)
      for item in starting_items_5:
        counter_monkey_5 += 1
        #print("monkey 3", item)
        item = int(item)
        if amount != "old":
          amount = int(amount)

          if operator == "*":
            worry_level = item * amount
          elif operator == "+":
            worry_level = item + amount
        if amount == "old":
          if operator == "*":
            worry_level = item * item
          elif operator == "+":
            worry_level = item + item
        # #print(worry_level)
        worry_level = int(worry_level / 3)
        # #print(worry_level,"divided by 3")
        if worry_level % divisor == 0:
          if test_true_parsed == "0":
            starting_items_0.append(worry_level)
          elif test_true_parsed == "1":
            starting_items_1.append(worry_level)
          elif test_true_parsed == "2":
            starting_items_2.append(worry_level)
          elif test_true_parsed == "3":
            starting_items_3.append(worry_level)
          elif test_true_parsed == "4":
            starting_items_4.append(worry_level)
          elif test_true_parsed == "5":
            starting_items_5.append(worry_level)
          elif test_true_parsed == "6":
            starting_items_6.append(worry_level)
          elif test_true_parsed == "7":
            starting_items_7.append(worry_level)
          # #print(f"item {worry_level} throw to {test_true_parsed}")
        else:
          if test_false_parsed == "0":
            starting_items_0.append(worry_level)
          elif test_false_parsed == "1":
            starting_items_1.append(worry_level)
          elif test_false_parsed == "2":
            starting_items_2.append(worry_level)
          elif test_false_parsed == "3":
            starting_items_3.append(worry_level)
          elif test_false_parsed == "4":
            starting_items_4.append(worry_level)
          elif test_false_parsed == "5":
            starting_items_5.append(worry_level)
          elif test_false_parsed == "6":
            starting_items_6.append(worry_level)
          elif test_false_parsed == "7":
            starting_items_7.append(worry_level)
      starting_items_5 = starting_items_5[alt:]

         # #print(f"item {worry_level} throw to {test_false_parsed}")
    elif monkey == 7:
      alt = len(starting_items_6)
      for item in starting_items_6:
        counter_monkey_6 += 1
        #print("monkey 3", item)
        item = int(item)
        if amount != "old":
          amount = int(amount)

          if operator == "*":
            worry_level = item * amount
          elif operator == "+":
            worry_level = item + amount
        if amount == "old":
          if operator == "*":
            worry_level = item * item
          elif operator == "+":
            worry_level = item + item
        # #print(worry_level)
        worry_level = int(worry_level / 3)
        # #print(worry_level,"divided by 3")
        if worry_level % divisor == 0:
          if test_true_parsed == "0":
            starting_items_0.append(worry_level)
          elif test_true_parsed == "1":
            starting_items_1.append(worry_level)
          elif test_true_parsed == "2":
            starting_items_2.append(worry_level)
          elif test_true_parsed == "3":
            starting_items_3.append(worry_level)
          elif test_true_parsed == "4":
            starting_items_4.append(worry_level)
          elif test_true_parsed == "5":
            starting_items_5.append(worry_level)
          elif test_true_parsed == "6":
            starting_items_6.append(worry_level)
          elif test_true_parsed == "7":
            starting_items_7.append(worry_level)
          # #print(f"item {worry_level} throw to {test_true_parsed}")
        else:
          if test_false_parsed == "0":
            starting_items_0.append(worry_level)
          elif test_false_parsed == "1":
            starting_items_1.append(worry_level)
          elif test_false_parsed == "2":
            starting_items_2.append(worry_level)
          elif test_false_parsed == "3":
            starting_items_3.append(worry_level)
          elif test_false_parsed == "4":
            starting_items_4.append(worry_level)
          elif test_false_parsed == "5":
            starting_items_5.append(worry_level)
          elif test_false_parsed == "6":
            starting_items_6.append(worry_level)
          elif test_false_parsed == "7":
            starting_items_7.append(worry_level)
      starting_items_6 = starting_items_6[alt:]

         # #print(f"item {worry_level} throw to {test_false_parsed}")
    elif monkey == 8:
      alt = len(starting_items_7)
      for item in starting_items_7:
        counter_monkey_7 += 1
        #print("monkey 3", item)
        item = int(item)
        if amount != "old":
          amount = int(amount)

          if operator == "*":
            worry_level = item * amount
          elif operator == "+":
            worry_level = item + amount
        if amount == "old":
          if operator == "*":
            worry_level = item * item
          elif operator == "+":
            worry_level = item + item
        # #print(worry_level)
        worry_level = int(worry_level / 3)
        # #print(worry_level,"divided by 3")
        if worry_level % divisor == 0:
          if test_true_parsed == "0":
            starting_items_0.append(worry_level)
          elif test_true_parsed == "1":
            starting_items_1.append(worry_level)
          elif test_true_parsed == "2":
            starting_items_2.append(worry_level)
          elif test_true_parsed == "3":
            starting_items_3.append(worry_level)
          elif test_true_parsed == "4":
            starting_items_4.append(worry_level)
          elif test_true_parsed == "5":
            starting_items_5.append(worry_level)
          elif test_true_parsed == "6":
            starting_items_6.append(worry_level)
          elif test_true_parsed == "7":
            starting_items_7.append(worry_level)
          # #print(f"item {worry_level} throw to {test_true_parsed}")
        else:
          if test_false_parsed == "0":
            starting_items_0.append(worry_level)
          elif test_false_parsed == "1":
            starting_items_1.append(worry_level)
          elif test_false_parsed == "2":
            starting_items_2.append(worry_level)
          elif test_false_parsed == "3":
            starting_items_3.append(worry_level)
          elif test_false_parsed == "4":
            starting_items_4.append(worry_level)
          elif test_false_parsed == "5":
            starting_items_5.append(worry_level)
          elif test_false_parsed == "6":
            starting_items_6.append(worry_level)
          elif test_false_parsed == "7":
            starting_items_7.append(worry_level)
      starting_items_7 = starting_items_7[alt:]

         # #print(f"item {worry_level} throw to {test_false_parsed}")


print(starting_items_0,starting_items_1,starting_items_2,starting_items_3,starting_items_4,starting_items_5,starting_items_6,starting_items_7)
most_monkeys = sorted([int(counter_monkey_0),int(counter_monkey_1),int(counter_monkey_2),int(counter_monkey_3),int(counter_monkey_4),int(counter_monkey_5),int(counter_monkey_6),int(counter_monkey_7)])[-2:]
print(most_monkeys)
print(f"PART I:", most_monkeys[0]*most_monkeys[1])