import numpy as np
import time
sudoku__ = [[ 8 ,'x'  ,'x','x' ,'x','x', 'x', 'x','x' ],
             ['x','x',3,6,'x' ,'x' , 'x',  'x' ,'x'],
             [ 'x',7, 'x', 'x',9 , 'x' ,2,'x','x'],
             ['x', 5, 'x', 'x','x' ,7,'x',  'x','x' ],
             ['x','x','x' , 'x', 4,  5, 7,'x','x'],
             ['x'  ,  'x','x',1,'x','x','x',3,'x'],
             ['x','x',1,'x','x','x','x',6,8],
             ['x','x',8,5,'x','x','x',1,'x'],
             ['x',9,'x','x','x','x',4,'x','x']]

G = np.array(sudoku__,dtype=str)
def line(sudoku,row,col,number):
    zeile = []
    spalte = []
    for x in sudoku[:,col]:
        if x != "x":
            spalte.append(int(x))
    for y in sudoku[row,:]:
        if y != "x":
            zeile.append(int(y))

    if int(number) in zeile or int(number) in spalte:
        return False
    else:

        return True


def quadrant(sudoku,row,col,number):
    rr = row//3
    rc = col//3
    quadrant_ = []
    for x in range(rr*3,rr*3+3):
        for y in range(rc*3,rc*3+3):
            if sudoku[x][y] != "x":
                quadrant_.append(int(sudoku[x][y]))

    if int(number) in quadrant_:
        #print(quadrant_)
        return False
    else:
        return True

#print(quadrant(G,0,5,9))
#print(line(G,0,5,9))
def solve(sudoku,row,col,number):
    if line(sudoku,row,col,number) and quadrant(sudoku,row,col,number):
        return True
    else:
        return False


def find_x(sudoku):
    for x in range(len(sudoku)):
        for y in range(len(sudoku[0])):
            if sudoku[x][y] == "x":
                return x,y
    return None

def lösung(sudoku):
    find = find_x(sudoku)
    if not find:
        return True
    else:
        row, col = find

    for x in range(1,10):
        if solve(sudoku,row,col,x):
            sudoku[row][col] = x
            #print(sudoku)
            if lösung(sudoku):
                return True
            else:
                sudoku[row][col] = "x"

start = time.time()
lösung(G)
end = time.time()
time =(end-start)
print(G)
print(f"Time elapsed: {time} Seconds")







