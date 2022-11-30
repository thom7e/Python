import numpy as np

with open("day-9.in", "r") as file:
    x = file.read().strip().split("\n")

B = np.array([x])


A = np.array([[]],dtype=int)
#print(A)
#print(x)

for ar in x:
    arr = [int(x) for x in ar]
    #print(arr)
    #print(arr)
    new_A=np.append(A,[arr],axis=1)

#print(new_A)

X = []
for i in x:
    line = []
    for i_ in i:
        #print(i_)
        line.append(i_)
    X.append(line)


def part_1(X):
    ### PART I '####
    lowest = []
    for col in range(len(X)):
        for cell in range(len(X[0])):
            if col == 0:
                if cell == 0:
                    if X[col][cell + 1] > X[col][cell] and X[col + 1][cell] > X[col][cell]:
                        lowest.append(X[col][cell])
                if 0 < cell < len(X[0]) - 1:
                    if X[col][cell - 1] > X[col][cell] and X[col][cell + 1] > X[col][cell] and X[col + 1][cell] > X[col][cell]:
                        lowest.append(X[col][cell])
                if cell == len(X[0])-1:
                    if X[col][cell - 1] > X[col][cell] and X[col + 1][cell] > X[col][cell]:
                        lowest.append(X[col][cell])

            elif 0 < col < len(X)-1:
                if cell == 0:
                    if X[col][cell + 1] > X[col][cell] and X[col + 1][cell] > X[col][cell] and X[col - 1][cell] > X[col][cell]:
                        lowest.append(X[col][cell])
                if 0 < cell < len(X[0])-1:
                    if X[col][cell - 1] > X[col][cell] and X[col][cell + 1] > X[col][cell] and X[col + 1][cell] > X[col][cell] and X[col - 1][cell] > X[col][cell]:
                        lowest.append(X[col][cell])
                if cell == len(X[0])-1:
                    if X[col][cell - 1] > X[col][cell]  and X[col + 1][cell] > X[col][cell] and X[col - 1][cell] > X[col][cell]:
                        lowest.append(X[col][cell])

            elif col == len(X)-1:
                if cell == 0:
                    if X[col][cell + 1] > X[col][cell] and X[col - 1][cell] > X[col][cell]:
                        lowest.append(X[col][cell])
                if 0 < cell < len(X[0])-1:
                    if X[col][cell - 1] > X[col][cell] and X[col][cell + 1] > X[col][cell] and X[col - 1][cell] > X[col][cell]:
                        lowest.append(X[col][cell])
                if cell == len(X[0])-1:
                    if X[col][cell - 1] > X[col][cell]  and X[col - 1][cell] > X[col][cell]:
                        lowest.append(X[col][cell])



#print(lowest)

    risk = []
    for risk_level in lowest:
        risk.append(int(risk_level)+1)
    return sum(risk)

print("### PART I #### \n",f"Das Risiko Level ist: {part_1(X)}")

def check_lowest(X,col,cell):
    ### PART I '####
    lowest = []

    if col == 0:
        if cell == 0:
            if X[col][cell + 1] > X[col][cell] and X[col + 1][cell] > X[col][cell]:
                lowest.append(X[col][cell])
        if 0 < cell < len(X[0]) - 1:
            if X[col][cell - 1] > X[col][cell] and X[col][cell + 1] > X[col][cell] and X[col + 1][cell] > X[col][cell]:
                lowest.append(X[col][cell])
        if cell == len(X[0])-1:
            if X[col][cell - 1] > X[col][cell] and X[col + 1][cell] > X[col][cell]:
                lowest.append(X[col][cell])

    elif 0 < col < len(X)-1:
        if cell == 0:
            if X[col][cell + 1] > X[col][cell] and X[col + 1][cell] > X[col][cell] and X[col - 1][cell] > X[col][cell]:
                lowest.append(X[col][cell])
        if 0 < cell < len(X[0])-1:
            if X[col][cell - 1] > X[col][cell] and X[col][cell + 1] > X[col][cell] and X[col + 1][cell] > X[col][cell] and X[col - 1][cell] > X[col][cell]:
                lowest.append(X[col][cell])
        if cell == len(X[0])-1:
            if X[col][cell - 1] > X[col][cell]  and X[col + 1][cell] > X[col][cell] and X[col - 1][cell] > X[col][cell]:
                lowest.append(X[col][cell])

    elif col == len(X)-1:
        if cell == 0:
            if X[col][cell + 1] > X[col][cell] and X[col - 1][cell] > X[col][cell]:
                lowest.append(X[col][cell])
        if 0 < cell < len(X[0])-1:
            if X[col][cell - 1] > X[col][cell] and X[col][cell + 1] > X[col][cell] and X[col - 1][cell] > X[col][cell]:
                lowest.append(X[col][cell])
        if cell == len(X[0])-1:
            if X[col][cell - 1] > X[col][cell]  and X[col - 1][cell] > X[col][cell]:
                lowest.append(X[col][cell])


    return lowest


def find_basin(arr, col,cell):
    basin = []
    pos = [(1,0),(-1,0),(0,1),(0,-1)]
    for x,y in pos:
        for z in range(10):
            if int(arr[col+x*z][cell+y*z]) != 9 :
                basin.append(int(arr[col+x*z][cell+y*z]))

            else:
                basin.remove(int(arr[col][cell]))
                break
    basin.append(int(arr[col][cell]))
    return basin


print(find_basin(X,2,2))

def part_2(X):
    ### PART I '####
    lowest = []
    for col in range(len(X)):
        for cell in range(len(X[0])):
            if col == 0:
                if cell == 0:
                    if X[col][cell + 1] > X[col][cell] and X[col + 1][cell] > X[col][cell]:
                        lowest.append(X[col][cell])
                if 0 < cell < len(X[0]) - 1:
                    if X[col][cell - 1] > X[col][cell] and X[col][cell + 1] > X[col][cell] and X[col + 1][cell] > X[col][cell]:
                        lowest.append(X[col][cell])
                if cell == len(X[0])-1:
                    if X[col][cell - 1] > X[col][cell] and X[col + 1][cell] > X[col][cell]:
                        lowest.append(X[col][cell])

            elif 0 < col < len(X)-1:
                if cell == 0:
                    if X[col][cell + 1] > X[col][cell] and X[col + 1][cell] > X[col][cell] and X[col - 1][cell] > X[col][cell]:
                        lowest.append(X[col][cell])
                if 0 < cell < len(X[0])-1:
                    if X[col][cell - 1] > X[col][cell] and X[col][cell + 1] > X[col][cell] and X[col + 1][cell] > X[col][cell] and X[col - 1][cell] > X[col][cell]:
                        lowest.append(X[col][cell])
                if cell == len(X[0])-1:
                    if X[col][cell - 1] > X[col][cell]  and X[col + 1][cell] > X[col][cell] and X[col - 1][cell] > X[col][cell]:
                        lowest.append(X[col][cell])

            elif col == len(X)-1:
                if cell == 0:
                    if X[col][cell + 1] > X[col][cell] and X[col - 1][cell] > X[col][cell]:
                        lowest.append(X[col][cell])
                if 0 < cell < len(X[0])-1:
                    if X[col][cell - 1] > X[col][cell] and X[col][cell + 1] > X[col][cell] and X[col - 1][cell] > X[col][cell]:
                        lowest.append(X[col][cell])
                if cell == len(X[0])-1:
                    if X[col][cell - 1] > X[col][cell]  and X[col - 1][cell] > X[col][cell]:
                        lowest.append(X[col][cell])



#print(lowest)

    risk = []
    for risk_level in lowest:
        risk.append(int(risk_level)+1)
    return sum(risk)



#print(lowest)
print("### PART II #### \n",f"Das Risiko Level ist: {part_2(X)}")

