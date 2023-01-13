with open("day-4.in") as inp:
    data = inp.read().splitlines()

def part_1(data):
    counter_p1 = 0
    for block in data:
        block = block.split(" ")
        phrase_1 = []
        for phrase_ in block:
            if not phrase_ in phrase_1:
                phrase_1.append(phrase_)

        if len(phrase_1) == len(block):
            counter_p1 += 1

    return counter_p1

print("PART I",part_1(data))

def part_2(data):
    counter_p2 = 0
    for block in data:
        block = block.split(" ")
        block = [sorted(x) for x in block]

        phrase_1 = []
        for phrase_ in block:
            if not sorted(phrase_) in phrase_1:
                phrase_1.append(phrase_)

        if len(phrase_1) == len(block):
            counter_p2 += 1

    return counter_p2

print("PART II",part_2(data))