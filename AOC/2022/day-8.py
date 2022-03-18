import re
with open("day-8.in", "r") as file:
    x = file.read().split("\n")

combinations = []
for y in x:
    combinations.append(y.split("| "))
outputs = []
inputs = []
for output in range(len(combinations)):
    outputs.append(combinations[output][1])
for input_ in range(len(combinations)):
    inputs.append(combinations[input_][0])

#print(outputs)
inputsss = []
for x in inputs:
    new = ["".join(sorted(x)) for x in x.split(" ")]
    inputsss.append(new)

differents = []
counter = 0
outputsss = []


for y in outputs:
    new_ = ["".join(sorted(x)) for x in y.split(" ")]
    outputsss.append(new_)
#print(inputsss[0])
#print(outputsss[0])
counter_ = 0
for xx in outputsss:
    for yy in xx:
        if len(yy) == 2 or len(yy) == 4 or len(yy) == 3 or len(yy) == 7:
            counter_ += 1
print(counter_)


print("___________________________________________")
checks = []

for part_ones in inputsss:
    for numbers in part_ones:
        if len(numbers) == 2 and "".join(sorted(numbers)) == "ab":



    print("next")

#print(checks, len(checks))


#print(len(set(differents)))

