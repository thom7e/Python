from collections import Counter
import string
import re
with open("day-4.in") as d:
    inp = d.read().splitlines()

def part_1():
    commons = [x.split("-") for x in inp]
    sum_ = []
    for com in commons:
        sorted_ = "".join(sorted("".join(com[:-1])))
        mc = Counter("".join(sorted_)).most_common(5)
        mc_ = "".join(sorted("".join([x[0] for x in mc[:5]])))
        hashsum = "".join(sorted(com[-1].split("[")[1].split("]")[0]))


        id = int(com[-1].split("[")[0])
        if mc_ == hashsum:
            sum_.append(id)

    return sum(sum_)

print("PART I",part_1())

def part_2():
    #example = "qzmt-zixmtkozy-ivhz-343"
    alphabet = list(string.ascii_lowercase)
    for line in inp:
        example = line.split("[")[0]
        new_string = []
        id = int(example.split("-")[-1])
        for letter in example:
            if letter in alphabet:
                new_string.append(alphabet[(int(alphabet.index(letter))+id)%26])
            elif letter == "-":
                new_string.append(" ")
        encrypted = "".join(new_string)
        #print(encrypted)


        if len(re.findall("north",encrypted)) > 0:
            return id


print("PART II",part_2())