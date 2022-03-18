import re
with open("day-3-file") as f:
    dir = f.read().split("\n")

dir_1 = dir[0]
dir_2 = dir[1]

def route(dir_1):
    x1, y = 0, 0
    way_1 = set()
    for direction in [dir_1]:

        for dir_ in direction.split(","):

            if dir_[0] == "R":
                #print("rechts")
                #print(dir_[1:])
                lr = int(dir_[1:])
                for x in range(lr+1):
                    way_1.add((x1+x,y))
                x1 += lr

            elif dir_[0] == "D":
                #print("unten")
                #print(dir_[1:])

                up = -int(dir_[1:])
                for x in range(up):
                    way_1.add((x1,y+x))
                y += up

            elif dir_[0] == "U":
                #print("oben")
                #print(dir_[1:])

                up = int(dir_[1:])
                for x in range(up+1):
                    way_1.add((x1,y+x))
                y += up

            elif dir_[0] == "L":
                #print("links")
                #print(dir_[1:])
                lr = -int(dir_[1:])
                for x in range(lr):
                    way_1.add((x1+x,y))
                x1 += lr

        return set(way_1)

route_1 = route(dir_1)
route_2 = route(dir_2)

both = route_1&route_2

ans = sorted([abs(i)+abs(j) for (i,j) in both])
print(f"Meine Antwort ist {ans}")

A,B,_ = open("day-3-file").read().split("\n")
A,B = [x.split(",") for x in [A,B]]

DX = {"L":-1,"R": 1, "U":0, "D":0}
DY = {"L":0,"R": 0, "U":1, "D":-1}

#print(A)
def get_points(A):
    x = 0
    y = 0
    ans = set()
    ans.add((x,y))
    for cmd in A:
        d = cmd[0]
        n = int(cmd[1:])
        assert d in ["L","R","U","D"]
        for _ in range(n):
            x += DX[d]
            y += DY[d]
            ans.add((x,y))
    return ans

PA = get_points(A)
PB = get_points(B)
#print(PA)
#print(route_1)
both2 = PA&PB
answer = sorted(([abs(x)+abs(y) for (x,y) in both2]))
print(answer)
