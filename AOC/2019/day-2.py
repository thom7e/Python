

#program3 = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,2,23,6,27,2,6,27,31,2,13,31,35,1,10,35,39,2,39,13,43,1,43,13,47,1,6,47,51,1,10,51,55,2,55,6,59,1,5,59,63,2,9,63,67,1,6,67,71,2,9,71,75,1,6,75,79,2,79,13,83,1,83,10,87,1,13,87,91,1,91,10,95,2,9,95,99,1,5,99,103,2,10,103,107,1,107,2,111,1,111,5,0,99,2,14,0,0]
#program = [1,1,1,4,99,5,6,0,99]

program = [int(x) for x in open("day-2-file").read().split(",")]

program[1] = 12
program[2] = 2

i = 0
while True:
    opcode = program[i]
    i1, i2, i3 = program[i + 1], program[i + 2], program[i + 3]
    if opcode == 1:
        program[i3] = program[i1] + program[i2]
    elif opcode == 2:
        program[i3] = program[i1] * program[i2]
    elif opcode == 99:
        print(f"SOLUTION PART1: {program[0]}")
        break
    i += 4

program = [int(x) for x in open("day-2-file").read().split(",")]
for x in range(0,100):
    for y in range(0,100):
        program[1] = x
        program[2] = y
        i = 0
        while True:
            opcode = program[i]
            i1,i2,i3 = program[i+1],program[i+2],program[i+3]
            if opcode == 1:
                program[i3] = program[i1]+program[i2]
            elif opcode == 2:
                program[i3] = program[i1] * program[i2]
            elif opcode == 99:
                if program[0] == 19690720:
                    print("Solution Part2: Pair found")
                    print(f"Verb:{program[1]}, noun: {program[2]}")
                    print(100*program[1]+program[2])

                    break
                else:

                    break
            i += 4
        program = [int(x) for x in open("day-2-file").read().split(",")]

