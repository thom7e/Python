with open("day-5.in") as f:
    rpc = f.read().splitlines()
with open("day-5-crates.in") as c:
    crates = c.read().splitlines()


def part_1():
        crate = []
        for cr in crates:
            crate.append(cr.split(","))


        for actions in rpc:
            action_1 = actions.split(" ")[1]
            action_2 = actions.split(" ")[3]
            action_3 = actions.split(" ")[5]

            #print(f"{action_1} is moved from crate {action_2} to crate {action_3}")
            amount = 0
            for x in range(1,int(action_1)+1):
                y = x-amount
                #print(y)
                #print(f"from {crate[int(action_2) - 1]} to {crate[int(action_3) - 1]}")
                crate[int(action_3) - 1].insert(0,crate[int(action_2) - 1][y-1])
                crate[int(action_2) - 1].pop(y-1)
                #print(crate[int(action_3) - 1])
                #print(crate[int(action_2) - 1])
                amount += 1
                #print("next")
            solution = []
            for sol in crate:
                if len(sol)>1:
                    solution.append(sol[0])
                else:
                    solution.append(''.join(sol))

        return ''.join(solution)

print(f" PART I: {part_1()}")

def part_2():
    crate = []
    for cr in crates:
        crate.append(cr.split(","))

    for actions in rpc:
        action_1 = actions.split(" ")[1]
        action_2 = actions.split(" ")[3]
        action_3 = actions.split(" ")[5]

        # print(f"{action_1} is moved from crate {action_2} to crate {action_3}")
        amount = 0
        stelle = 0
        for x in range(1, int(action_1) + 1):
            y = x - amount
            # print(y)
            #print(f"from {crate[int(action_2) - 1]} to {crate[int(action_3) - 1]}")
            crate[int(action_3) - 1].insert(stelle, crate[int(action_2) - 1][y - 1])
            crate[int(action_2) - 1].pop(y - 1)
            #print(crate[int(action_3) - 1])
            #print(crate[int(action_2) - 1])
            amount += 1
            stelle += 1
            # print("next")
        solution = []
        for sol in crate:
            if len(sol) > 1:
                solution.append(sol[0])
            else:
                solution.append(''.join(sol))

    return ''.join(solution)


print(f" PART II: {part_2()}")
