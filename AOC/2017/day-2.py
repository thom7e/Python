with open("day-2.in") as inp:
    data = inp.read().splitlines()

## PART I
counter= 0
checker = 0

for line in data:
    row_ = "".join(line).replace("   "," ").split(" ")
    row = [int(x) for x in row_ if x.isdigit()]
    checker = max(row)-min(row)
    counter += checker

print("PART I",counter)

## PART II

counter = 0
checker = 0
for line in data:
    row_ = "".join(line).replace("   "," ").split(" ")
    row = [int(x) for x in row_ if x.isdigit()]
    for divi in row:
        for divisor in row:
            if divi == divisor:
                pass
            else:
                if divi%divisor == 0:
                    counter += divi/divisor
print("PART II",int(counter))