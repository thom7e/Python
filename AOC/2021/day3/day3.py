import numpy as np
import pandas as pd
import math
import os 
print(os.getcwd())

df = pd.read_fwf(r"day3.txt", header = None)
print(len(df))

def getZahl(a,b):
	liste = []
	i = 0
	j = 0
	for i in range(0,len(df),a):
		if j < (len((df.loc[i,0]))):
			#print(df.loc[i,0]2[j])
			if df.loc[i,0][j] == "#":
				liste.append("yes")
			j = j+b
		else:
			j = j - (len((df.loc[i,0])))
			#print(df.loc[i,0][j])
			if df.loc[i,0][j] == "#":
				liste.append("yes")
			j = j+b
	return liste.count("yes")

erg = []
slopes = [(1,1),(1,3),(1,5),(1,7),(2,1)]

for (da,db) in slopes:
	print(getZahl(da,db))
	erg.append(getZahl(da,db))

print(math.prod(erg))
