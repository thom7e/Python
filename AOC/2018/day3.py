import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
with open("day3.input") as input:
    lines = input.read().splitlines()

hauptarray = []
maximal_x = []
maximal_y =  []

for maxline in lines:
    leftedge = int((maxline.split(" ")[2]).split(",")[0])
    topedge = int(((maxline.split(" ")[2]).split(",")[1]).split(":")[0])
    wideness = int((maxline.split(" ")[3]).split("x")[0])
    tallness = int((maxline.split(" ")[3]).split("x")[1])
    maximal_x.append(leftedge+wideness)
    maximal_y.append(topedge+tallness)

max_x = max(maximal_x)
max_y= max(maximal_y)

alle_arr = []

for line in lines:
    arr = np.zeros([max_x + 2, max_y + 2], dtype=int)
    ## Anweisungen
    number = int((line.split(" ")[0]).split("#")[1])
    leftedge = int((line.split(" ")[2]).split(",")[0])
    topedge = int(((line.split(" ")[2]).split(",")[1]).split(":")[0])
    wideness = int((line.split(" ")[3]).split("x")[0])
    tallness = int((line.split(" ")[3]).split("x")[1])
    #print(number, leftedge,topedge,wideness,tallness)

    ## Array
    for x in range(0,leftedge+wideness+2):
        for y in range(0,topedge+tallness+2):
            arr[x,y] = 0
    for x1 in range(topedge, topedge+tallness):
        for x2 in range(leftedge, leftedge+wideness):
            #print(x1,x2)
            arr[x1,x2] = 1
    alle_arr.append(arr)

all_arr = sum(alle_arr)
#print(all_arr)
maximalwert = np.max(all_arr)
print(maximalwert)
#print(maximalwert)
counter = 0

unique, counts = np.unique(all_arr,return_counts=True)
print(sorted(zip(unique, counts)))
total_double_matched = counts[2:].sum()
print('Total double matched : {}'.format(total_double_matched))
#print(all_arr)
#for maxwert in np.nditer(all_arr):
#   if maxwert == maximalwert:
#       counter +=1


#print(counter)
#print(counter)
#test = [1,2,3,4,5]
#for x in range(len(test)-1):
#    lösung = test[x]+test[x+1]

#print(lösung)