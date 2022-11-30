from string import ascii_lowercase
from collections import Counter

ans = []
with open("day6") as file:
	ans = file.read().split("\n\n")

# answers = []
# for i in range(len(ans)):
# 	x = ans[i].split("\n")
# 	answers.append(x)

counter = []
groupsize = []


for a in ans:	
	x = a.count("\n")+1
	y = Counter(a)
	
	for z in y.values():
		if z == x:
			counter.append(1)


print(sum(counter))

