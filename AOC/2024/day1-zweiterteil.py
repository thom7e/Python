import re
from collections import Counter

with open("day-1.in") as input:
    inp = input.read().splitlines()

smallest_1 = []
smallest_2 = []
for sortiert in inp:
    smallest_1.append(sortiert.split(" ")[0])
    smallest_2.append(sortiert.split(" ")[3])

element_counts = Counter(smallest_2)

erg = 0
for x in range(len(smallest_1)):
    print(int(smallest_1[x]),int(element_counts[str(smallest_1[x])]))
    erg += int(smallest_1[x])*int(element_counts[str(smallest_1[x])])

print(erg)