with open("day-4-trial.input") as input:
    lines = input.read().splitlines()

print(lines[0])

# Filtering
for line in lines:
    date = line.split(" ")[0].split("-")[1:]
    hour = int(line.split(" ")[1].split(":")[0])
    minute = int(line.split(" ")[1].split(":")[1].split("]")[0])
    if "#" in line:
        guard = line.split(" ")[3].split("#")[-1]
        print(guard)
    else:
        action = line.split(" ")[-1]
        print(action)
    print(date,hour,minute)