with open("day-7.in", "r") as file:
    hor_pos = [int(y) for y in file.read().strip().split(",")]

def check_fuel(hor_pos,align):
    posibilities = []

    for pos in hor_pos:
        fuel = pos-align
        posibilities.append(abs(fuel))

    return sum(posibilities)

def check_fuel_part2(hor_pos,align):
    posibilities = []
    for pos in hor_pos:
        fuel = []
        for f in range(0,abs(pos-align)):
            fuel.append(f+1)
        #print(sum(fuel))
        posibilities.append(sum(fuel))

    return sum(posibilities)

#print(check_fuel_part2(hor_pos,5))
min = []

for aligning in range(0,max(hor_pos)):
    pos = check_fuel_part2(hor_pos, aligning)
    if len(min) > 0:
        if pos >= min[0]:
            pass
        elif pos < min[0]:
            min.pop()
            min.append(check_fuel_part2(hor_pos, aligning))
    else:
        min.append(check_fuel_part2(hor_pos, aligning))

print(min)



