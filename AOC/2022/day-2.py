with open("day-2") as file:
    lines = file.read().splitlines()


def part1(lines):
    hor = 0
    depth = 0
    for command in lines:
        if command.split(" ")[0] == "forward":
            hor += int(command.split(" ")[1])

        elif command.split(" ")[0] == "down":
            depth += int(command.split(" ")[1])
        elif command.split(" ")[0] == "up":
            depth -= int(command.split(" ")[1])

    print(hor*depth)

def part2(lines):
    hor = 0
    aim = 0
    depth = 0
    for command in lines:
        if command.split(" ")[0] == "forward":
            hor += int(command.split(" ")[1])
            depth += int(command.split(" ")[1]) * aim
        elif command.split(" ")[0] == "down":
            aim += int(command.split(" ")[1])
        elif command.split(" ")[0] == "up":
            aim -= int(command.split(" ")[1])

    print(hor*depth)

part1(lines)
part2(lines)