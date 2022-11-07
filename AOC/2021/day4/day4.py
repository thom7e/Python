import re
import pandas as pd
import numpy as np
import csv
import re

passports = []
f = open(r"day4.csv", "r")
r = csv.reader(f,delimiter=";")

liste = []
for row in r:
	liste.append(row)

counter = 0
for i in range(0,len(liste),1):
	if re.search(r"byr:",str(liste[i])) and re.search(r"iyr:",str(liste[i])) and re.search(r"eyr:",str(liste[i])) and re.search(r"hgt:",str(liste[i])) and re.search(r"hcl",str(liste[i])) and re.search(r"ecl",str(liste[i])) and re.search(r"pid",str(liste[i])):
		counter = counter + 1

# print(counter)


# print("".join(re.findall(r"\d{4}","".join(re.search(r"byr:\d{4} ",str(liste[0])).group()))))
# print("".join(re.findall(r"\d{4}","".join(re.search(r"iyr:\d{4} ",str(liste[0])).group()))))
# print("".join(re.findall(r"\d{4}","".join(re.search(r"eyr:\d{4} ",str(liste[0])).group()))))

# try:
# 	print("".join(re.findall(r"\d{3}","".join(re.search(r"hgt:\d{3}cm",str(liste[0])).group()))))
# 	print("".join(re.findall(r"\d{2}","".join(re.search(r"hgt:\d{2}in",str(liste[0])).group()))))
# except IndentationError:
# 	pass
# except AttributeError:
# 	pass

# print(re.search(r"hcl:#\w{6}",str(liste[i])).group())
# try:
# 	print(re.search(r"ecl:amb ",str(liste[i])).group() or re.search(r"ecl:blu ",str(liste[i])).group() or re.search(r"ecl:brn ",str(liste[i])).group() or re.search(r"ecl: gry",str(liste[i])).group() or re.search(r"ecl:grn ",str(liste[i])).group() or re.search(r"ecl:hzl",str(liste[i])).group() or re.search(r"ecl:oth",str(liste[i])).group())
# except AttributeError:
# 	pass
# print(re.search(r"pid:[0-9]{9}",str(liste[i])).group())
# j = 0

# byr = "".join(re.findall(r"\d{4}","".join(re.search(r"byr:\d{4} ",str(liste[j])).group())))
# iyr = "".join(re.findall(r"\d{4}","".join(re.search(r"iyr:\d{4} ",str(liste[j])).group())))
# eyr = "".join(re.findall(r"\d{4}","".join(re.search(r"eyr:\d{4} ",str(liste[j])).group())))
# hgtcm = "".join(re.findall(r"\d{3}","".join(re.search(r"hgt:\d{3}cm",str(liste[j])).group())))
# hgtin = "".join(re.findall(r"\d{2}","".join(re.search(r"hgt:\d{2}in",str(liste[j])).group())))
# hcl = re.search(r"hcl:#\w{6}",str(liste[j])).group()
# ecl = re.search(r"ecl:amb ",str(liste[j])).group() or re.search(r"ecl:blu ",str(liste[j])).group() or re.search(r"ecl:brn ",str(liste[j])).group() or re.search(r"ecl: gry",str(liste[j])).group() or re.search(r"ecl:grn ",str(liste[j])).group() or re.search(r"ecl:hzl",str(liste[j])).group() or re.search(r"ecl:oth",str(liste[j])).group()

zaehler = 0
for j in range(0,len(liste),1):
	try:
		if int("".join(re.findall(r"\d{4}","".join(re.search(r"byr:\d{4} ",str(liste[j])).group())))) <= 2002 and int("".join(re.findall(r"\d{4}","".join(re.search(r"byr:\d{4} ",str(liste[j])).group())))) >= 1920:
	except AttributeError:
		pass
	except	IndentationError:
		pass
			try:
				if int("".join(re.findall(r"\d{4}","".join(re.search(r"iyr:\d{4} ",str(liste[j])).group())))) <= 2020 and int("".join(re.findall(r"\d{4}","".join(re.search(r"iyr:\d{4} ",str(liste[j])).group())))) >= 2010:
			except AttributeError:
				pass
					try:
						if int("".join(re.findall(r"\d{4}","".join(re.search(r"eyr:\d{4} ",str(liste[j])).group())))) <= 2030 and int("".join(re.findall(r"\d{4}","".join(re.search(r"eyr:\d{4} ",str(liste[j])).group())))) >= 2020:
					except AttributeError:
						pass
							try:
								if int("".join(re.findall(r"\d{3}","".join(re.search(r"hgt:\d{3}cm",str(liste[j])).group())))) <= 193 and int("".join(re.findall(r"\d{3}","".join(re.search(r"hgt:\d{3}cm",str(liste[j])).group())))) >= 150:
							except AttributeError:
								pass
									try:
										if int("".join(re.findall(r"\d{2}","".join(re.search(r"hgt:\d{2}in",str(liste[j])).group())))) <= 76 and int("".join(re.findall(r"\d{2}","".join(re.search(r"hgt:\d{2}in",str(liste[j])).group())))) >=59:
									except AttributeError:
										pass
											try:
												if re.search(r"hcl:#\w{6}",str(liste[j])).group():
											except AttributeError:
												pass
													try:
														if re.search(r"ecl:amb ",str(liste[j])).group() or re.search(r"ecl:blu ",str(liste[j])).group() or re.search(r"ecl:brn ",str(liste[j])).group() or re.search(r"ecl: gry",str(liste[j])).group() or re.search(r"ecl:grn ",str(liste[j])).group() or re.search(r"ecl:hzl",str(liste[j])).group() or re.search(r"ecl:oth",str(liste[j])).group():
													except AttributeError:
														pass
															zaehler = zaehler + 1
			
	
								
print(zaehler)

# zaehler = 0
# for j in range(0,len(liste),1):
	

# 	try:
# 		if int("".join(re.findall(r"\d{4}","".join(re.search(r"byr:\d{4} ",str(liste[j])).group())))) <= 2002 and int("".join(re.findall(r"\d{4}","".join(re.search(r"byr:\d{4} ",str(liste[j])).group())))) >= 1920:
# 			#zaehler = zaehler + 1
# 	except AttributeError:
# 		pass
# 	try:	
# 		if int("".join(re.findall(r"\d{4}","".join(re.search(r"iyr:\d{4} ",str(liste[j])).group())))) <= 2020 and int("".join(re.findall(r"\d{4}","".join(re.search(r"iyr:\d{4} ",str(liste[j])).group())))) >= 2010:
# 			#zaehler = zaehler + 1
# 	except AttributeError:
# 		pass
# 	try:
# 		if int("".join(re.findall(r"\d{4}","".join(re.search(r"eyr:\d{4} ",str(liste[j])).group())))) <= 2030 and int("".join(re.findall(r"\d{4}","".join(re.search(r"eyr:\d{4} ",str(liste[j])).group())))) >= 2020:
# 			#zaehler = zaehler + 1
# 	except AttributeError:
# 		pass

# 	try:
# 		if int("".join(re.findall(r"\d{3}","".join(re.search(r"hgt:\d{3}cm",str(liste[j])).group())))) <= 193 and int("".join(re.findall(r"\d{3}","".join(re.search(r"hgt:\d{3}cm",str(liste[j])).group())))) >= 150:
# 			#zaehler = zaehler + 1

# 		if int("".join(re.findall(r"\d{2}","".join(re.search(r"hgt:\d{2}in",str(liste[j])).group())))) <= 76 and int("".join(re.findall(r"\d{2}","".join(re.search(r"hgt:\d{2}in",str(liste[j])).group())))) >=59:
# 			#zaehler = zaehler + 1
# 	except IndentationError:
# 		pass
# 	except AttributeError:
# 		pass

# 	try:	
# 		if re.search(r"hcl:#\w{6}",str(liste[j])).group():
# 			#zaehler = zaehler + 1
# 	except AttributeError:
# 		pass
# 	try:
# 		if re.search(r"ecl:amb ",str(liste[j])).group() or re.search(r"ecl:blu ",str(liste[j])).group() or re.search(r"ecl:brn ",str(liste[j])).group() or re.search(r"ecl: gry",str(liste[j])).group() or re.search(r"ecl:grn ",str(liste[j])).group() or re.search(r"ecl:hzl",str(liste[j])).group() or re.search(r"ecl:oth",str(liste[j])).group():
# 			#zaehler = zaehler + 1
# 	except AttributeError:
# 		pass
	
# 	zahler = zaehler + 1
# print(zaehler)

		
# def getAnzahl(liste,pattern):
# 	counter = 0
# 	for i in range(0,len(liste),1):
# 		if re.search(r"byr:\d{4} ",str(liste[i]))\
# 					 and re.search(r"iyr:\d{4} ",str(liste[i]))\
# 					 and re.search(r"eyr:\d{4} ",str(liste[i]))\
# 					 and re.search(r"hgt:\d{3}cm",str(liste[i])) or re.search(r"hgt:\d{2}in",str(liste[i]))\
# 					 and re.search(r"hcl:#\w{6}",str(liste[i]))\
# 					 and re.search(r"ecl:amb ",str(liste[i])) or re.search(r"ecl:blu ",str(liste[i])) or re.search(r"ecl:brn ",str(liste[i])) or re.search(r"ecl: gry",str(liste[i])) or re.search(r"ecl:grn ",str(liste[i])) or re.search(r"ecl:hzl",str(liste[i])) or re.search(r"ecl:oth",str(liste[i])) \
# 					 and re.search(r"pid:[0-9]{9}",str(liste[i])):
# 			counter = counter + 1
# 	return(counter)
# print(neueliste[0])
# print(neueliste[0][0])
# print(neueliste[0][1])
