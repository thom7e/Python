import re
with open("day-7.in") as d:
    inp = d.read().splitlines()

counter_p1 = 0
counter_p2 = 0

def part_1(supernet,hypernet):
    check = []
    sq = supernet
    hypernet_seq = hypernet
    for outsiders in sq:
        # print(outsiders)
        for first_ in range(len(outsiders) - 3):

            four_char = outsiders[first_:first_ + 4]
            # print(four_char)

            if four_char[0] == four_char[3] and four_char[1] == four_char[2]:
                if four_char[0] == four_char[1] or four_char[2] == four_char[3]:
                    check.append("false")
                    break
                else:
                    check.append("true")
                    break

    for insiders in hypernet_seq:

        for second_ in range(len(insiders) - 3):
            four_char_ = insiders[second_:second_ + 4]

            if four_char_[0] == four_char_[-1] and four_char_[1] == four_char_[2]:
                if four_char_[0] == four_char_[1] or four_char_[2] == four_char_[3]:
                    break
                else:
                    check.append("false")
                    break

    if not "false" in check and not check == []:
        return True

def compile_p1(string):
    pattern = "\W"
    split = re.split(pattern, string)
    sq = split[::2]
    hypernet_seq = split[1::2]
    return (sq,hypernet_seq)

def part_2(supernet,hypernet):
    sq = supernet
    hypernet_seq = hypernet
    hyper_check_liste = []
    for insiders in hypernet_seq:
        for second_ in range(len(insiders) - 2):

            four_char = insiders[second_:second_ + 3]
            if four_char[0] == four_char[-1]:
                hyper_check_liste.append(four_char)

    for outsiders in sq:
        for first_ in range(len(outsiders) - 2):

            four_char = outsiders[first_:first_ + 3]
            if four_char[0] == four_char[-1]:
                corresponding = "".join([four_char[1],four_char[0],four_char[1]])

                if corresponding in hyper_check_liste:
                    return True

for ipv6 in inp:
    if part_1(compile_p1(ipv6)[0],compile_p1(ipv6)[1]):
        counter_p1 += 1

    if part_2(compile_p1(ipv6)[0],compile_p1(ipv6)[1]):
        counter_p2 += 1


print("PART I",counter_p1)
print("PART II",counter_p2)