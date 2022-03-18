import numpy as np
with open("day25.in") as f:
    input_ = f.read().split()




def add_input(inputfile):
    G = np.empty(shape=(len(input_), len(input_[0])), dtype=str)
    row = 0
    col = 0
    for x in input_:
        for y in x:
            if row == len(input_[0]):
                row = 0
                col += 1
            elif row == len(input_[0]) and col == len(input_):
                return G

            G[col][row] = y
            row +=1
    return G

def for_move(field):
    field_ = field.copy()
    C = len(field)
    R = len(field[0])
    for cc in range(C):
        for rr in range(R):
            if field_[cc][rr] != field[cc][rr]:
                continue
            if field[cc][rr] == ">":
                if rr < R - 1:
                    if field[cc][rr + 1] == ".":
                        field[cc][rr] = "."
                        field[cc][rr + 1] = ">"

                elif rr == R - 1:
                    if field[cc][0] == ".":
                        field[cc][rr] = "."
                        field[cc][0] = ">"

    for cc in range(C):
        for rr in range(R):
            if field_[cc][rr] != field[cc][rr]:
                continue

            if field[cc][rr] == "v":
                if cc < C-1:
                    if field[cc + 1][rr] == ".":
                        field[cc][rr] = "."
                        field[cc + 1][rr] = "v"
                elif cc == C-1:
                    if field[0][rr] == ".":
                        field[cc][rr] = "."
                        field[0][rr] = "v"

    return field



def move(field):
    field_ = field.copy()
    C = len(field)
    R = len(field[0])
    rr = 0
    cc = 0
    while True:
        print(field)
        print(C,R,cc,rr,field[cc][rr])

        if field_[cc][rr] != field[cc][rr]:
            rr+=1
            continue

        if field[cc][rr] == ">":
            if rr < R-1:
                if field[cc][rr+1] == ".":
                    field[cc][rr] = "."
                    field[cc][rr+1] = ">"

            elif rr == R-1:
                if field[cc][0] == ".":
                    field[cc][rr] = "."
                    field[cc][0] = ">"

        if field[cc][rr] == "v":
            if cc < C-1:
                if field[cc+1][rr] == ".":
                    field[cc][rr] = "."
                    field[cc+1][rr] = "v"
            elif cc == C-1:
                if field[0][rr] == ".":
                    field[cc][rr] = "."
                    field[0][rr] = "v"

        rr +=1
        if rr == R:
            rr = 0
            cc += 1
        if cc == C:
            cc = 0

        if cc == C-1 and rr == R-1:
            break


    print(field)

field = add_input(input_)
counter = 0
for step in range(1,1000):
    field_old = field.copy()
    for_move(field)
    if not np.array_equal(field,field_old):
        counter +=1
    else:
        print(counter-1)
        break

#print(field)
#print(move(field))