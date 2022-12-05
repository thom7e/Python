with open("day-4.in") as f:
    rpc = f.read().splitlines()

#print(rpc)




def part_1():
    counter = 0
    for lines in rpc:
        ranges_1 = lines.split(",")[0]
        ranges_2 = lines.split(",")[1]

        liste_1 = [x for x in range(int(ranges_1.split("-")[0]),int(ranges_1.split("-")[1])+1)]
        liste_2 = [x for x in range(int(ranges_2.split("-")[0]),int(ranges_2.split("-")[1])+1)]
        #print(liste_1, liste_2)

        neue_liste_1 = []
        for vergleich in liste_1:
            if vergleich in liste_2:
                neue_liste_1.append(vergleich)
        if neue_liste_1 == liste_1:
            counter += 1
            continue


        neue_liste_2 = []
        for vergleich_2 in liste_2:
            if vergleich_2 in liste_1:
                neue_liste_2.append(vergleich_2)


        if neue_liste_2 == liste_2:
            counter += 1
            continue



    return counter


def parte_2():
    part_2 = 0

    for lines in rpc:
        ranges_1 = lines.split(",")[0]
        ranges_2 = lines.split(",")[1]

        liste_1 = [x for x in range(int(ranges_1.split("-")[0]), int(ranges_1.split("-")[1]) + 1)]
        liste_2 = [x for x in range(int(ranges_2.split("-")[0]), int(ranges_2.split("-")[1]) + 1)]
        # print(liste_1, liste_2)

        neue_liste_1 = []
        for vergleich in liste_1:
            if vergleich in liste_2:
                neue_liste_1.append(vergleich)


        neue_liste_2 = []
        for vergleich_2 in liste_2:
            if vergleich_2 in liste_1:
                neue_liste_2.append(vergleich_2)

        if len(neue_liste_2) or len(neue_liste_1) > 0:
            part_2 += 1

    return part_2

print(part_1(),parte_2())