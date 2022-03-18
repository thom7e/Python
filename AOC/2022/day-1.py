with open("day-1-test") as f:
    dir = f.read().split("\n")



counter = 0
for x in range(len(dir)-3):
    first_sum = sum([int(dir[x]),int(dir[x+1]),int(dir[x+2])])
    sec_sum = sum([int(dir[x+1]),int(dir[x+2]),int(dir[x+3])])
    print(first_sum)
    print(sec_sum)
    print("nächstes")
    if first_sum < sec_sum:
        counter+=1


print(counter)
