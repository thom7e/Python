
with open("day-6.in") as inp:
    data = inp.read().split("\t")

data = [int(x) for x in data]

def get_config(bla):
    while True:
        for index,max_value in enumerate(bla):
            if max_value == max(bla):
                bla[index] = 0
                index += 1
                for adding in range(max_value):
                    if index == len(bla):
                        index = 0
                    bla[index] += 1
                    index += 1
                new_data = bla
                return new_data

with open("day-6-output","w") as output:
    for x in range(19000):

        output.write(f"{get_config(data)}\n")

with open("day-6-output") as out:
    check = out.read().splitlines()

control = []
counter = 0

for c in check:
    counter += 1
    #print(control)
    if c in control:
        print("P1",counter)
        break

    control.append(c)
counter_ = 0

for c_ in check:
    counter_ += 1
    if c_ == c:
        print("P2",counter-counter_)
        break


