with open("day-10.in") as file:
    x = file.read().strip().split("\n")

line = []
for xx in x:
    line.append([x for x in xx])
open = ["[","<","(","{"]


def replace(linez):
    combs = ["[]", "<>", "()", "{}"]
    for comb in combs:
        linez = linez.replace(comb, "")
    return linez

def rekursion(line):
    new_line = replace(line)
    if len(replace(line)) == len(line):
        return replace(line)
    else:
        return rekursion(new_line)

def check_corrupted(line):
    checker = []
    for x in rekursion(line):
        if x not in open:
            checker.append("x")
        else:
            checker.append("y")
    if len(set(checker)) == 1:
        return ""
    else:
        return str(line)

def check_incomplete(line):
    checker = []
    for x in rekursion(line):
        if x not in open:
            checker.append("x")
        else:
            checker.append("y")
    if len(set(checker)) == 2:
        return ""
    else:
        return str(line)

corrupted =  []
for line_ in x:
    corrupted.append(str(check_corrupted(line_)))

def part_1(corrupted):
    score = 0
    for line in corrupted:
        #print(line)
        if not line == "":
            for x in range(len(rekursion(line))):
                if rekursion(line)[x] == "]":
                    score += 57
                    break
                if rekursion(line)[x] == ">":
                    score += 25137
                    break
                if rekursion(line)[x] == ")":
                    score += 3
                    break
                if rekursion(line)[x] == "}":
                    score += 1197
                    break
    return score
print(f"PART 1: {part_1(corrupted)}")

incomplete = []
for line__ in x:
    incomplete.append(str(check_incomplete(line__)))

def part_2(liste):
    points = []
    for line in liste:
        score = 0

        if not line == "":

            for x in range(len(rekursion(line))):
                new_line = rekursion(line)
                if new_line[::-1][x] == "[":
                    score = score*5 + 2

                elif new_line[::-1][x] == "<":
                    score = score*5 + 4

                elif new_line[::-1][x] == "(":
                    score = score*5 + 1

                elif new_line[::-1][x] == "{":
                    score = score*5 + 3
            points.append(score)

    return sorted(points)[int(len(points)/2)]
print(f"PART II: {part_2(incomplete)}")
