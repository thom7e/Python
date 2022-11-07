import re
with open("day7bsp") as file:
	ans = file.read().split("\n")


arten=[]
for a in ans:
	arten.append("".join(a.split("\n")))

#print(arten[1])
aufgeteilt = []

for art in range(len(arten)):
	aufgeteilt.append(arten[art].split("contain"))

#Hier ist in index
comma = []
for a in range(len(aufgeteilt)):
	comma.append(aufgeteilt[a][1].split(","))


liste = []
liste2=[]
for c in range(len(comma)):
	#print(comma[c])
	liste.append(comma[c])
for l in liste:
	liste2.append(l)
	#print(l)
		
#bprint(liste2[1])

alles = []
for ll in liste2:
	alles.append(ll)

print(alles[0][0])
print(alles[0])
print(len(alles[0]))
every = []
for aa in range(len(alles)):
	for aaa in range(len(alles[aa])):
		every.append(alles[aa][0])

print(every)

anzahl = []
inhalt=[]
alle=[]

for art in range(len(arten)):
	aufgeteilt.append(str((arten[art].split("contain"))))
anzahl = []
inhalt=[]
for such in arten:
	inhalt.append(re.search(r"\d{1}? shiny gold ",such))
	x = re.search(r"\d{1}? shiny gold ",such)
	if re.search(r"\d{1}? shiny gold ",such):
		y = "".join(re.findall(r"[0-9]",x.group()))
		anzahl.append(int(y))

for such2 in arten:
		for bla in every:
			inhalt.append(re.search(r"\d{1}? str(every) ",such))
			x = re.search(r"\d{1}? shiny gold ",such)

	# for zahlen in x:
	# 	print(zahlen)
	# 	#print(re.findall(r"[0-9]",zahlen))

print(inhalt)
print(sum(anzahl))