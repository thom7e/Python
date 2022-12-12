import numpy as np
import pandas as pd
import sys

#np.set_printoptions(threshold=np.inf)


with open("day-9.in") as d:
    inp = d.read().splitlines()


x_head,y_head = 0,0
x_tail,y_tail = 0,0
start = 0

grid = np.zeros((20,20),dtype=str)
#grid_x,grid_y = 300,300
#grid[grid_x, grid_y] = "x"

s = (0,0)
H = (x_head,y_head)
T = (x_tail,y_tail)
visited = [s]
for index,directions in enumerate(inp):
    dir = directions[0]
    amount = int(directions[1:])
    print(f"HEAD {x_head, y_head}, TAIL {x_tail, y_tail}")
    # Richtung

    if dir == "R":
        #print(dir, (x_head, y_head), (x_tail, y_tail))
        x_check, y_check = x_head, y_head
        y_tail = y_head
        for k in range(1,amount+1):
            x_head += 1
            if not k < 1 and not k == amount:
                x_tail += 1
            print((x_tail, y_tail), (x_check, y_check))
            if not (x_tail, y_tail) == (x_check, y_check):
                print(dir, x_tail, y_tail, x_head, y_head)


    elif dir == "U":
        #print(dir, (x_head, y_head), (x_tail, y_tail))
        x_check, y_check = x_head, y_head
        x_tail = x_head
        #x_tail = x_head
        for k in range(1,amount+1):
            y_head += 1
            if not k < 1 and not k == amount:
                y_tail += 1
            if not (x_tail, y_tail) == (x_check, y_check):
                print(dir, x_tail, y_tail, x_head, y_head)


    ### NEGATIVE

    elif dir == "L":
        #print(dir, (x_head, y_head), (x_tail, y_tail))
        x_check, y_check = x_head, y_head
        y_tail = y_head
        for k in range(1,amount+1):
            x_head -= 1
            if not k < 1 and not k == amount:
                x_tail -= 1
            if not (x_tail, y_tail) == (x_check, y_check):
                print(dir, x_tail, y_tail, x_head, y_head)



            # print((x_head, y_head), (x_tail, y_tail))

    elif dir == "D":
        #print(dir,(x_head,y_head),(x_tail,y_tail))
        x_check,y_check = x_head,y_head
        #x_tail = x_head
        x_tail = x_head
        for k in range(1,amount+1):
            y_head -= 1
            if not k < 1 and not k == amount:
                y_tail -= 1

            if not (x_tail,y_tail) == (x_check,y_check):
                print(dir, x_tail, y_tail, x_head, y_head)






print(visited)
print(len(set(visited)))

print([x for x in range(1,1)])