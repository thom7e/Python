# FBFBBFFRLR
# F means front
# B means back
# L means left
# R means right


ticket = list("FFFBBBFRRR")
#print(ticket)
#ticket = list(ticket_strip[0])

#print(ticket[0])
rows = list(range(0,128))
seats = list(range(0,8))

for t in range(len(ticket)):
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

	#print(seats)
	#print(rows)
print(seats[0]+rows[0]*8)

#print("Reihe "  + str(rows))
#print("Sitz " + str(seats))
#print("ID " + str(rows[0]*8+seats[0]))
