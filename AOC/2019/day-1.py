import re
import numpy

with open("day-1-file") as file:
    lines = file.read().splitlines()

##testing
zahl = 148191
#zahl = 1969
def fuel_required(zahl):
    fuel_required1 = (int(numpy.ceil(int(zahl)) / 3)) - 2
    return fuel_required1
summe = []
for line_ in lines:
    summe.append(fuel_required(line_))
print(f"LÖSUNG PART 1: {sum(summe)}")

## PART 2 ##
liste = []
def rechnung(zahl,liste):
    fuel_required1 = (int(numpy.ceil(int(zahl)) / 3)) - 2
    if fuel_required1 > 5:
        #liste.append(fuel_required1)
        rechnung(fuel_required1,liste)
    liste.append(fuel_required1)
    return sum(liste)

#print(rechnung(zahl,liste))
liste = [] ## Liste leeren

ges = []
for line_ in lines:
    ges.append(rechnung(line_,liste))
    liste = []
print(f"LÖSUNG PART 2: {sum(ges)}")
