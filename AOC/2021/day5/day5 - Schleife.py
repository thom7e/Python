# FBFBBFFRLR
# F means front
# B means back
# L means left
# R means right

#Öffnen der Dati


tickets = []
with open("day5.txt") as file:
	for row in file:
		print()
		tickets.append(row.rstrip())
print(len(tickets))

liste = []
for i in range(0,len(tickets),1):
	#ticket_strip = [tickets[i]]
	#print(len(ticket_strip))
	ticket = list(tickets[i])
	

	#print(ticket[0])
	rows = list(range(0,128))
	seats = list(range(0,8))

	for t in range(0,len(ticket),1):
		if ticket[t] == "F":
			#print("forward")
			# print(rows[0])
			# print(rows[-1])
			rows = list(range(rows[0],int((rows[-1]+rows[0])/2)+1))
			#rows = rows[rows[0]:int((rows[-1]+rows[0])/2)+1]
				
		elif ticket[t] == "B":
			#print("back")
			# print(rows)
			# print(rows[0])
			# print(rows[-1])		
			#rows = rows[int((rows[-1]+rows[0])/2)+1:rows[-1]+1]
			rows = list(range(int((rows[-1]+rows[0])/2)+1,rows[-1]+1))
		elif ticket[t] == "R":
			#print("Right")
			seats = list(range(int((seats[-1]+seats[0])/2)+1,seats[-1]+1))
		elif ticket[t] == "L":
			#print("Left")
			seats = list(range(seats[0],int((seats[-1]+seats[0])/2)+1))


			liste.append(rows[0]*8+seats[0])

print(len(liste))

print(max(liste))
#print(sorted(liste))
# print("Reihe "  + str(rows))
# print("Sitz " + str(seats))
# print("ID " + str(rows[0]*8+seats[0]))
