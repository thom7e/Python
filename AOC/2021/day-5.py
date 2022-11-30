from collections import Counter

with open("day-5.in", "r") as file:
    x = file.read().splitlines()


direcs = []
for dir in x:
    y = dir.split(" -> ")
    direcs.append(y)

directions = []
for dirs in direcs:
    for dirs2 in dirs:
        directions.append(dirs2.split(","))

pairs = []

for x in range(len(directions)-1):
    pairs.append((directions[x],directions[x+1]))

readypairs = []
for pair in range(len(pairs)):
    #print(pairs[pair])
    if pair % 2 == 0:
        readypairs.append(pairs[pair])

#print(readypairs)

tests = []
for x in readypairs:
    #print(x[0][0], x[1][0])
    x1 = int(x[0][0])
    x2 = int(x[1][0])
    y1 = int(x[0][1])
    y2 = int(x[1][1])
    if y1 == y2:
        if x1 < x2:
            for y in range(abs(x1),abs(x2)+1):
                tests.append((y,y1))
        else:
            for y in range(abs(x2),abs(x1)+1):

                tests.append((y,y1))
    elif x1 == x2:
        if y1 < y2:
            for y in range(abs(y1),abs(y2)+1):
                tests.append((x1,y))
        else:
            for y in range(abs(y2),abs(y1)+1):
                tests.append((x1,y))
    else:
        print(x1,y1,x2,y2)
        if x1 < x2:
            for y in range(abs(x1),abs(x2)+1):
                tests.append((abs(y+1),y+1))
        #elif x1 > x2 and y1 > y2:
            #for y in range(abs(x2),abs(x1)+1):
                #for z in range(abs(y2),abs(y1)+1):
                    #tests.append((abs(y+1),abs(z-1)))
        elif x1 > x2 and y1 < y2:
            for y in range(abs(x1)-abs(x2)+1):
                for z in range(abs(abs(y2)-abs(y1)+1)):
                    tests.append((abs(x1-y),abs(y1+z)))




print(tests)

counter = 0
for count in Counter(tests).values():
    if count > 1:
        counter +=1
print(counter)