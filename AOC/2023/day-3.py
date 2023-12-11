import string
import numpy as np
import re

with open("day-3.in") as f:
    inp = f.read().splitlines()

grid = np.array([list(line) for line in inp])
print(grid)

print(grid[2,1:4])

# Erstellen einer Menge aller druckbaren Zeichen
all_characters = set(string.printable)

# Entfernen von Buchstaben und Ziffern
special_characters = all_characters - set(string.ascii_letters) - set(string.digits)

# Umwandlung der Menge in einen String
special_characters_str = ''.join(special_characters)
special_characters_str = special_characters_str.replace(".", "")
check ="['599', '4']"
print(int(str(re.findall(r'\d{2,}',check)).replace("['","").replace("']","")))

def check_neighbours(i,j,grid):
    runde= [(0,1),(1,0),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]
    zahlen = []
    rechtsrum = [(-1,1),(-1,0),(-1,1)]
    linksrum = [(-1,1),(0,-1),(1,-1)]
    oben_und_unten =[(-1,0),(1,0)]
    for x,y in runde:
        if grid[i+x,j+y].isdigit():
            #print(grid[i+x,j+y],"bei Pos", i+x, j+y)
            number = grid[(i+x),(j+y-2):(j+y+3)]
            number = "".join([x for x in number ])
            number_ = str(re.findall(r"\d+", number))
            if len(number_) <= 7:
                zahlen.append(int(number_.replace("['","").replace("']","")))
            else:
                #print(number_)
                if (x,y) in rechtsrum:
                    zahlen.append(int(number_.split(",")[-1].split(".")[-1].replace("']","").replace("'","")))
                    print("rechtsrum")
                    print(int(number_.split(",")[0].replace("['", "").replace("'", "")))
                if (x,y) in linksrum:
                    print("linksrum")
                    zahlen.append(int(number_.split(",")[0].split(".")[0].replace("['","").replace("'","")))
                    print(int(number_.split(",")[0].replace("['", "").replace("'", "")))
                if (x,y) in oben_und_unten:
                    print("HEEEEEEEEEEY",number_)
                    if number[1] == ".":
                        print(". ist auf 1")
                        zahlen.append(int(number_.split(",")[1].replace("']","").replace("'","")))
                    if number[-2] == ".":
                        print(". ist auf -2")
                        print(int(number_.split(",")[0].replace("['","").replace("'","")))
                        zahlen.append(int(number_.split(",")[0].replace("['","").replace("'","")))


    print(set(zahlen))
    return set(zahlen)

summe = []
for i, row in enumerate(grid):
    for j, element in enumerate(row):
        #print(element)
        if element in special_characters_str:
            print(f"Element an Position ({i}, {j}): {element}")
            summe.extend(check_neighbours(i,j,grid))


print(sum(summe))


############
from collections import defaultdict

D = open("day-3.in").read().strip()
lines = D.split('\n')
G = [[c for c in line] for line in lines]
R = len(G)
C = len(G[0])

p1 = 0
nums = defaultdict(list)
for r in range(len(G)):
  gears = set() # positions of '*' characters next to the current number
  n = 0
  has_part = False
  for c in range(len(G[r])+1):
    if c<C and G[r][c].isdigit():
      n = n*10+int(G[r][c])
      for rr in [-1,0,1]:
        for cc in [-1,0,1]:
          if 0<=r+rr<R and 0<=c+cc<C:
            ch = G[r+rr][c+cc]
            if not ch.isdigit() and ch != '.':
              has_part = True
            if ch=='*':
              gears.add((r+rr, c+cc))
    elif n>0:
      for gear in gears:
        nums[gear].append(n)
      if has_part:
        p1 += n
      n = 0
      has_part = False
      gears = set()

print(p1)
p2 = 0
for k,v in nums.items():
  if len(v)==2:
    p2 += v[0]*v[1]
print(p2)

