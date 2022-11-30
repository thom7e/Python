import re
with open("day16ticket") as f:
    ticket = re.findall(r"\d+", f.read())

with open("day16nearby") as ff:
    nearby = ff.read().splitlines()

with open("day16ticket") as fff:
    ticket2 = re.findall(r"\w+ \w+", fff.read())

zeilen = []
with open("day16nearby") as ffff:
    bla = ffff.read().splitlines()
    for z in bla:
        zeilen.append(z.split(","))

def checknumbers(nearby):
    nums = []
    checks = []
    for n in nearby:
        nums.append(n.split(","))
    for nn in range(len(nums)):
        for nnn in nums[nn]:
            checks.append(int(nnn))
    return checks

def validnumbers(ticket):
    keys = []
    values = []

    for t in range(len(ticket)):
        if t%2 == 0:
            keys.append(int(ticket[t]))
        else:
            values.append(int(ticket[t]))
    zahlen = []
    pairs = dict(zip(keys,values))
    valid = []
    for i in pairs:
        zahlen.append(list(range(i, pairs[i]+1)))
    for x in range(len(zahlen)):
        for xx in zahlen[x]:
            valid.append(int(xx))

    #print(keys)
    #print(values)
    return valid

def properties(ticket,ticket2):
    keys = []
    values = []
    properties = []
    ranges = []
    for t in range(len(ticket)):
        if t % 2 == 0:
            keys.append(int(ticket[t]))
        else:
            values.append(int(ticket[t]))
    for i in range(len(keys)):
        ranges.append(tuple(range(keys[i],values[i]+1)))

    for r in range(0,len(ranges)-1,2):
        properties.append(ranges[r]+ranges[r+1])

    return properties


properties(ticket,ticket2)

valids = validnumbers(ticket)
checks = checknumbers(nearby)

falses = []
valid = []
for c in checks:
    if int(c) not in valids:
        falses.append(int(c))
    if int(c) in valids:
        valid.append(int(c))

print("Part One: " + str(sum(falses)))

########## PART TWO ##########

props = dict(zip(ticket2,properties(ticket,ticket2)))
#print(props)

def getSpalten(zeilen,valids):
    richtige = []
    print(zeilen[0])
    spalten = []
    for r in range(len(zeilen[0])):
        for z in range(len(zeilen)):
            spalten.append(zeilen[r])
       #for z in zeilen:
            #spalten.append(int(z[r]))
    print(spalten)







getSpalten(zeilen,valid)


