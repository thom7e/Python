
possibilities = []

counter = 0
for password in range(138241,674034+1):
    x = [int(a) for a in str(password)]
    if len(x) == 6:
        if x[0] <= x[1] <=x[2] <= x[3] <= x[4] <= x[5]:
            if x[0] == x[1] or x[1] == x[2] or x[2] == x[3] or x[3] == x[4] or x[4] == x[5]:

                if x[0] == x[1] == x[2] == x[3] or x[1] == x[2] == x[3] == x[4] or x[2] == x[3] == x[4] == x[5]:
                    if x.count(x[0]) <= 4 and x.count(x[1]) <=4 and x.count(x[2]) <= 4:
                        if len(set(x)) == 2:
                            print(x)
                            counter +=1
                            #print(x)
                if x[0] == x[1] == x[2] or x[1] == x[2] == x[3] or x[2] == x[3] == x[4] or x[3] == x[4] == x[5]:
                    if x.count(x[0]) <= 3 and x.count(x[1]) <=3 and x.count(x[2]) <= 3 and x.count(x[3]) <= 3:
                        if len(set(x)) == 3:
                            counter +=1
                            #print(x)
print(counter)

counter2 = 0
for passwords in range(138241, 674034 + 1):
    digits = [int(x) for x in str(passwords)]
    has_pair = any([(i == 0 or digits[i]!=digits[i-1]) and digits[i] == digits[i+1] and (i==len(digits)-2 or digits[i]!=digits[i+2]) for i in range(len(digits)-1)])
    has_dec = any([digits[i] > digits[i+1] for i in range(len(digits)-1)])
    if has_pair and not has_dec:
        counter += 1
print(counter2)




