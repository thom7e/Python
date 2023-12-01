import re
summe_p1 = []
summe_p2 = []
with open("day-1.in") as input:
    inp = input.readlines()


for line in inp:
    liste_numbers = []
    liste_numbers_p2 = []
    for i in range(len(line)):
        if line[i].isdigit():
            liste_numbers_p2.append(line[i])
            liste_numbers.append(line[i])
        if line[i:].startswith("one"):
            liste_numbers_p2.append("1")
        if line[i:].startswith("two"):
            liste_numbers_p2.append("2")
        if line[i:].startswith("three"):
            liste_numbers_p2.append("3")
        if line[i:].startswith("four"):
            liste_numbers_p2.append("4")
        if line[i:].startswith("five"):
            liste_numbers_p2.append("5")
        if line[i:].startswith("six"):
            liste_numbers_p2.append("6")
        if line[i:].startswith("seven"):
            liste_numbers_p2.append("7")
        if line[i:].startswith("eight"):
            liste_numbers_p2.append("8")
        if line[i:].startswith("nine"):
            liste_numbers_p2.append("9")

    summe_p1.append(int(str(liste_numbers[0]) + str(liste_numbers[-1])))
    summe_p2.append(int(str(liste_numbers_p2[0])+str(liste_numbers_p2[-1])))

print(f"p2: {sum(summe_p1)}")
print(f"p2: {sum(summe_p2)}")
