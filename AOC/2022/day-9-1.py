import numpy as np
with open("day-9.in") as d:
    inp = d.read().splitlines()


x_head,y_head = 0,0
x_tail,y_tail = 0,0
start = 0


#grid_x,grid_y = 6,6
#grid[grid_x, grid_y] = "x"

H = (x_head,y_head)
T = (x_tail,y_tail)
visited_head = []
visited_tail = []

for index,directions in enumerate(inp):
    dir = directions[0]
    amount = int(directions[1:])

    #print(x_check, y_check)


    # Richtung
    if dir == "R":
        #x_head += amount
        for step_head in range(1,amount+1):

            x_tail = x_head
            print(dir, x_tail, y_tail, x_head, y_head)
            x_head += 1


            visited_head.append((x_head, y_head))
            visited_tail.append((x_tail, y_tail))





    elif dir == "U":

        for step_head in range(1,amount+1):


            y_head += 1
            print("vorher",dir, x_tail, y_tail, x_head, y_head)
            if y_tail < y_head:
                x_tail += 1
                y_tail += 1

            elif y_tail > y_head:
                x_tail -= 1
                y_tail -= 1

            print("nacher",dir, x_tail, y_tail, x_head, y_head)


            visited_head.append((x_head, y_head))








    ### NEGATIVE
    elif dir == "L":
        for step_head in range(1, amount + 1):

            x_head -= 1
            x_tail = x_head
            visited_head.append((x_head, y_head))

            visited_tail.append((x_tail, y_tail))



    elif dir == "D":
        for step_head in range(1, amount + 1):

            y_head -= 1
            y_tail = y_head
            visited_head.append((x_head,y_head))
            visited_tail.append((x_tail, y_tail))





print(visited_head)
print(visited_tail)







