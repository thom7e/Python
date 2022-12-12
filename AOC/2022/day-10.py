import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

with open("day-10.in") as d:
    inp = d.read().splitlines()

x = 1
cycle = 1
counter = 0
cycle_1 = 20
cycle_2 = 60
cycle_3 = 100
cycle_4 = 140
cycle_5 = 180
cycle_6 = 220
inde = 0
werte = []
while True:
    counter += 1
    cycle += 1
    werte.append((cycle,x))
    for index,cmd in enumerate(inp):
        if cmd.split(" ")[0] == "noop":

            inp.pop(0)
            break
        else:
            #print(int(cmd.split(" ")[1]))
            x += int(cmd.split(" ")[1])

            cycle += 1
            inp.pop(0)
            werte.append((cycle,x))
            break


    #print("CYCLE", cycle,counter)
    #print("x ist :", x)


    if cycle == 240:
        break

summe = []
for k in werte:
    #print(k[1],k[0],k)
    if k[0] == cycle_1 or k[0] == cycle_2 or k[0] == cycle_3 or k[0] ==cycle_4 or k[0]== cycle_5 or k[0] == cycle_6:
        summe.append(k[1]*k[0])
print("P1 ",sum(summe))


grid = np.zeros((7,42),dtype=str)
print(grid)
#print(werte)
row = 0
col = 1
l=0
for i in werte:

    sprite = [i[1]-1+l,i[1]+l,i[1]+1+l]
    crt = i[0]-1
    cycle = i[0]
    #print("cycle:",i[0],"CRT",i[0]-1,"sprite",sprite)
    #print(row,col)
    if crt in sprite:
        print(row,col,"#")
        grid[row,col] = "#"
    else:
        grid[row, col] = "."
        print(row, col, ".")
    col += 1
    if int(cycle) % 40 == 0:
        row += 1
        col = 0
        l += 40
    #(row)


print(grid[0,0])
print(grid[1,0])
#l = 39%39
#print(l)
print(grid[0:6,0:5])
print("\n\n")
print(grid[0:6,5:10])
print("\n\n")
print(grid[0:6,10:15])
print("\n\n")
print(grid[0:6,15:20])
print("\n\n")
print(grid[0:6,20:25])
print("\n\n")
print(grid[0:6,25:30])
print("\n\n")
print(grid[0:6,30:35])
print("\n\n")
print(grid[0:6,35:40])
print("\n\n")