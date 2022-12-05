
def part1():
    with open("day-3.in") as f:
        rpc = f.read().splitlines()

    letters = []
    for rucksack in rpc:
        first = rucksack[:int(len(rucksack)/2)]
        second = rucksack[int(len(rucksack)/2):]
        #print(set(''.join(sorted(first))),set(''.join(sorted(second))))
        for letter in set(first):
            if letter in set(''.join(second)):
                letters.append(letter)

    #print(letters)
    buchstaben = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    werte =  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]

    counter = 0
    for wert in letters:
        for x in range(len(buchstaben)):
            if buchstaben[x] == wert:
                #print(wert,buchstaben[x],x)
                counter += x+1

    return counter

print(part1())
def part2():
    with open("day-3.in") as f:
        letters = f.read().splitlines()

    splitter = 0
    rucksack_new = []

    for x in range(len(letters)):

        if x%3 == 0:
            rucksack_new.append([x for x in letters[splitter:splitter+3]])
            splitter += 3
   # print(rucksack_new)
    summen =[]
    for group in rucksack_new:
        print(group)
        for letter in group:
            for z in ''.join(letter):
                #print(z,group[0])
                if z in group[0] and z in group[1] and z in group[2]:
                    summen.append(z)
                    break
    print(summen)

    #print(letters)
    buchstaben = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    werte =  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]

    counter = 0
    for wert in range(len(summen)):
        #print(wert)
        if (wert+1)%3 == 0:
            print(wert)

            for k in range(len(buchstaben)):
                if buchstaben[k] == summen[wert]:
                    #print(wert,buchstaben[x],x)
                    counter += k+1

    return counter
print(part2())