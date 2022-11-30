player1 = []
with open("player1") as p1:
    pl1 = p1.read().splitlines()
    for p in pl1:
        player1.append(int(p))

player2 = []
with open("player2") as p2:
    pl2 = p2.read().splitlines()
    for pp in pl2:
        player2.append(int(pp))


while not len(player1) == 0 and len(player2) != 0 or not len(player2) == 0 and len(player1) != 0:

    if player1[0] > player2[0]:
        player1.append(player1[0])
        player1.append(player2[0])
        player1.pop(0)
        player2.pop(0)

    elif player2[0] > player1[0]:
        player2.append(player2[0])
        player2.append(player1[0])
        player1.pop(0)
        player2.pop(0)

print(player1)
print(player2)

if len(player1) > 0:
    player1.reverse()
    erg = []
    for i in range(len(player1)):
        erg.append(player1[i] * (i + 1))
    print(sum(erg))

if len(player2) > 0:
    player2.reverse()
    erg1 = []
    for ii in range(len(player2)):
        erg1.append(player2[ii] * (ii + 1))
    print(sum(erg1))















