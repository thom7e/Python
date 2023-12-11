from functools import reduce
from operator import mul
import re

def p1():
    with open("day-6.in") as races:
        r = races.read().splitlines()


    time = [int(x) for x in r[0].split(" ") if x.isdigit()]

    distance  = [int(x) for x in r[1].split(" ") if x.isdigit()]

    possibilities = []
    for index,rr in enumerate(time):
        pos = 0
        #print("time",rr,"distance",distance[index])
        for hold_down in range(0,rr+1):
            if hold_down*(rr-hold_down) > distance[index]:
                pos += 1
        possibilities.append(pos)

    ergebnis = reduce(mul, possibilities)

    return ergebnis
print("p1:" ,p1())
def p2():
    with open("day-6.in") as races:
        r = races.read().splitlines()

    time = "".join(str([int(x) for x in r[0].split(" ") if x.isdigit()]))
    distance = "".join(str([int(x) for x in r[1].split(" ") if x.isdigit()]))

    time = int(str(re.findall(r'\d+',time)).replace("[","").replace("]","").replace(",","").replace("'","").replace(" ",""))
    dist = int(str(re.findall(r'\d+',distance)).replace("[","").replace("]","").replace(",","").replace("'","").replace(" ",""))
    pos = 0
    possibilities = []
    for hold_down in range(0, time +1):
        if hold_down * (time - hold_down) > dist:
            pos += 1
    possibilities.append(pos)

    ergebnis = reduce(mul, possibilities)
    return ergebnis
print("p2:",p2())