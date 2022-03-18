import numpy as np
with open("day-15.in") as file:
    f = file.read().strip().split("\n")

def create_array(input):
    G = []
    for x in input:
        G.append([int(x) for x in x])
    G = np.array(G)
    return G

G = create_array(f)
Real = create_array(f)
R = len(G[0])
C = len(G)
def check_lowest2(liste1,liste2,start):
    jumps = []
    if start == 0:
        start = 0
    else:
        start = start -1
    for x,y in enumerate(liste1):
        if x < len(liste1)-1 and x < len(liste2)-1:
            #if liste1[x] + liste2[x] == 2:
                #jumps.append((liste1[x] + liste2[x],x))
           # else:
                #if liste1[x]+liste1[x+1]+liste2[x+1] < liste1[x]+liste2[x]+liste2[x+1]:
                #    jumps.append((liste1[x]+liste1[x+1]+liste2[x+1],x+1))
                #if liste1[x]+liste1[x+1]+liste2[x+1] > liste1[x]+liste2[x]+liste2[x+1]:
                #    jumps.append((liste1[x]+liste2[x]+liste2[x+1],x))
            zwischenstep = []
            if liste1[x] + liste2[x] == 2:
                zwischenstep.append((2,x))
                jumps.append((min(zwischenstep)))
            else:
                zwischenstep.append((liste1[x] + liste1[x + 1] + liste2[x + 1], x+1))
                zwischenstep.append((liste1[x] + liste2[x] + liste2[x + 1], x))
                jumps.append((min(zwischenstep)))


    #print(jumps[start:])
    print(jumps[start:])
    return min(jumps[start:])
#start_ = 0
#print(check_lowest2(G[0],G[1],0))
#print(check_lowest2(G[1],G[2],0))
#print(check_lowest2(G[2],G[3],6))
#print(check_lowest2(G[3],G[4],7))
#print(check_lowest2(G[4],G[5],7))
#print(check_lowest2(G[5],G[6],8))
#print(check_lowest2(G[6],G[7],8))
#print(check_lowest2(G[8],G[9],8))

#start = check_lowest2(G[0],G[1],start_)[0]
#print(check_lowest2(G[1],G[2],start))
#print(check_lowest2(G[2],G[3],0))
#print(check_lowest2(G[3],G[4],0))
#print(check_lowest2(G[5],G[6],6))
start = 0
jumps = []
for x in range(len(G)-1):
    jumps.append(check_lowest2(G[x],G[x+1],start)[1])
    start = check_lowest2(G[x],G[x+1],start)[1]
    print(jumps)


col = 0
row = 0
jump = 0
G_new = G
while True:
    G_new[col][row] = 99
    if jumps[jump] == row:
        col += 1
        jump += 1
    else:
        row+=1
    if col == len(G) or row == len(G[0]) or jump == len(jumps):
        break


counter = 0
for col_ in range(1,len(G_new)):
    for row_ in range(len(G_new[0])):
        if G[col_][row_] == 99:
            print(Real[col_][row_])
            counter += Real[col_][row_]
        #print(col_,row_)

print(Real[len(Real)-1][len(Real[0])-1])
#print(G)
#print(Real)
#print(counter)
counter = counter + Real[len(Real)-1][len(Real[0])-1]
print(counter)

#print(check_lowest(G[1],G[1+1],0))
#print(check_lowest(G[2],G[2+1],0))
#print(check_lowest(G[3],G[3+1],6))
#print(check_lowest(G[4],G[4+1],7))
#print(check_lowest(G[5],G[5+1],7))
#print(check_lowest(G[6],G[6+1],8))
#print(check_lowest(G[7],G[7+1],8))
#print(check_lowest(G[8],G[8+1],8))






