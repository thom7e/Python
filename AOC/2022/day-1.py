with open("day-1.in") as f:
    calories = f.read().splitlines()

total = 0
all = []
for x in range(len(calories)):
    if calories[x] == "":
        all.append(total)
        total = 0
        continue
    else:
        total += int(calories[x])

## PART I
print(f"PART I {max(all)}")
## PART II
all.sort()
print(f"PART II {all[-3:]} {sum(all[-3:])}")
