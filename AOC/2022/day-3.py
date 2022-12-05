import string

alphabet = list(string.ascii_lowercase)+list(string.ascii_uppercase)

def part1():
    with open("day-3.in") as f:
        bagpacks = f.read().splitlines()

    letters = []
    for backpack in bagpacks:
        # divide in first and second backpack
        first = backpack[:int(len(backpack)/2)]
        second = backpack[int(len(backpack)/2):]
        # check if a letter from the first backpack is in the second backpack and append it to a list
        for letter in set(first):
            if letter in set(''.join(second)):
                letters.append(letter)

    counter = 0
    # get the amounts per letter
    for wert in letters:
        for x in range(len(alphabet)):
            # check the amount in the list alphabet
            if alphabet[x] == wert:
                #print(wert,alphabet[x],x)
                counter += x+1

    return counter

print(f"PART I: {part1()}")

def part2():
    with open("day-3.in") as f:
        letters = f.read().splitlines()

    # now we have to set the splitter to gather the 3er-packages
    splitter = 0
    backpack_new = []

    for x in range(len(letters)):
        # Modulo 3 to get every third
        if x%3 == 0:
            backpack_new.append([x for x in letters[splitter:splitter+3]])
            splitter += 3

    sums =[]

    for group in backpack_new:
        #print(group)
        for letter in group:
            for z in ''.join(letter):
                #like before, but only append if its in every group
                if z in group[0] and z in group[1] and z in group[2]:
                    sums.append(z)
                    # important to break if its true because of the loop
                    break

    counter = 0
    for wert in range(len(sums)):
        # because of the loop it's always every third letter, so skip the duplicates
        if (wert+1)%3 == 0:
            for k in range(len(alphabet)):
                if alphabet[k] == sums[wert]:
                    counter += k+1

    return counter

print(f"PART II: {part2()}")