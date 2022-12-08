import string
with open("day-5.in") as f:
    raw = f.read().split("\n\n")

commands = raw[1].splitlines()
stackz = raw[0].splitlines()

def parse_stacks():

    capitals = list(string.ascii_uppercase)
    all_stacks = []

    for row in stackz:
        index = 1
        stack = []
        while index < 35:
            if len(row) <= 31:
                if index <= 29:
                    stack.append(row[index])
                    index += 4

                else:
                    stack.append(" ")
                    break
            else:
                stack.append(row[index])
                index += 4

        all_stacks.append(stack)

    stacks_sorted = []
    for stacks in range(len(all_stacks[:-1])+1):

        for sort_stacks in all_stacks:
            if str(sort_stacks[stacks][0]) in ["1","2","3","4","5","6","7","8","9"]:
                stacks_sorted.append(";")
            if str(sort_stacks[stacks][0]) in capitals:
                stacks_sorted.append(f"{str(sort_stacks[stacks][0])},")

    parsed_stacks =''.join(stacks_sorted).split(";")

    return parsed_stacks


stacks = parse_stacks()

def part_1():
        # get the different stacks, so i can get it by the indices
        stack = []
        for st in stacks:
            stack.append(st.split(","))


        # check the input for the actions and movements
        for actions in commands:
            action_1 = actions.split(" ")[1] # amount
            action_2 = actions.split(" ")[3] # stack where it comes from
            action_3 = actions.split(" ")[5] # stack where its moved to

            # start amount
            amount = 0
            # got through the movements, and when the amount is > 0 we go for another loop
            for x in range(1,int(action_1)+1):
                # y will be the index/crate which is moved, because wie start the loop by 1 we have to substract it again to get the right index
                y = x-amount
                # now make the actions and get the new stacks
                stack[int(action_3) - 1].insert(0,stack[int(action_2) - 1][y-1]) # insert the index/crate from the second stack to position 0 of the first stack
                stack[int(action_2) - 1].pop(y-1) # delete the crate
                amount += 1 #we have to add 1 to the amount to get the index back to the start

            # parse the solution in a string
            solution = []
            for sol in stack:
                if len(sol)>1:
                    solution.append(sol[0])
                else:
                    solution.append(''.join(sol))

        return ''.join(solution)

print(f" PART I: {part_1()}")

def part_2():
    # get the different stacks, so i can get it by the indices
    stack = []
    for st in stacks:
        stack.append(st.split(","))

    # check the input for the actions and movements
    for actions in commands:
        action_1 = actions.split(" ")[1]  # amount
        action_2 = actions.split(" ")[3]  # stack where it comes from
        action_3 = actions.split(" ")[5]  # stack where its moved to

        # start amount
        amount = 0
        # start index
        index = 0
        for x in range(1, int(action_1) + 1):
            # y will be the index/crate which is moved, because wie start the loop by 1 we have to substract it again to get the right index
            y = x - amount
            # now make the actions and get the new stacks
            stack[int(action_3) - 1].insert(index, stack[int(action_2) - 1][y - 1]) # now the index isn't 0 but always +1 like before in the loop to get the right order like before
            stack[int(action_2) - 1].pop(y - 1)
            amount += 1 #we have to add 1 to the amount to get the index back to the start
            index += 1 #we have to add 1 to the index to change the index (so the crate is in the same order like before)

        # parse the solution in a string
        solution = []
        for sol in stack:
            if len(sol) > 1:
                solution.append(sol[0])
            else:
                solution.append(''.join(sol))

    return ''.join(solution)


print(f" PART II: {part_2()}")
