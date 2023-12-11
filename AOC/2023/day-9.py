def get_pattern(line):
    if all(zahl == 0 for zahl in line):
        return 0
    new_pattern = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    return line[-1] + get_pattern(new_pattern)

def p1():
    with open("day-9.in") as d:
        lines = d.read().strip().split("\n")
        sum_all = 0
        for line in lines:
            nums = [int(x) for x in line.split(" ")]
            sum_all += get_pattern(nums)
        print("p1", sum_all)


def get_pattern2(line):
    if all(zahl == 0 for zahl in line):
        return 0
    new_pattern = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    return line[0] - get_pattern2(new_pattern)

def p2():
    with open("day-9.in") as d:
        lines = d.read().strip().split("\n")
        sum_all = 0
        for line in lines:
            nums = [int(x) for x in line.split(" ")]
            sum_all += get_pattern2(nums)
        print("p2", sum_all)


p1()
p2()