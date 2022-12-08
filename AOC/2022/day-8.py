import numpy as np

with open("day-8.in") as d:
    cmds = d.read().splitlines()


def get_grid(input):
    grid = np.zeros([int(len(input[0])),int(len(input))],dtype = int)

    for index,x in enumerate(input):
        x1 = " ".join(x).split(" ")
        for index2,tree in enumerate(x1):
            grid[index][index2] = int(tree)

    return grid
trees = get_grid(cmds)

visible_edges = ((len(trees[0])-2)*2+len(trees[0:,0])*2)
counter = 0
visible_trees = []

def part_I(input):
    trees = get_grid(input)
    visible_edges = ((len(trees[0]) - 2) * 2 + len(trees[0:, 0]) * 2)

    visible_trees = []
    for inner_col in range(1,len(trees[0:,0])-1):
        for inner_row in range(1,len(trees[0])-1):
            for check in range(len(trees)):## row right
                if trees[inner_col, inner_row] > np.max(trees[inner_col,:inner_row]):
                    visible_trees.append((inner_col, inner_row))#,"nach links"))#, trees[inner_col, inner_row], ">", [x for x in (trees[inner_col,:inner_row])]))
                    break
                else:
                    break
            for check in range(len(trees)): ## row left
                if trees[inner_col, inner_row] > np.max(trees[inner_col,inner_row+1:]):
                    visible_trees.append((inner_col, inner_row))
                    break
                else:
                    break
            for check in range(len(trees)): ## column nach oben
                if trees[inner_col,inner_row] > np.max(trees[:inner_col,inner_row]):
                    visible_trees.append((inner_col, inner_row))
                    break
                else:
                    break
            for check in range(len(trees)): ## column nach unten
                if trees[inner_col,inner_row] > np.max(trees[inner_col+1:,inner_row]):
                    visible_trees.append((inner_col, inner_row))
                    break
                else:
                    break
    return len(set(visible_trees)) + visible_edges


def part_II(input):

    trees = get_grid(input)


    counters = []

    for inner_col in range(1, len(trees[0:, 0]) - 1):
        for inner_row in range(1, len(trees[0]) - 1):
            # COUNTERS
            counter_right = 0
            counter_left = 0
            counter_top = 0
            counter_down = 0

            #
            for check in reversed(trees[inner_col, :inner_row]):  ## row right
                if check < trees[inner_col, inner_row]:
                    counter_left += 1
                if check >= trees[inner_col, inner_row]:
                    counter_left += 1
                    break


            for check in trees[inner_col, inner_row + 1:]:  ## row left
                if check < trees[inner_col, inner_row]:
                    counter_right += 1
                if check >= trees[inner_col, inner_row]:
                    counter_right += 1
                    break

            for check in reversed(trees[:inner_col, inner_row]):  ## column nach oben
                if check < trees[inner_col, inner_row]:
                    counter_top += 1
                if check >= trees[inner_col, inner_row]:
                    counter_top += 1
                    break

            for check in trees[inner_col + 1:, inner_row]:  ## column nach unten
                if check < trees[inner_col, inner_row]:
                    counter_down += 1
                if check >= trees[inner_col, inner_row]:
                    counter_down += 1
                    break

            counters.append((counter_right*counter_left*counter_down*counter_top))
    return max(counters)


print(f"PART I {part_I(cmds)}")
print(f"PART II {part_II(cmds)}")
