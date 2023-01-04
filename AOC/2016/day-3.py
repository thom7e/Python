import re

with open("day-3.in") as d:
    inp = d.read().splitlines()

triangles = [x.split(" ") for x in inp]

triangle_right = []
counter = 0
for tri in triangles:

    sides = [x for x in tri if x.isdigit()]
    #print(sides)
    side_1,side_2,side_3 = int(sides[0]),int(sides[1]),int(sides[2])


    # First
    if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1:
        triangle_right.append((side_1, side_2, side_3))

    counter += 1


print("P1", len(triangle_right))

def sides(triangels):
    sides_ = []
    for y in triangels:
        sides_.append([x for x in y if x.isdigit()])
    dreier = []
    col = 0
    row = 0
    while True:
        dreier.append((sides_[col][row],sides_[col+1][row],sides_[col+2][row]))
        col += 3
        if row == 2 and col == len(sides_):
            break
        if col == len(sides_):
            row += 1
            col = 0


    return dreier


triangle_right = []
for tri in sides(triangles):

    side_1,side_2,side_3 = int(tri[0]),int(tri[1]),int(tri[2])


    # First
    if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1:
        triangle_right.append((side_1, side_2, side_3))

print("P2",len(triangle_right))



