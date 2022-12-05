import numpy as np
import sys


with open("day-13.in") as file:
    f = file.read().strip().split("\n")

coordinates = []
for coo in f:
    coordinates.append((int(coo.split(",")[0]),int(coo.split(",")[1])))

max_x = []
max_y = []
for x,y in coordinates:
    max_x.append(x)
    max_y.append(y)


G = np.zeros(shape=(max(max_y)+1,max(max_x)+1))
for x,y in coordinates:
    G[y][x] = int(1)

def fold_y(G,y):
    G = np.add(G, np.flip(G, axis=0))
    return G[0:y,0:]

def fold_x(G,x):
    G = np.add(G, np.flip(G, axis=1))
    return G[0:,0:x]

foldings = []
foldings_in = ["fold along x=655","fold along y=447","fold along x=327","fold along y=223","fold along x=163","fold along y=111","fold along x=81","fold along y=55","fold along x=40","fold along y=27","fold along y=13","fold along y=6"]
for fold in foldings_in:
    foldings.append((fold.split(" ")[-1]).split("="))

def part_1(G, fold):
    G = fold_x(G,int(fold))
    counter = 0
    #print(G[0][0])
    for i in range(len(G)):
        for j in range(len(G[0])):
            if G[i][j] > 0:
                counter += 1
    return counter

print(G)
print(f"PART I: {part_1(G,655)}")

########### PART II ##############
for x,y in foldings:
    if x == "x":
        G = fold_x(G, int(y))

    elif x == "y":
        G = fold_y(G, int(y))
#print(len(G))
#print(len(G[0]))

for i in range(len(G)):
    for j in range(len(G[0])):
        if G[i][j] > 0:

            G[i][j] = "NaN"


print(G[0:6,0:5])
print("\n\n")
print(G[0:6,5:10])
print("\n\n")
print(G[0:6,10:15])
print("\n\n")
print(G[0:6,15:20])
print("\n\n")
print(G[0:6,20:25])
print("\n\n")
print(G[0:6,25:30])
print("\n\n")
print(G[0:6,30:35])
print("\n\n")
print(G[0:6,35:40])


