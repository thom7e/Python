from collections import Counter
string_ = "BNSOSBBKPCSCPKPOPNNK"
start = []
for s in string_:
    start.append(str(s))

new= []
with open("day-14.in") as file:
    x = file.read().strip().split("\n")

pairs = []
for pairs_ in x:
    pairs.append(pairs_.split(" -> "))

def insertion(start,pairs):
    new = []
    for search in range(len(start)-1):
         for insertion in range(len(pairs)):
             if pairs[insertion][0] == str(f"{start[search]+start[search+1]}"):
                 new.append(start[search])
                 new.append(pairs[insertion][1])
             else:
                 pass

    new.append(start[-1])
    return new

for steps in range(10):
    start = insertion(start,pairs)
    print(max(Counter(start).values())-min(Counter(start).values()))


