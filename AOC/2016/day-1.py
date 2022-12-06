import numpy as np
import pandas as pd
import sys

np.set_printoptions(threshold=np.inf)


with open("day-1.in") as d:
    inp = d.read().split(", ")


x,y = 0,0
start = 0
visited = []
grid = np.zeros((600,600),dtype=str)
grid_x,grid_y = 300,300
#grid[grid_x, grid_y] = "x"

part_2 = []

for index,directions in enumerate(inp):
    dir = directions[0]
    amount = int(directions[1:])
    # Richtung
    if start == 360:
        #print("RESET 360")
        start = 0
    elif start == -360:
        #print("RESET -360")
        start = 0
    if dir == "L":
        start -= 90
    elif dir == "R":
        start += 90


    #print(start)
    if start == 0 or start == 360 or start == -360:
        y += amount
        for i in range(1,amount+1):
            visited.append((x,y+i-amount))
            #grid[grid_x, grid_y+y+i-amount] = "x"
            if (x,y+i-amount) in visited[:-1]:
                #print(f"BINGO",start,(x,y+i-amount),abs(0-(x))+abs(y+i-amount))
                part_2.append(abs(0-(x))+abs(y+i-amount))
    elif start == 90 or start == -270:
        x += amount
        for i in range(1,amount+1):
            visited.append((x+i-amount,y))
            #grid[grid_x+i-amount, grid_y] = "x"
            if (x+i-amount,y) in visited[:-1]:
                #print(f"BINGO",start,(x+i-amount,y),abs(0-(x+i-amount))+abs(y))
                part_2.append(abs(0-(x+i-amount))+abs(y))

        #print(visited)
    elif start == 180 or start == -180:
        amount = -amount
        y += amount
        for i in range(int(amount)+1,y-y+1):
            visited.append((x,y-i))
            #grid[grid_x, grid_y+y-i] = "x"
            if (x,y-i) in visited[:-1]:
                #print(f"BINGO",start,(x,y-i),abs(0-x)+abs(y-i))
                part_2.append(abs(0-x)+abs(y-i))
        #print(visited)
    elif start == 270 or start == -90:
        amount = -amount
        x += amount
        for i in range(int(amount)+1,x-x+1):
            visited.append((x-i,y))
            #grid[grid_x+x-i, grid_y] = "x"
            if (x-i,y) in visited[:-1]:
                #print(f"BINGO",(x-i,y),abs(0-(x-i))+abs(y))
                part_2.append(abs(0-(x-i))+abs(y))









for all_x in range(len(grid[0])):
    for all_y in range(len(grid[0])):
        grid[all_x,all_y] = "x"

for g_x,g_y in visited:
    grid[grid_x+g_x,grid_y+g_y] = "o"


#print(grid[250:350,250:350])
#w = np.where(grid == "x")
#print(w)
df = pd.DataFrame(grid)
#print(df)
df.to_csv("weg.csv")
print(f"PART I: {abs(0 - x) + abs(0 - y)}")
print(f"PART II: {part_2[0]}")
#print(abs(0-235)+abs(0-(-54)))



