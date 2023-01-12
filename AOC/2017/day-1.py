with open("day-1.in") as inp:
    data = inp.read().splitlines()[0]

counter = 0

for number in range(len(data)-1):
    if data[number] == data[number+1]:
        counter += int(data[number])

if data[0] == data[-1]:
    counter += int(data[-1])

print("P1",counter)

counter = 0
for number in range(len(data)):
    if number + len(data)/2 < len(data):
        if data[number] == data[(number+int(len(data)/2))]:
            counter += int(data[number])
    else:
        vglindex = abs(int(len(data)-(len(data)/2+number)))
        if data[number] == data[vglindex]:
            counter += int(data[number])

print("P2",counter)
