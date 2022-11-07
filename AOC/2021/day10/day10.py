jolts = []

with open("day10") as f:
    for j in f:
        jolts.append(int(j))

jolts.append(0)
xs = sorted(jolts)
xs.append(max(xs) + 3)

keys = []
for i in jolts:
    keys.append(i)

einser = 0
dreier = 0

for i in keys:
    if i + 3 in xs:
        dreier += 1
    if i + 1 in xs:
        einser += 1
    if i + 3 in xs and i + 1 in xs:
        dreier -= 1

print(einser*dreier)

DP = {}


def dp(i):
    if i == len(xs) - 1:
        return 1
    if i in DP:
        return DP[i]
    ans = 0
    for j in range(i + 1, len(xs)):
        if xs[j] - xs[i] <= 3:
            ans += dp(j)
    DP[i] = ans
    return ans


print(dp(0))
