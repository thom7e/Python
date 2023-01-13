



def part_1():
    with open("day-5.in") as inp:
        data = inp.read().splitlines()
    data = [int(x) for x in data]

    index = 0
    counter = 0

    while True:
        if index > len(data)-1:
            return (f"{counter} steps needed to escape")

        instr = data[index]

        data[index] += 1
        index += instr

        counter += 1

print("PART I \n",part_1())

def part_2():
    with open("day-5.in") as inp:
        data = inp.read().splitlines()
    data = [int(x) for x in data]

    index = 0
    counter = 0

    while True:
        if index > len(data)-1:
            return (f"{counter} steps needed to escape")

        instr = data[index]
        if data[index] >= 3:
            data[index] -= 1
        else:
            data[index] += 1
        index += instr

        counter += 1

print("PART II \n",part_2())


