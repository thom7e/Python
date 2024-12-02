import re

with open("day-1.in") as input:
    inp = input.read().splitlines()

smallest_1 = []
smallest_2 = []
for sortiert in inp:
    smallest_1.append(sortiert.split(" ")[0])
    smallest_2.append(sortiert.split(" ")[3])

smallest_1= sorted(smallest_1)
smallest_2= sorted(smallest_2)

erg = 0
for x in range(len(smallest_1)):
    #print(smallest_2[x],smallest_1[x])
    erg += abs(int(smallest_2[x])-int(smallest_1[x]))

print(erg)