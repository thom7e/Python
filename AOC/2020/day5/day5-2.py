#Öffnen der Dati
tickets = []
with open("day5.txt") as file:
	for row in file:
		tickets.append(row.rstrip())
#Tickets durchlaufen
liste = []
for i in range(len(tickets)):
	#Ticket in Einzelteile aufspalten
	ticket_strip = [tickets[i]]
	ticket = list(ticket_strip[0])
	#Range der Reihen und Sitze festlegen
	rows = list(range(0,128))
	seats = list(range(0,8))
	#Prüfung der Buchstaben
	for t in range(len(ticket)):
		#Immer gleiches System:
		# Bei F bleibt Index0 als unter Grenze und letzter Index+Erster Index/2 stehen.
		# +1 wegen Range, da letzte Zahl nicht dazugenomomen wird
		# Bei B genau das gleiche andersherum, bei L und R ebenso
		if ticket[t] == "F":
			rows = list(range(rows[0],int((rows[-1]+rows[0])/2)+1))
		
		elif ticket[t] == "B":
			rows = list(range(int((rows[-1]+rows[0])/2)+1,rows[-1]+1))

		elif ticket[t] == "R":
			seats = list(range(int((seats[-1]+seats[0])/2)+1,seats[-1]+1))

		elif ticket[t] == "L":
			seats = list(range(seats[0],int((seats[-1]+seats[0])/2)+1))

	#Liste erweitern mit ID's		
	liste.append(rows[0]*8+seats[0])


#Output
print("Höchste ID : " + str(max(liste)))

listsort = sorted(liste)


#Thomas Lösung

for i in range(len(listsort)-1):
	if listsort[i+1] - listsort[i] > 1:
		print("Der Sitz zwischen " + str(listsort[i+1]) + " und " + str(listsort[i]) + ".")
		#print(listsort[i])

#Elegante Lösung

seat = set(range(listsort[0],listsort[-1])) - set(listsort)
print(seat)