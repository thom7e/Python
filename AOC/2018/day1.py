with open("day1.input") as input:
    lines = input.read().splitlines()
#print(lines)
start = 0
duplicates = []
## PART I
for change in lines:
    start += int(change)

print(f"PART I : {start}")
## PART II
start = 0
repetitions = [0]
i = 0

while True:
    start += int(lines[i])
    repetitions.append(start)
    i += 1
    if i == len(lines):
        i = 0
    if repetitions.count(start) > 1:
        print(f"PART II : {start}")
        break



