with open("day-22.in") as f:
    input_ = f.read().split("\n")

anweisungen = []
for anweisung in input_:
    anweisungen.append(anweisung.split(","))
anweisungen2 = []
cubes = set()
for anweisung2 in anweisungen:
    onoff = anweisung2[0].split(" ")[0]
    if onoff == "on":
        x = ((anweisung2[0].split("="))[1]).split("..")
        y = ((anweisung2[1].split("="))[1]).split("..")
        z = ((anweisung2[2].split("="))[1]).split("..")
        #if int(x[0]) in range(-50,51) and int(x[1]) in range(-50,51) and int(y[0]) in range(-50,51) and int(y[1]) in range(-50,51) and int(z[0]) in range(-50,51) and int(z[1]) in range(-50,51):
        for x_ in range(int(x[0]),int(x[1])+1):
            for y_ in range(int(y[0]),int(y[1])+1):
                for z_ in range(int(z[0]), int(z[1]) + 1):
                        cubes.add((x_,y_,z_))
    elif onoff == "off":
        x = ((anweisung2[0].split("="))[1]).split("..")
        y = ((anweisung2[1].split("="))[1]).split("..")
        z = ((anweisung2[2].split("="))[1]).split("..")
        #if int(x[0]) in range(-50,51) and int(x[1]) in range(-50,51) and int(y[0]) in range(-50,51) and int(y[1]) in range(-50,51) and int(z[0]) in range(-50,51) and int(z[1]) in range(-50,51):
        for x_ in range(int(x[0]),int(x[1])+1):
            for y_ in range(int(y[0]),int(y[1])+1):
                for z_ in range(int(z[0]), int(z[1]) + 1):
                    cubes.discard((x_,y_,z_))
#print(cubes)
print(len(cubes))

#print(anweisungen2)
