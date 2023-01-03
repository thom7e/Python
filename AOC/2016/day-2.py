import numpy as np
pad_p1 = [[1,2,3],[4,5,6],[7,8,9]]
pad_p2 = [[".",".",1,".","."],[".",2,3,4,"."],[5,6,7,8,9],[".","A","B","C","."],[".",".","D",".","."]]

def numpad(pad_):
    pad = np.array(pad_)

    with open("day-2.in") as d:
        inp = d.read().splitlines()

    commands = ["".join(x) for x in inp]
    row,col = 2,0
    p1 = []
    for cmd in commands:
        #print(cmd)
        for c in cmd:
            #print(c)
            if c == "U":
                if row > 0:
                    row -= 1

                    if pad[row,col] == ".":
                        row += 1


            elif c == "R" :
                if col < len(pad)-1 and pad[row,col+1] != ".":
                    col += 1



            elif c == "D" :
                if row < len(pad)-1 and pad[row+1,col] != ".":
                    row += 1


            elif c == "L" :
                if col > 0 and pad[row,col-1] != ".":
                    col -= 1



        p1.append(str(pad[row,col]))

    part_1 = "".join(p1)
    return part_1

print(f"PART I {numpad(pad_p1)}")
print(f"PART II {numpad(pad_p2)}")
