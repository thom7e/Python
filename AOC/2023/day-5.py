import re

with open("day-5.in") as input:
    f = input.read().splitlines()

def get_listen(f):
    temp_liste = []
    neue_listen = []
    for element in f:
        if element == '':
            if temp_liste:
                neue_listen.append(temp_liste)
                temp_liste = []
        else:
            temp_liste.append(element)

    if temp_liste:
        neue_listen.append(temp_liste)
    return neue_listen

def get_werte(base_list,input):
    for line in base_list:
        dest,source,range = line.split(" ")[0],line.split(" ")[1],line.split(" ")[2]
        if int(source) <= int(input) <= int(source)+int(range):
            return int(input) - int(source) + int(dest)
    for line in base_list:
        dest, source, range = line.split(" ")[0], line.split(" ")[1], line.split(" ")[2]
        if int(input) <  int(source) or int(input) >= int(source+range):

            return input

def get_location(seed):
    x= seed
    for step in range(1,8):
        seed = x
        x = get_werte(neue_listen[step][1:],seed)
    return x


def neue_seeds(liste):
    new_list = []
    for i in range(0, len(liste), 2):  # Durchläuft die Liste in 2er-Schritten
        start_value = liste[i]
        range_value = liste[i+1]
        new_list.extend(range(start_value, start_value + range_value))

    return new_list


def p1(liste):
    lowest = []
    for x in liste:
        lowest.append((get_location(x)))

    return min(lowest)


neue_listen = get_listen(f)
## SEEDS
seeds = [int(x) for x in re.findall(r'\d+',str(neue_listen[0]))]

print("ERGEBNIS p1:", p1(seeds))


# P2 MEMORY ERROR
# p2_liste = neue_seeds(seeds)
#
# for x in p2_liste[:-1]:
#     print(get_location(x))
# print("ERGEBNIS p2:",p1(p2_liste[:-1]))
# #print(get_werte(neue_listen[7][1:], 67))




