with open("day2.input") as input:
    lines = input.read().splitlines()
#print(lines)
## PART I
from collections import Counter

counter_2 = 0
counter_3 = 0

for line in lines:
    letters = line.strip()
    if 2 in Counter(letters).values():
        counter_2 += 1
    if 3 in Counter(letters).values():
        counter_3 += 1
    #print(Counter(letters).values())

print(f"PART I: {counter_2 * counter_3}")

## PART II

with open("day2-2-trial.input") as input:
    lines = input.read().splitlines()

#print(sorted(lines))
for line in lines:
    for index, letter in enumerate(sorted(list(line))):
        print(index,letter)


#for line in lines:
#    for index, letter in list(enumerate(line.strip())):
#        print(index,letter)
