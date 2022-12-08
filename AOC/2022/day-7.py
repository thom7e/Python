from collections import defaultdict

with open("day-7.in") as d:
    cmds = d.read().splitlines()

all = defaultdict(int)

path = []


for line in cmds:
    if line.split(" ")[1] == "ls":
        continue
    elif line.split(" ")[0] == "dir":
        continue

    elif line.split(" ")[1] == "cd":
        if line.split(" ")[2] == "..":
            path.pop()
        else:
            path.append(line.split(" ")[2])

    else:

        amount = int(line.split(" ")[0])
        for i in range(1, len(path) + 1):
            #print(path[:i], amount)
            all["/".join(path[:i])] += amount




counter = 0
free_space_needed = 70000000-30000000
total_used = all["/"]
print(total_used)
possible_folders = []
for k,v in all.items():

    if v <= 100000:
        counter += v
    if v >= total_used-free_space_needed:
        possible_folders.append(v)

print(f"PART I: {counter}")
print(f"PART II: {min(possible_folders)}")
