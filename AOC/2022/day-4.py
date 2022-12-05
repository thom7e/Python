with open("day-4.in") as f:
    inp = f.read().splitlines()

def part_1():
    counter = 0
    # get the information needed
    for lines in inp:
        ranges_1 = lines.split(",")[0] #first range
        ranges_2 = lines.split(",")[1] #second range

        # get the lists with the ranges befor
        liste_1 = [x for x in range(int(ranges_1.split("-")[0]),int(ranges_1.split("-")[1])+1)]
        liste_2 = [x for x in range(int(ranges_2.split("-")[0]),int(ranges_2.split("-")[1])+1)]

        # check which number is in the other list and append it to a new list, then comopare the new list with the old list. If it's the same count +1
        new_list_1 = []
        for comparison in liste_1:
            if comparison in liste_2:
                new_list_1.append(comparison)
        if new_list_1 == liste_1:
            counter += 1
            continue # take care of continue, so you don't get duplicates


        new_list_2 = []
        for comparison_2 in liste_2:
            if comparison_2 in liste_1:
                new_list_2.append(comparison_2)


        if new_list_2 == liste_2:
            counter += 1
            continue # take care of continue, so you don't get duplicates



    return counter

print(f"PART I {part_1()}")

def parte_2():
    part_2 = 0

    for lines in inp:
        ranges_1 = lines.split(",")[0]
        ranges_2 = lines.split(",")[1]

        liste_1 = [x for x in range(int(ranges_1.split("-")[0]), int(ranges_1.split("-")[1]) + 1)]
        liste_2 = [x for x in range(int(ranges_2.split("-")[0]), int(ranges_2.split("-")[1]) + 1)]
        # print(liste_1, liste_2)

        # check which number is in the other list and append it to a new list,if something in the list count +1
        new_list_1 = []
        for comparison in liste_1:
            if comparison in liste_2:
                new_list_1.append(comparison)


        new_list_2 = []
        for comparison_2 in liste_2:
            if comparison_2 in liste_1:
                new_list_2.append(comparison_2)

        if len(new_list_2) or len(new_list_1) > 0:
            part_2 += 1

    return part_2

print(f"PART II {parte_2()}")