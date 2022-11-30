
ans = []
with open("day6") as file:
	ans = file.read().split("\n\n")
print(ans)

answers = []
for i in range(len(ans)):
	x = ans[i].replace("\n","")
	answers.append(x)

print(answers)

counter = []
for a in range(len(answers)):
	y = set(answers[a])
	counter.append(len(y))




# print(splittet)
# print(answers)
print(sum(counter))

