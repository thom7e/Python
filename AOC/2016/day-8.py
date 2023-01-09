import numpy as np

with open("day-8.in") as d:
  data = d.read().splitlines()

grid = np.zeros((6,50),dtype="str")
for col in range(len(grid)):
  for row in range(len(grid[0])):
    grid[col,row] = "."

for cmd in data:

    if cmd.split(" ")[0] == "rect":
        row = int(cmd.split(" ")[1].split("x")[0])
        col = int(cmd.split(" ")[1].split("x")[1])

        for col_ in range(col):
            for row_ in range(row):
                grid[col_, row_] = "#"
    elif cmd.split(" ")[0] == "rotate":
        rotation_value = int(cmd.split(" ")[4])
        col_num = int(cmd.split(" ")[2].split("=")[-1])
        if cmd.split(" ")[1] == "column":
            grid[:,col_num] = np.roll(grid[:,col_num],rotation_value)
        elif cmd.split(" ")[1] == "row":
            grid[col_num,:] = np.roll(grid[col_num,:],rotation_value)

counter = 0
for col in range(len(grid)):
    for row in range(len(grid[0])):
        if grid[col, row] == "#":
            counter += 1

print("PART I", counter,"\n\n")

start = 0
print("LETTERS PART II\n\n")
for x in range(10):
    print(grid[0:6,start:start+5])
    print("\n\n")
    start += 5

