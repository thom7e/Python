row = []
with open('day18test') as f:
    for rows in f:
        row.append(rows.replace("\n",""))
        
import re

for exp in row:
    klammer = exp.split(")")
    print(klammer)

