with open("day14.in") as f:
    input = f.read().splitlines()

#print(input[0], input[1:-1])

#print(format(101,"b"))
mask = [x for x in input[0].split("= ")[1]]
for new_bin in range(len(mask)):
    if mask[new_bin] == "X":
        mask[new_bin] = "0"
    else:
        pass
print(format(int("".join(mask)),"b"))
for bins in input[1:]:
    new_mask = format(int(bins.split("= ")[1]),"b")


