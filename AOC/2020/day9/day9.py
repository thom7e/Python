numbers = []

with open("day9") as f:
    zahlen = f.read().splitlines()

def partone(zahlen):
    for zahl in range(len(zahlen)):
        start = 0
        end = 24
        fuenfer = []
        #print(zahlen[0])
        while end < len(zahlen):
            liste5 = (int(zahlen[start]), int(zahlen[start+1]), int(zahlen[start+2]), int(zahlen[start+3]), int(zahlen[start+4]), int(zahlen[start+5]), int(zahlen[start+6]), int(zahlen[start+7]), int(zahlen[start+8]), int(zahlen[start+9]), int(zahlen[start+10]), int(zahlen[start+11]), int(zahlen[start+12]), int(zahlen[start+13]), int(zahlen[start+14]), int(zahlen[start+15]), int(zahlen[start+16]), int(zahlen[start+17]), int(zahlen[start+18]), int(zahlen[start+19]), int(zahlen[start+20]), int(zahlen[start+21]), int(zahlen[start+22]), int(zahlen[start+23]), int(zahlen[start+24]))
            start = start + 1
            end = end + 1
            fuenfer.append(list(liste5))

    liste2 = []
    liste = [1,2,3,4,5]
    for c in range(len(liste)):
        for d in range(len(liste)):
            if liste[c] != liste[d]:
                x = liste[c] + liste[d]
                liste2.append(int(x))

    kombi = []
    for i in range(len(fuenfer)):
        #print(fuenfer[i])
        kombos = []
        for j in range(len(fuenfer[i])):
            for k in range(len(fuenfer[i])):
                if fuenfer[i][j] != fuenfer[i][k]:
                    x = fuenfer[i][j]+fuenfer[i][k]
                kombos.append(int(x))
        kombi.append(kombos)

    i = 0
    for test in range(len(zahlen)-25):
        if not int(zahlen[test+25]) in kombi[i]:
            print(int(zahlen[test+25]))
        i = i+1

print(partone(zahlen))

with open("day9") as f:
    for h in f.read().splitlines():
        numbers.append(int(h))

head = 0
tail = 0
target = 1492208709
print(numbers)
while head <= len(numbers):
    current_list = numbers[tail:head]
    if len(current_list) < 2:
        head += 1
    sum_list = sum(current_list)
    if sum_list == target:
        print("found solution: ")
        print(max(current_list) + min(current_list))
        break
    elif sum_list < target:
        head += 1
    elif sum_list > target:
        tail += 1
