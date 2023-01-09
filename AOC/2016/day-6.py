from collections import Counter
with open("day-6.in") as d:
    inp = d.read().splitlines()

cols = []
for cols_ in range(len(inp[0])):
    cols.append([x[cols_] for x in inp])
#cols = "".join(cols)
error_code = []
for line in cols:
    mc = Counter(line)
    error_code.append(mc.most_common()[0][0])

print("PART I","".join(error_code))

cols = []
for cols_ in range(len(inp[0])):
    cols.append([x[cols_] for x in inp])
#cols = "".join(cols)
error_code = []
for line in cols:
    mc = Counter(line)
    error_code.append(mc.most_common()[-1][0])

print("PART II", "".join(error_code))