with open("day-10.in") as d:
    inp = d.read().splitlines()

x = 1
cycle = 1
counter = 0
cycle_1 = 20
cycle_2 = 60
cycle_3 = 100
cycle_4 = 140
cycle_5 = 180
cycle_6 = 220
inde = 0
werte = []
while True:
    counter += 1
    cycle += 1
    print(cycle, x)
    for index,cmd in enumerate(inp):
        if cmd.split(" ")[0] == "noop":

            inp.pop(0)
            break
        else:
            #print(int(cmd.split(" ")[1]))
            x += int(cmd.split(" ")[1])

            cycle += 1
            inp.pop(0)
            werte.append((cycle,x))
            break


    #print("CYCLE", cycle,counter)
    #print("x ist :", x)
    if cycle == cycle_1 or cycle == cycle_1-1:
        #print("20",x,x*cycle_1)
        werte.append(x*cycle_1)

    elif cycle == cycle_2 or cycle == cycle_2-1:
        #print("60:",x,cycle_2*x)
        werte.append(x * cycle_2)
    elif cycle == cycle_3 or cycle == cycle_3-1:
        #print("100:", x,cycle_3*x)
        werte.append(x * cycle_3)
    elif cycle == cycle_4 or cycle == cycle_4-1:
        #print("140:", x,cycle_4*x)
        werte.append(x * cycle_4)
    elif cycle == cycle_5 or cycle == cycle_5-1:
        #print("180:", x,cycle_5*x)
        werte.append(x * cycle_5)
    elif cycle == cycle_6 or cycle == cycle_6-1:
        #print("220:", x,cycle_6*x)
        werte.append(x * cycle_6)

    if cycle == 221:
        break


print(sum(set(werte)))